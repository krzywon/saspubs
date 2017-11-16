import paramiko

DEBUG = False
RETRIEVE_METHOD = "ssh" # or "ftp" or "urllib"
MAX_FTP_RETRIES = 5
HOST_PORT = 22

dest_host = "webster.ncnr.nist.gov"                    #hard-coded
dest_port = 22

# I have a different key for pushing to webster.
# TODO: move these to command line arguments.
dest_pkey = paramiko.RSAKey(filename='/home/bbm/.ssh/datapushkey')
dest_username = "bbm"

# Now initialize the transfer to the destination:    
dest_transport = paramiko.Transport((dest_host, dest_port))
dest_transport.connect(username = dest_username, pkey = dest_pkey)
dest_transport.window_size = 2147483647
dest_transport.use_compression(True)
dest_sftp = paramiko.SFTPClient.from_transport(dest_transport)

def push_item(path, data, make_temporary=True):
    dest_path = path if not make_temporary else path + ".tmp"
    f = dest_sftp.open(dest_path, 'w')
    f.write(data)
    f.close()
    if make_temporary:
        dest_sftp.rename(dest_path, path)
