import os
import paramiko

DEST_HOST = "github.com/sas_pubs"
DEST_PKEY_FILE_PATH = "Z:\.ssh"
DEST_PKEY_FILE = 'z:\.ssh\id_rsa.pub'
DEST_USERNAME = "krzywon"


class SSHConnection(object):
    def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sftp = None
        
    def connect(self, host=DEST_HOST, username=DEST_USERNAME, pkey=DEST_PKEY_FILE, pkey_passphrase=None):
        self.ssh.connect(host, username=username, key_filename=pkey)
        self.sftp = paramiko.SFTPClient.from_transport(self.ssh)
        
    def write_data(self, remote_path, data, make_temporary=True):
        dest_path = remote_path if not make_temporary else remote_path + ".tmp"
        f = self.sftp.open(dest_path, 'w')
        f.write(data)
        f.close()
        if make_temporary:
            self.sftp.posix_rename(dest_path, remote_path)


if __name__ == '__main__':
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())
        if os.path.exists(os.path.normpath(DEST_PKEY_FILE_PATH)):
            print("File path is correct.")
            client.connect("github.com", username=DEST_USERNAME, key_filename=DEST_PKEY_FILE)
            stdin, stdout, stderr = client.exec_command('ls')
            print(stdout.readlines())
        else:
            print("File path does not exist.")

    finally:
        client.close()
