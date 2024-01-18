# begin.py
import os
# Content to be written in workfile.py
workfile_content = """
# import package
from gpycraft.googleSheet.gsheetsdb import gsheetsdb as gb
from gpycraft.fireStore.firestoreupload import firestoreupload
from gpycraft.app_config import Admin
import os

# Instantiate the Admin class
admin_instance = Admin()
os.environ['SHEET_NUMBER'] = ''
# Access the variables from the admin instance
credentials_path = admin_instance.credentials_path
sheetNumber = os.environ.get('SHEET_NUMBER')
sheet_url = admin_instance.sheet_url(sheet_number=sheetNumber)
storage_bucket = admin_instance.storage_bucket



# begin by instanciating the class
gsheets_instance = gb(credentials_path, sheet_url, sheet_number=sheetNumber)
fire_instance = firestoreupload(storage_bucket=storage_bucket, credentials_path=credentials_path)
"""
# Content to be written in app_config.yaml
app_config_content = """
credentials_path: credentials.json
storage_bucket: 
sheets:
  - sheet_number: 
    sheet_name: 
    sheet_url: 
"""
# Write content to workfile.py
with open('workfile.py', 'w') as file:
    file.write(workfile_content)

print("workfile.py created successfully.")

# Write content to app_config.yaml
with open('app_config.yaml', 'w') as file:
    file.write(app_config_content)

print("app_config")