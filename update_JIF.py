import os
import json

import JIF

INSTRUMENTS = [
    "MAGIK",
]

DB_DIR = "./csl_data"

def update_JIF_inplace(instrument):
    db_file_path = os.path.join(DB_DIR, instrument + ".json")
    db = json.loads(open(db_file_path).read())
    JIF.update_JIF_by_either(db.values())
    open(db_file_path, "w").write(json.dumps(db))

if __name__=='__main__':
    import sys
    if len(sys.argv) > 1:
        update_JIF_inplace(sys.argv[1])
        
    else: 
        for instrument in INSTRUMENTS:
            update_JIF_inplace(instrument)
