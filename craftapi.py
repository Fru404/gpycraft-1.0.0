from flask import Flask, jsonify,request
import gspread
from oauth2client.service_account import ServiceAccountCredentials


app = Flask(__name__)

# Define scope and credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the Google Sheet

  # Replace 'Your Google Sheet Name' with your actual sheet name

# Define API endpoint to fetch data
@app.route('/api/data', methods=['GET'])
def get_data():
    sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/15FfUKjivLLftJ3R0eDVuxUYRFJd6pyWWOc8vWxTiLlA/edit#gid=0').sheet1
    data = sheet.get_all_records()
    
    return jsonify(data)
@app.route('/api/append_record', methods=['POST'])
def append_record():
    sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/15FfUKjivLLftJ3R0eDVuxUYRFJd6pyWWOc8vWxTiLlA/edit#gid=0').sheet1
    data = sheet.get_all_records()  # Get data from the request body
    
    # Extract data for the new record
    data = request.get_json()  # Get data from the request body
    
    # Extract the value for the 'name' key
    name = data.get('name')  # Assuming 'name' is the key for the value to be appended
    
    # Append the new record to the Google Sheet
    sheet.append_row([name])
    # Append the new record to the Google Sheet
    
    
    return jsonify({'message': 'Record appended successfully'})

if __name__ == '__main__':
    app.run(debug=True)
