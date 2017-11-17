import json
import os

from server_sftp import SFTPConnection
from config import INSTRUMENTS, DB_PATH, DB_FILENAME_FMT, VERSION_FILENAME_FMT, REMOTE_PATH

def push_instrument(instrument):
    db_filename = DB_FILENAME_FMT.format(instrument=instrument)
    db_fullpath = os.path.join(DB_PATH, db_filename)
    version_filename = VERSION_FILENAME_FMT.format(db_path=DB_PATH, instrument=instrument)
    version_fullpath = os.path.join(DB_PATH, version_filename)
    if not os.path.exists(db_fullpath):
        # nothing to push
        return
    else:
        if os.path.exists(version_fullpath):
            version_info = json.loads(open(version_fullpath, 'r').read())
        else:
            version_info = {}
        new_mtime = os.stat(db_fullpath).st_mtime
        old_mtime = version_info.get("file_mtime", 0)
        if new_mtime > old_mtime:
            server_connection = SFTPConnection()
            server_connection.connect()
            server_connection.sftp.put(db_fullpath, REMOTE_PATH + 'data/' + db_filename)
            version_info["file_mtime"] = new_mtime
            open(version_fullpath, "w").write(json.dumps(version_info, 2))
            
if __name__=='__main__':
    import sys
    if len(sys.argv) > 1:
        push_instrument(sys.argv[1], server_connection)
        
    else: 
        for instrument in INSTRUMENTS:
            push_instrument(instrument, server_connection)
