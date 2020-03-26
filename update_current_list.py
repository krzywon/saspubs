import os
import json
import datetime

from config import GROUPS, DB_FILENAME_FMT, DB_PATH, VERSION_FILENAME_FMT,\
    crossref_keys_to_update
from instrument_zotero_feed import append_from_crossref, extract_doi
from instrument_zotero_feed import main as zotero_feed_main


def older_duplicates(db, keys):
    accessed = [db[key]['accessed']['date-parts'][0] if key in db.keys() and
                'accessed' in db[key].keys() and 'date-parts' in
                db[key]['accessed'].keys() else [1900, 1, 1] for key in keys]
    dates = [datetime.date(acc[0], acc[1], acc[2]) for acc in accessed]
    return keys.pop(dates.index(min(dates)))


def check_all_against_current(update_group, zotero_key=''):
    csl_db_filename = DB_FILENAME_FMT.format(group=update_group)
    csl_db_path = os.path.join(DB_PATH, csl_db_filename)
    db = json.loads(open(csl_db_path, 'r').read())
    remove_list = []
    doi_dict = dict([(key, extract_doi(item)) for key, item in db.items()])
    duplicate_dict = {}  # {doi: [key1, key2, ... , keyN]}
    for key, doi in doi_dict.items():
        if doi and doi in duplicate_dict.keys():
            duplicate_dict[doi].append(key)
        else:
            duplicate_dict[doi] = [key]
    remove_list.extend(older_duplicates(db, key_list) for doi, key_list in
                       duplicate_dict.items() if len(key_list) > 1)
    update_list = [item for item in db.values()]
    changes = append_from_crossref(update_list,
                                   keys_to_update=crossref_keys_to_update,
                                   values_to_delete=remove_list,
                                   group=update_group, api_key=zotero_key)
    if changes:
        version_filename = VERSION_FILENAME_FMT.format(group=update_group)
        version_path = os.path.join(DB_PATH, version_filename)
        os.remove(csl_db_path)
        os.remove(version_path)
        zotero_feed_main([update_group])


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 2:
        check_all_against_current(sys.argv[1], zotero_key=sys.argv[2])
    elif len(sys.argv) > 1:
        check_all_against_current(sys.argv[1])
    else:
        for group in GROUPS:
            check_all_against_current(group)
