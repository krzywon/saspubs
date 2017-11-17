import requests
import json
import os
import urllib
import re

try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote

from config import INSTRUMENTS, crossref_keys_to_import, DB_PATH, DB_FILENAME_FMT, VERSION_FILENAME_FMT
import JIF

DEBUG = True

VERSIONS = "format=versions"
ZOTERO_API = "https://api.zotero.org"

TARGET_DIRECTORY = "./"

DOI_IN_EXTRA = re.compile(r'DOI:\s+([^\s]+)')

crossref_json_headers = {
    "Accept": "application/vnd.citationstyles.csl+json",
    "User-Agent": "NCNR Publications Manager (https://ncnr.nist.gov/publications/publications_browser.html; mailto:brian.maranville@nist.gov)"
}

zotero_to_crossref = {
    "date": ["issued", "raw"]
}



def process_zotero(instrument, include_JIF=True, filter_keys=True):
    # get revision number
    group_path = "groups/" + INSTRUMENTS[instrument]["group"]
    collection = INSTRUMENTS[instrument].get("collection", None)
    if collection:
        collection_path = group_path + "/collections/" + collection
    else:
        collection_path = group_path
    
    version_file = VERSION_FILENAME_FMT.format(db_path=DB_PATH, instrument=instrument)
    csl_db_file = DB_FILENAME_FMT.format(db_path=DB_PATH, instrument=instrument)
    if not os.path.isfile(version_file):
        version_data = {}
    else:
        version_data = json.loads(open(version_file).read())
    if not os.path.isfile(csl_db_file):
        db = {}
    else:
        db = json.loads(open(csl_db_file, 'r').read())
    collection_endpoint = ZOTERO_API + "/" + collection_path
    group_endpoint = ZOTERO_API + "/" + group_path

    old_version = version_data.get("version", 0)
    to_update = requests.get("%s/items?since=%d&format=versions" % (collection_endpoint, old_version)).json()
    deleted_data = requests.get("%s/deleted?since=%d&format=json" % (group_endpoint, old_version)).json()
    keys_to_update = list(to_update.keys())
    number_to_update = len(keys_to_update)
    number_to_delete = len(deleted_data.get("items", []))
    if number_to_update == 0 and number_to_delete == 0:
        # then nothing has changed.  we're done.
        return
        
    new_version = max(list(to_update.values()))
    counter = 0
    step = 25 # can only get a limited number of items from zotero at once
    new_data = []
    while counter < number_to_update:
        key_subset = keys_to_update[counter:counter+step]
        key_subset_str = ",".join(key_subset)
        print(key_subset)
        partial_data = requests.get("%s/items?format=csljson&itemKey=%s" % (collection_endpoint, key_subset_str)).json()
        new_data.extend(partial_data["items"])
        print(partial_data["items"])
        counter += step
    if DEBUG: print("new data:", len(new_data), [item['id'] for item in new_data])
    deleted_data = requests.get("%s/deleted?since=%d&format=json" % (group_endpoint, old_version)).json()
    if DEBUG: print("to delete:", deleted_data)

    for key, item in zip(keys_to_update, new_data):
        #key = item['key']
        data = item
        db[key] = data
        if 'DOI' in data and not data['DOI'] == "":
            crossref_data = csl_from_crossref(data['DOI'])
            if crossref_data is not None: 
                db[key].update(crossref_data)
        elif DOI_IN_EXTRA.match(data.get("extra", "")):
            DOI = DOI_IN_EXTRA.match(data.get("extra", "")).groups()[0]
            crossref_data = csl_from_crossref(DOI)
            if crossref_data is not None: 
                db[key].update(crossref_data)
                
    for key in deleted_data['items']:
        del db[key]
        
    version_data["version"] = new_version
    open(version_file, "w").write(json.dumps(version_data, indent=2))
    if include_JIF:
        JIF.update_JIF_by_either(db.values())
    open(csl_db_file, "w").write(json.dumps(db))
    
def csl_from_crossref(doi):
    escaped_doi = quote(doi)
    if DEBUG: print(doi, escaped_doi)
    transform = "application/vnd.citationstyles.csl+json"
    mailto = "mailto:brian.maranville@nist.gov"
    request_url = "https://api.crossref.org/works/{doi}/transform/{transform}?{mailto}".format(doi=escaped_doi, transform=transform, mailto=mailto)
    rj = requests.get(request_url)
    try: 
        content = rj.json()
        return content
    except Exception as e:
        print("not processing doi: %s because of error: %s" % (doi,str(e)))
        return None

if __name__=='__main__':
    import sys
    if len(sys.argv) > 1:
        process_zotero(sys.argv[1])
        
    else: 
        for instrument in INSTRUMENTS:
            process_zotero(instrument)
