import paramiko

# TODO: Modify host params and use SSH, not SFTP

DEST_HOST = ""
DEST_PORT = 22
DEST_PKEY_FILE = ''
DEST_USERNAME = ""

class SFTPConnection(object):
    def __init__(self, dest_host=DEST_HOST, dest_port=DEST_PORT):
        self.transport = paramiko.Transport((dest_host, dest_port))
        self.sftp = None
        
    def connect(self, username=DEST_USERNAME, pkey_file=DEST_PKEY_FILE, pkey_passphrase=None):
        pkey = paramiko.RSAKey(filename=pkey_file, password=pkey_passphrase)
        self.transport.connect(username=username, pkey=pkey)
        self.transport.window_size = 2147483647
        self.transport.use_compression(True)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        
    def write_data(self, remote_path, data, make_temporary=True):
        dest_path = remote_path if not make_temporary else remote_path + ".tmp"
        f = self.sftp.open(dest_path, 'w')
        f.write(data)
        f.close()
        if make_temporary:
            self.sftp.posix_rename(dest_path, remote_path)
            
