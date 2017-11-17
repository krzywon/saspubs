import json
import os

from config import INSTRUMENTS, DB_PATH, DB_FILENAME_FMT, VERSION_FILENAME_FMT, REMOTE_PATH

def push_instrument(instrument, server_connection):
    db_filename = DB_FILENAME_FMT.format(db_path=DB_PATH, instrument=instrument)
    version_path = VERSION_FILENAME_FMT.format(db_path=DB_PATH, instrument=instrument)
    if not os.path.exists(db_filename):
        # nothing to push
        return
    else:
        if os.path.exists(version_path):
            version_info = json.loads(open(version_path, 'r').read())
        else:
            version_info = {}
        new_mtime = os.stat(db_filename).st_mtime
        old_mtime = version_info.get("file_mtime", 0)
        if new_mtime > old_mtime:
            server_connection.sftp.put(db_filename, REMOTE_PATH + db_filename)
            version_info["file_mtime"] = new_mtime
            open(version_path, "w").write(json.dumps(version_info, 2))
            
if __name__=='__main__':
    import sys
    from server_sftp import SFTPConnection
    server_connection = SFTPConnection()
    server_connection.connect()
    if len(sys.argv) > 1:
        push_instrument(sys.argv[1])
        
    else: 
        for instrument in INSTRUMENTS:
            push_instrument(instrument)
