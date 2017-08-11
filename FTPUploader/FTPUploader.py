from os import path
import paramiko


class FTPUploader(object):
    def __init__(self, debug=False):
        self.debug = debug
        self.login = 'jason'
        self.password = 'sallyhay3s'

    def upload_file(self, destination, remote_directory, file_to_upload):
        if self.debug: print("FTPUploader.FTPUploader: Destination=%s" % destination)
        if self.debug: print("FTPUploader.FTPUploader: Remote Directory=%s" % remote_directory)
        if self.debug: print("FTPUploader.FTPUploader: File=%s" % file_to_upload)

        # upload image to remote server
        with Server(self.login, self.password, destination) as server:
            # base = path.basename('image.jpg')
            # server.upload('image.jpg', path.join(remote_dir, base))

            base = path.basename(file_to_upload)
            if self.debug: print("FTPUploader.FTPUploader: base=%s" % base)

            server.upload(file_to_upload, path.join(remote_directory, base))


class Server(object):
    """
    Wraps paramiko for super-simple SFTP uploading and downloading.
    """

    def __init__(self, username, password, host, port=22):

        self.transport = paramiko.Transport((host, port))
        self.transport.connect(username=username, password=password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def upload(self, local, remote):
        self.sftp.put(local, remote)

    def download(self, remote, local):
        self.sftp.get(remote, local)

    def close(self):
        """
        Close the connection if it's active
        """

        if self.transport.is_active():
            self.sftp.close()
            self.transport.close()

    # with-statement support
    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.close()