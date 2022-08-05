import pysftp


def DownloadSFTPFile(hostname,port,s_username,s_password,hostkey,sftp_filePath,desinationPath):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = hostkey
    with pysftp.Connection(hostname, port =port, username=s_username, password=s_password,cnopts = cnopts ) as sftp:
            sftp.get(sftp_filePath,desinationPath)      
            sftp.close()

def UploadSFTPFile(hostname,port,s_username,s_password,hostkey,destSFTPFolderPath,uploadFilePath):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = hostkey
    with pysftp.Connection(hostname, port =port, username=s_username, password=s_password,cnopts = cnopts ) as sftp:
            sftp.cd(destSFTPFolderPath)
            sftp.put(uploadFilePath)      
            sftp.close()