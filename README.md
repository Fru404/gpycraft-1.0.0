<link href='https://fonts.googleapis.com/css?family=MedievalSharp' rel='stylesheet'>

<h1 align="center" style="color: red; font-family: 'MedievalSharp'; font-size: 22px;">GPYCRAFT</h1>

<svg fill="none" viewBox="0 0 600 300" width="600" height="300" xmlns="http://www.w3.org/2000/svg">
  <foreignObject width="100%" height="100%">
    <div xmlns="http://www.w3.org/1999/xhtml">
      <style>
        .container {
          display: flex;
          width: 100%;
          height: 300px;
          background-color: black;
          color: white;
        }
      </style>

      <div class="container">
        <h1>Hi there, my name is Nikola 👋</h1>
      </div>
    </div>
  </foreignObject>
</svg>


<p align="center">
    <img src="https://raw.githubusercontent.com/Fru404/Web/main/1497441839.svg" alt="SVG" style="width: 200px; height: 200px; display: block; margin: 0 auto;">
</p>


This python module makes it possible to manipulate google sheets or any sheets stored in firebase storage. It allows for manipulation and display sheet data in a convenient way for analysis. It supports creation of API to google sheet

Before Starting it is neccessary to have credentials.json file found in Google cloud platform and make sure the google sheet link is shareable



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