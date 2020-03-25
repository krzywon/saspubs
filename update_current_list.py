import os
import json

from config import GROUPS, DB_FILENAME_FMT, DB_PATH, crossref_keys_to_update
from instrument_zotero_feed import append_from_crossref


def check_all_against_current(update_group=''):
    if update_group is not '':
        csl_db_filename = DB_FILENAME_FMT.format(group=update_group)
        csl_db_path = os.path.join(DB_PATH, csl_db_filename)
        db = json.loads(open(csl_db_path, 'r').read())
        update_list = []
        for key in crossref_keys_to_update:
            # long hand to check why this fails
            update_list.extend([item for item in db.values() if key not in
                                item.keys()])
        append_from_crossref(update_list,
                             keys_to_update=crossref_keys_to_update)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        check_all_against_current(sys.argv[1])
    else:
        for group in GROUPS:
            check_all_against_current(group)
