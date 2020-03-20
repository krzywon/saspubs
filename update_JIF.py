import os
import json

import JIF
from config import GROUPS, DB_PATH, DB_FILENAME_FMT


def update_JIF_inplace(group):
    db_filename = DB_FILENAME_FMT.format(group=group)
    db_file_path = os.path.join(DB_PATH, db_filename)
    try:
        db = json.loads(open(db_file_path).read())
        JIF.update_JIF_by_either(db.values())
        open(db_file_path, "w").write(json.dumps(db))
    except Exception as e:
        print("could not process {group}: {error}".format(group=group,
                                                          error=str(e)))


if __name__=='__main__':
    import sys
    if len(sys.argv) > 1:
        update_JIF_inplace(sys.argv[1])
        
    else: 
        for group in GROUPS:
            update_JIF_inplace(group)
