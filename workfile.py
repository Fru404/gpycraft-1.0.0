
# import package
from gpycraft.googleSheet.gsheetsdb import gsheetsdb as gb
from gpycraft.fireStore.firestoreupload import firestoreupload
from gpycraft.app_config import Admin
import os

# Instantiate the Admin class
admin_instance = Admin()
os.environ['SHEET_NUMBER'] ='0'
# Access the variables from the admin instance
credentials_path = admin_instance.credentials_path
sheetNumber = os.environ.get('SHEET_NUMBER')
sheet_url = admin_instance.sheet_url(sheet_number=sheetNumber)
storage_bucket = admin_instance.storage_bucket

# begin by instanciating the class
gsheets_instance = gb(credentials_path, sheet_url, sheet_number=sheetNumber)
fire_instance = firestoreupload(storage_bucket=storage_bucket, credentials_path=credentials_path)

fire_instance.upload_file(local_file_path='log/None.log.1')
#fire_instance.get_file('https://storage.googleapis.com/realtime-375815.appspot.com/new.txt')

