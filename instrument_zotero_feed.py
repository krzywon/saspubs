import requests
import json
import os
import re

try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote

from config import GROUPS, DB_PATH, DB_FILENAME_FMT, VERSION_FILENAME_FMT
import JIF
from citeproc_to_html import make_page, get_date_string

DEBUG = True

VERSIONS = "format=versions"
ZOTERO_API = "https://api.zotero.org"
DEFAULT_DATESTR = "1970-01-01"

TARGET_DIRECTORY = "./"

DOI_IN_EXTRA = re.compile(r'DOI:\s+([^\s]+)')

crossref_json_headers = {
    "Accept": "application/vnd.citationstyles.csl+json",
    "User-Agent": "NCNR Publications Manager (https://ncnr.nist.gov/publications/publications_browser.html; mailto:brian.maranville@nist.gov)"
}

RETRIEVE_FROM_CROSSREF = [
    "is-referenced-by-count",
    "container-title-short",
    "article-number",
    "ISSN"
]

OVERWRITE_FROM_CROSSREF = [
    #"issued"
]

ZOTERO_CSL_MAPPINGS = {
    "journalAbbreviation": "container-title-short",
    "shortTitle": "title-short"
}


def process_zotero(group, include_JIF=True, filter_keys=True):
    # get revision number
    group_path = "groups/" + GROUPS[group]["group"]
    collection = GROUPS[group].get("collection", None)
    if collection:
        collection_path = group_path + "/collections/" + collection
    else:
        collection_path = group_path
    
    version_filename = VERSION_FILENAME_FMT.format(group=group)
    csl_db_filename = DB_FILENAME_FMT.format(group=group)
    version_path = os.path.join(DB_PATH, version_filename)
    csl_db_path = os.path.join(DB_PATH, csl_db_filename)
    if not os.path.isfile(version_path):
        version_data = {}
    else:
        version_data = json.loads(open(version_path).read())
    if not os.path.isfile(csl_db_path):
        db = {}
    else:
        db = json.loads(open(csl_db_path, 'r').read())
    collection_endpoint = ZOTERO_API + "/" + collection_path
    group_endpoint = ZOTERO_API + "/" + group_path

    old_version = version_data.get("version", 0)
    versions_rq = requests.get("{collection}/items?since={old_version:d}&format=versions&itemType=-attachment%20||%20note".format(collection=collection_endpoint, old_version=old_version))
    items_version = int(versions_rq.headers["Last-Modified-Version"])
    if not items_version > old_version:
        # no changes... we're done
        return
        
    to_update = versions_rq.json()
    
    keys_to_update = list(to_update.keys())
    number_to_update = len(keys_to_update)
    
    new_version = items_version
    counter = 0
    step = 25 # can only get a limited number of items from zotero at once
    new_data = []
    while counter < number_to_update:
        key_subset = keys_to_update[counter:counter+step]
        key_subset_str = ",".join(key_subset)
        if DEBUG: print(key_subset)
        partial_data = requests.get("%s/items?format=csljson&itemKey=%s" % (collection_endpoint, key_subset_str)).json()
        new_data.extend(partial_data["items"])
        if DEBUG: print(partial_data["items"])
        counter += step
    if DEBUG: print("new data:", len(new_data), [item['id'] for item in new_data])

    # fix incorrect keys in zotero CSL data
    remap_zotero(new_data)
    
    #for key, item in zip(keys_to_update, new_data):
    #all_from_crossref(new_data)
    append_from_crossref(new_data)
    
    for item in new_data:
        key = item["id"].split("/")[-1] #id is "ASD1234" or "12987296/ASD1234"
        db[key] = item.copy()
    
    deleted_rq = requests.get("%s/deleted?since=%d&format=json" % (group_endpoint, old_version))
    deletions_version =  int(deleted_rq.headers["Last-Modified-Version"])
    deleted_data = deleted_rq.json()
    number_to_delete = len(deleted_data.get("items", []))
    if DEBUG: print("to delete:", deleted_data)
    number_actually_deleted = 0
    for dkey in deleted_data['items']:
        if dkey in db:
            if DEBUG: print("deleting key:", dkey)
            del db[dkey]
            number_actually_deleted += 1
            
    version_data["version"] = items_version 
    # if deletions_version is newer, that's ok... 
    # (re-attempting a deletion for a stale version doesn't hurt)
    if include_JIF:
        JIF.update_JIF_by_either(db.values())
    open(csl_db_path, "w").write(json.dumps(db))
    open(version_path, "w").write(json.dumps(version_data, indent=2))
    make_page(group)


def remap_zotero(values, mappings=ZOTERO_CSL_MAPPINGS):
    keys_to_map = mappings.keys()
    for key, new_key in mappings.items():
        for item in values:
            if key in item:
                item[new_key] = item[key]
                del item[key]


def csl_from_crossref(doi):
    escaped_doi = quote(doi)
    if DEBUG: print(doi, escaped_doi)
    transform = "application/vnd.citationstyles.csl+json"
    mailto = "mailto=brian.maranville@nist.gov"
    request_url = "https://api.crossref.org/works/{doi}/transform/{transform}?{mailto}".format(doi=escaped_doi, transform=transform, mailto=mailto)
    rj = requests.get(request_url)
    try: 
        content = rj.json()
        return content
    except Exception as e:
        if DEBUG: print("not processing doi: %s because of error: %s" % (doi,str(e)))
        return {}


def extract_doi(item):
    DOI = None
    extra = item.get("extra", "")
    if 'DOI' in item and not item['DOI'] == "":
        DOI = item["DOI"]
    elif DOI_IN_EXTRA.match(extra):
        DOI = DOI_IN_EXTRA.match(extra).groups()[0]
    return DOI


def append_from_crossref(values, keys_to_update=RETRIEVE_FROM_CROSSREF, keys_to_overwrite=OVERWRITE_FROM_CROSSREF):
    # values in the overwrite list will be overwritten
    # values in the update list will be not overwrite if they exist.
    for item in values:
        DOI = extract_doi(item)
        if DOI is not None:
            crossref_data = csl_from_crossref(item['DOI'])
            for key in keys_to_update:
                if key in crossref_data and not key in item:
                    item[key] = crossref_data[key]
            for key in keys_to_overwrite:
                if key in crossref_data:
                    item[key] = crossref_data[key]
            if "issued" in item:
                try:
                    ds = get_date_string(item)
                except:
                    # if getDateString throws an error, use the crossref value
                    if DEBUG: print("processing date error: ", item, crossref_data.get("issued", "no issued"))
                    if "issued" in crossref_data:
                        item['issued'] = crossref_data['issued']
                    else:
                        item['issued'] = {'raw': DEFAULT_DATESTR}


def all_from_crossref(values):
    for item in values:
        DOI = extract_doi(item)
        if DOI is not None:
            crossref_data = csl_from_crossref(item['DOI'])
            item.update(crossref_data)


def patch_db_from_crossref(group, keys_to_patch):
    csl_db_filename = DB_FILENAME_FMT.format(group=group)
    csl_db_path = os.path.join(DB_PATH, csl_db_filename)
    db = json.loads(open(csl_db_path, 'r').read())
    append_from_crossref(db.values(), keys_to_update=keys_to_patch, overwrite=True)
    open(csl_db_path, "w").write(json.dumps(db))


if __name__=='__main__':
    import sys
    if len(sys.argv) > 1:
        process_zotero(sys.argv[1])
        
    else: 
        for group in GROUPS:
            process_zotero(group)
