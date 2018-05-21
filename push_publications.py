import json
import os

from server_sftp import SFTPConnection
from config import INSTRUMENTS, DB_PATH, DB_FILENAME_FMT, VERSION_FILENAME_FMT, REMOTE_PATH

def push_instrument(instrument):
    db_filename = DB_FILENAME_FMT.format(instrument=instrument)
    db_fullpath = os.path.join(DB_PATH, db_filename)
    html_page_path = os.path.join("static", instrument + "_pubs.html")
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
            
        new_db_mtime = os.stat(db_fullpath).st_mtime
        old_db_mtime = version_info.get("db_file_mtime", 0)
        db_push_needed = new_db_mtime > old_db_mtime
        
        new_pubs_mtime = os.stat(html_page_path).st_mtime if os.path.exists(html_page_path) else -1
        old_pubs_mtime = version_info.get("pubs_file_mtime", 0)
        pubs_push_needed = new_pubs_mtime > old_pubs_mtime
        
        if db_push_needed or pubs_push_needed:
            server_connection = SFTPConnection()
            server_connection.connect()
            if db_push_needed:
                server_connection.sftp.put(db_fullpath, REMOTE_PATH + 'data/' + db_filename)
                version_info["db_file_mtime"] = new_db_mtime
            if pubs_push_needed and os.path.exists(html_page_path):
                server_connection.sftp.put(html_page_path, REMOTE_PATH + instrument + "_pubs.html")
                version_info["pubs_file_mtime"] = new_pubs_mtime
            open(version_fullpath, "w").write(json.dumps(version_info, 2))
            
if __name__=='__main__':
    import sys
    if len(sys.argv) > 1:
        push_instrument(sys.argv[1])
        
    else: 
        for instrument in INSTRUMENTS:
            push_instrument(instrument)
