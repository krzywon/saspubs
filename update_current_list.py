import os
import json
import datetime

from config import GROUPS, DB_FILENAME_FMT, DB_PATH, crossref_keys_to_update
from instrument_zotero_feed import append_from_crossref, extract_doi


def older_duplicate(db, dup1, dup2):
    acc1 = db[dup1]['accessed']['date-parts'][0]
    acc2 = db[dup2]['accessed']['date-parts'][0]
    date_dup1 = datetime.date(acc1[0], acc1[1], acc1[2])
    date_dup2 = datetime.date(acc2[0], acc2[1], acc2[2])
    return db[dup1] if date_dup1 < date_dup2 else db[dup2]


def check_all_against_current(update_group=''):
    if update_group is not '':
        csl_db_filename = DB_FILENAME_FMT.format(group=update_group)
        csl_db_path = os.path.join(DB_PATH, csl_db_filename)
        db = json.loads(open(csl_db_path, 'r').read())
        update_list = []
        doi_dict = dict([(key, extract_doi(item)) for key, item in db.items()])
        duplicate_dict = dict([(key, list(doi_dict.keys())[list(
            doi_dict.values()).index(doi)]) for key, doi, in doi_dict.items()
                               if doi is not None])
        remove_list = [older_duplicate(db, key, value) for key, value in
                       duplicate_dict.items() if key != value]
        for key in crossref_keys_to_update:
            update_list.extend([item for item in db.values() if key not in
                                item.keys()])
        updates = append_from_crossref(update_list,
                                       keys_to_update=crossref_keys_to_update,
                                       values_to_delete=remove_list)
        if updates is not {}:
            # TODO: Do something with the updates -> jsonify?
            pass


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        check_all_against_current(sys.argv[1])
    else:
        for group in GROUPS:
            check_all_against_current(group)
