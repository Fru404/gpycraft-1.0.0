# firestoreupload.py


from firebase_admin import credentials, initialize_app, storage
import requests 
import os
import yaml
import datetime
import random
import string
from gpycraft.app_config import Admin

import logging
from logging.handlers import RotatingFileHandler

# Set the optimal logging level (adjust as needed)
logging.basicConfig(level=logging.INFO)

# Create a logger with the module name
logger = logging.getLogger(__name__)

# Configure loggers at the module level
# (You can configure the logger with additional settings if needed)
logger.setLevel(logging.DEBUG)

# Include timestamps and ensure consistent formatting
formatter = logging.Formatter('%(asctime)s- %(name)s - %(levelname)s - %(message)s')

# Create a rotating file handler
# Replace 'your_log_file.log' with the desired log file name
# Set maxBytes to the maximum size of each log file
# Set backupCount to the number of backup files to keep
file_handler = RotatingFileHandler('logFile.log', maxBytes=1024, backupCount=3)
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


class firestoreupload:
    def __init__(self, credentials_path, storage_bucket) -> None:
        """
        Initialize the FireStoreUpload class.

        :param credentials_path: Path to the Firebase service account credentials JSON file.
        :param storage_bucket: Firebase Storage bucket name.
        """
        
        
        credentials_path = credentials_path
        storage_bucket = storage_bucket
        self.file_url=''
        
        
    def generate_reference(self):
        ints = random.randrange(1000000, 10000000)
        digit = str(ints)
        letter = random.choice(string.ascii_lowercase)
        return letter + digit

    def save_message_to_yaml(self, message, message_yml):
        try:
            with open(message_yml, 'a') as yaml_file:
                yaml.dump(message, yaml_file, default_flow_style=False)
            print(f'{yaml.dump(message,default_flow_style=False)} Saved')
            logger.info(' file Saved')
        except Exception as e:
            logger.error(f'Error saving message: {e}')

    def overwrite_message_in_yaml(self, existing_data, message, message_yml):
        print(yaml.dump(existing_data,default_flow_style=False))
        user_input = input("The document already exists. Do you want to continue? (y/n): ")
        if user_input == 'y':
            existing_data.update(message)
            try:
                with open(message_yml, 'w') as yaml_file:
                    yaml.dump(existing_data, yaml_file, default_flow_style=False)
                
                print(f'{yaml.dump(message,default_flow_style=False)} Document uploaded')
                reference = existing_data['ref']
                logger.info(f' file with reference {reference} Document uploaded')
            except Exception as e:
                print(f'Error overwriting message: {e}')
                logger.debug(f'Error overwriting message: {e}')
        else:
            logger.info(f'Not uploaded')
            print(f'{yaml.dump(message,default_flow_style=False)} Not uploaded')

        

    def upload_file(self, local_file_path):
        """
        Upload a file to Firebase Storage.

        :param local_file_path: Path to the local file to be uploaded.
        """
        admin_instance = Admin()
 
        # Access the variables from the admin instance
        credentials_path = admin_instance.credentials_path
        self.local_file_path = local_file_path
        storage_bucket = admin_instance.storage_bucket
        try:
            # Initialize Firebase app with credentials and storage bucket
            cred = credentials.Certificate(credentials_path)
            initialize_app(cred, {'storageBucket': storage_bucket})

            # Get file name from the local file path
            fileName = local_file_path

            # Get reference to the default storage bucket
            bucket = storage.bucket()

            # Create a blob (object) in the bucket with the same name as the local file
            blob = bucket.blob(fileName)

            # Upload the file to Firebase Storage
            blob.upload_from_filename(fileName)

            # Make the uploaded file public
            blob.make_public()
            
            self.file_url=blob.public_url
            #keep track of time uploaded
            # Get the current date and time
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            
            # Print success message with the file URL
            ref = self.generate_reference()

            message = {
                'ref': ref,
                'file': fileName,
                'url': self.file_url,
                'time': current_time,
                '#':'################################################'
            }
            os.makedirs('catalog', exist_ok=True)
            message_yml = os.path.join('catalog', 'dossier.yaml')

            

            if os.path.exists(message_yml):
                with open(message_yml, 'r') as existing_message:
                    existing_data = yaml.safe_load(existing_message)
                    if existing_data and 'ref' in existing_data and existing_data['file'] == fileName:
                        self.overwrite_message_in_yaml(existing_data, message, message_yml)
                    else:
                        self.save_message_to_yaml(message, message_yml)
                        logger.info('file uploaded')
                        print('file uploaded')
            else:
                  logger.info('file not recieved')
                  print('file not recieved')
        except Exception as e:
                logger.error(f"Error uploading file: {e}")
                print(f"Error uploading file: {e}")
                
    def get_file(self,file_url,local_folder='local'):
        """
        Download a file from a public URL and save it to the local folder.

        :param public_url: Public URL of the file to be downloaded.
        :param local_folder: Path to the local folder to save the downloaded file.
        """
        
        try:
            if not os.path.exists(local_folder):
                os.makedirs(local_folder)
                
            file_name = os.path.join(local_folder, file_url.split('/')[-1])
            response = requests.get(file_url)

            # Save the file locally
            with open(file_name, 'wb') as file:
                file.write(response.content)
            logger.info(f" {file_name}downloaded successfully.")
            print(f"File '{file_name}' downloaded successfully.")

        except Exception as e:
            logger.error(f"Error downloading file: {e}")
            print(f"Error downloading file: {e}")
            