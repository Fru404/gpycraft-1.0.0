Google Sheets Database and Firestore Upload
This Python script provides a simple interface to interact with Google Sheets as a database and upload files to Firebase Storage. The functionality is divided into two classes - gsheetsdb for handling Google Sheets operations and FireStoreUpload for handling Firebase Storage uploads.

gsheetsdb Class
Initialization
python
Copy code
from googlepycraft.googleSheet.gsheetsdb import gsheetsdb
Initialize the gsheetsdb class with the path to your Google Sheets service account credentials JSON file and the URL of the Google Sheets document.

python
Copy code
db = gsheetsdb(credentials_path='path/to/credentials.json', sheet_url='https://docs.google.com/spreadsheets/d/your_spreadsheet_id/edit')
Reading Data from Google Sheets
read_sheet Method
python
Copy code
# Read data from Google Sheets
data = db.read_sheet(key='column_name', number_of_rows=5, start_index=1, end_index=10)
key: The column name to filter data by.
number_of_rows: The number of rows to retrieve.
start_index and end_index: The range of rows to retrieve.
Converting Data to Pandas DataFrame
in_pd Method
python
Copy code
# Convert data to Pandas DataFrame
df = db.in_pd()
Converting Data to JSON
in_json Method
python
Copy code
# Convert data to JSON
json_data = db.in_json(target_key='column_name', num_rows=5, start_index=1, end_index=10)
target_key: The specific key to include in the JSON output.
num_rows: The number of rows to include in the JSON output.
start_index and end_index: The range of rows to include in the JSON output.
FireStoreUpload Class
Initialization
python
Copy code
from googlepycraft.fireStore.firestoreupload import FireStoreUpload
Initialize the FireStoreUpload class with the path to your Firebase service account credentials JSON file and the name of your Firebase Storage bucket.

python
Copy code
uploader = FireStoreUpload(credentials_path='path/to/firebase_credentials.json', storage_bucket='your_storage_bucket_name')
Uploading Files to Firebase Storage
upload_file Method
python
Copy code
# Upload a file to Firebase Storage
uploader.upload_file(local_file_path='path/to/local/file.txt')
local_file_path: The local path of the file to be uploaded.
Example Usage
python
Copy code
# Example usage of gsheetsdb
db = gsheetsdb(credentials_path='path/to/credentials.json', sheet_url='https://docs.google.com/spreadsheets/d/your_spreadsheet_id/edit')
data = db.read_sheet(key='column_name', number_of_rows=5, start_index=1, end_index=10)
df = db.in_pd()
json_data = db.in_json(target_key='column_name', num_rows=5, start_index=1, end_index=10)

# Example usage of FireStoreUpload
uploader = FireStoreUpload(credentials_path='path/to/firebase_credentials.json', storage_bucket='your_storage_bucket_name')
uploader.upload_file(local_file_path='path/to/local/file.txt')

Note: Make sure to replace placeholders such as path/to/credentials.json, your_spreadsheet_id, your_storage_bucket_name, etc., with your actual file paths and identifiers.