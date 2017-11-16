import requests
import json
import os
import urllib
import re

# zotero group ids
#https://api.zotero.org/groups/1942669/items/top?start=0&limit=25&format=atom&v=1
#https://api.zotero.org/groups/1942669/collections/29DQ33DH/items/top?start=0&limit=25&format=atom&v=1
#https://api.zotero.org/groups/1942136/collections/5FB99F7A/items/top?start=0&limit=25&format=atom&v=1
#https://api.zotero.org/groups/1942669/collections/RV37EK44/items/top?start=0&limit=25&format=atom&v=1

INSTRUMENTS = {
    
    "MAGIK": {
        "group": "1942669",
        "collection": "29DQ33DH"
    },
    "PBR": {
        "group": "1942136",
        #"collection": "5FB99F7A"
    },
    "NG7SANS": {
        "group": "1942669",
        "collection": "RV37EK44"
    }
}

NCNR_INSTRUMENTS_ID = 1942669
VERSIONS = "format=versions"
ZOTERO_API = "https://api.zotero.org"

TARGET_DIRECTORY = "./"

DOI_IN_EXTRA = re.compile(r'DOI:\s+([^\s]+)')

crossref_json_headers = {"Accept": "application/vnd.citationstyles.csl+json"}
crossref_keys_to_import = [
    "title",
    "author",
    "container-title-short",
    "container-title",
    "volume",
    "page",
    "article-number",
    "issued",
    "ISSN",
    "DOI",
    "URL",
    "type",
    "is-referenced-by-count"
]

zotero_to_crossref = {
    "date": ["issued", "raw"]
}

CSL_DATA_PATH = "./csl_data"

def process_instrument(instrument):
    # get revision number
    group_path = "groups/" + INSTRUMENTS[instrument]["group"]
    collection = INSTRUMENTS[instrument].get("collection", None)
    if collection:
        collection_path = group_path + "/collections/" + collection
    else:
        collection_path = group_path
    
    version_file = os.path.join(CSL_DATA_PATH, '.%s_version' % (instrument))
    csl_db_file = os.path.join(CSL_DATA_PATH, instrument + ".json")
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
    #collection_data = requests.get(collection_endpoint).json()
    #new_collection_version = collection_data.get("version", -1)
    old_version = version_data.get("version", 0)
    to_update = requests.get("%s/items?since=%d&format=versions" % (collection_endpoint, old_version)).json()
    keys_to_update = list(to_update.keys())
    number_to_update = len(keys_to_update)
    new_version = max(list(to_update.values())) if number_to_update > 0 else old_version
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
    print("new data:", len(new_data), [item['id'] for item in new_data])
    deleted_data = requests.get("%s/deleted?since=%d&format=json" % (group_endpoint, old_version)).json()
    print("to delete:", deleted_data)
    for key, item in zip(keys_to_update, new_data):
        #key = item['key']
        data = item
        if 'DOI' in data and not data['DOI'] == "":
            db[key] = csl_from_crossref(data['DOI'])
        elif DOI_IN_EXTRA.match(data.get("extra", "")):
            DOI = DOI_IN_EXTRA.match(data.get("extra", "")).groups()[0]
            db[key] = csl_from_crossref(DOI)
        else:
            db[key] = data
    for key in deleted_data['items']:
        del db[key]
    version_data["version"] = new_version
    open(version_file, "w").write(json.dumps(version_data, indent=2))
    open(csl_db_file, "w").write(json.dumps(db))
    
def csl_from_crossref(doi, filter_keys=False):
    escaped_doi = urllib.parse.quote(doi)
    print(doi, escaped_doi)
    rj = requests.get("https://api.crossref.org/works/%s/transform/application/vnd.citationstyles.csl+json" % (escaped_doi,)) #, headers = crossref_json_headers)
    entry = {}
    try: 
        content = rj.json()
        if filter_keys:
            entry.update(dict([(k, content.get(k, None)) for k in crossref_keys_to_import if content.get(k, None) is not None]))
        else:
            entry.update(content)
    except Exception:
        print("not processing %s because of error: text" % (doi,))
    return entry

if __name__=='__main__':
    import sys
    if len(sys.argv) > 1:
        process_instrument(sys.argv[1])
        
    else: 
        for instrument in INSTRUMENTS:
            process_instrument(instrument)
