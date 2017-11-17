import os
import json

import JIF
from config import INSTRUMENTS, DB_PATH, DB_FILENAME_FMT

def update_JIF_inplace(instrument):
    db_file_path = DB_FILENAME_FMT.format(db_path=DB_PATH, instrument=instrument)
    try:
        db = json.loads(open(db_file_path).read())
        JIF.update_JIF_by_either(db.values())
        open(db_file_path, "w").write(json.dumps(db))
    except Exception as e:
        print("could not process {instrument}: {error}".format(instrument=instrument, error=str(e)))

if __name__=='__main__':
    import sys
    if len(sys.argv) > 1:
        update_JIF_inplace(sys.argv[1])
        
    else: 
        for instrument in INSTRUMENTS:
            update_JIF_inplace(instrument)
