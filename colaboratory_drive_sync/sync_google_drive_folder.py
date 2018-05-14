import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# These are file extensions we know PyDrive chokes when trying to download
INVALID_EXTS = ['.ipynb', '.gdoc']

def sync_google_drive_folder(folder_id):
    # 1. Authenticate and create the PyDrive client.
    auth.authenticate_user()
    gauth = GoogleAuth()
    gauth.credentials = GoogleCredentials.get_application_default()
    drive = GoogleDrive(gauth)

    # 2. Set up a local directory to store the files. Namespace using unique folder id
    LOCAL_DIRECTORY = '~/data/{}'.format(folder_id)
    LOCAL_PATH = os.path.expanduser(LOCAL_DIRECTORY)
    try:
        os.makedirs(LOCAL_PATH)
    except:
        pass

    # 3. Iterate over all files in specified Google Drive folder, and for each create file in local (colab) directory

    # Query syntax: https://developers.google.com/drive/v2/web/search-parameters
    file_list = drive.ListFile({'q': "'{}' in parents".format(folder_id)}).GetList()

    for file in file_list:
        fname = os.path.join(LOCAL_PATH, file['title'])
        
        # Only copy files that have extensions it is possible to copy
        for ext in INVALID_EXTS:
            if fname.endswith(ext):
                continue
        try:
            f_ = drive.CreateFile({'id': file['id']})
            f_.GetContentFile(fname)
        except Error as error:
            print("File name:", fname)
            print("Error:", error)

          # print('\ntitle: %s' % file['title'])
          # print('id: %s' % file['id'])
          # print('downloaded to: {}'.format(fname))

    def get_local_path(filename=''):
        return os.path.join(LOCAL_PATH, filename)

    return get_local_path
