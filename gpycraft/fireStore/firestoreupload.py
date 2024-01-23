# firestoreupload.py


from firebase_admin import credentials, initialize_app, storage
import requests 
import os
import yaml
import datetime
import random
import string
from gpycraft.app_config import Admin
import time

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
if not os.path.exists('log'):
   os.makedirs('log')
logfolder='log'
project_name = os.environ.get('project_name')
logname=project_name
logpath=os.path.join(logfolder,f'{project_name}.log')
file_handler = RotatingFileHandler(logpath, maxBytes=2048, backupCount=8)
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
            print(f'{yaml.dump(message,default_flow_style=False)}')
            
        except Exception as e:
            logger.error(f'Error saving message: {e}')






    def overwrite_message_in_yaml(self, existing_data, message, message_yml):
        print(yaml.dump(existing_data,default_flow_style=False))
        user_input = input("The document already exists. Do you want to continue? (y/n): ")

        reference = None
        if user_input == 'y':
            existing_data.update(message)
            try:
                with open(message_yml, 'w') as yaml_file:
                    yaml.dump(existing_data, yaml_file, default_flow_style=False)
                
                print(f'{yaml.dump(message,default_flow_style=False)} Document uploaded')
                reference = existing_data['ref']
                logger.info(f' file with reference {reference}  uploaded')
            except Exception as e:
                print(f'Error overwriting message: {e}')
                logger.debug(f'Error overwriting message: {e}')
        else:
            logger.info(f' file {reference} Not uploaded')
            print(f'{yaml.dump(message,default_flow_style=False)} Not uploaded')

        








    def upload_file(self, local_file_path):
        """
        Upload a file to Firebase Storage.

        :param local_file_path: Path to the local file to be uploaded.
        """
        admin_instance = Admin()
        
        message_yml = os.path.join('catalog', 'document.yaml')
        if os.path.exists(message_yml):
        
             
            # Access the variables from the admin instance
            credentials_path = admin_instance.credentials_path
            self.local_file_path = local_file_path
            storage_bucket = admin_instance.storage_bucket

            try:
                
                # Initialize Firebase app with credentials and storage bucket
                cred = credentials.Certificate(credentials_path)
                initialize_app(cred, {'storageBucket': storage_bucket})
                ref = self.generate_reference()
                
                # Get file name from the local file path
                

                # Get reference to the default storage bucket
                bucket = storage.bucket()

                # Create a blob (object) in the bucket with the same name as the local file
                
                fileName = local_file_path
                blob = bucket.blob(fileName)
                
                #current_directory = os.getcwd()
                
            # Create the full path to the file
                #doc = os.path.join(current_directory, 'catalog/document.yaml')
                
                #opening document.yaml to see if file name is there
                #with open(doc, 'r') as check:
                #    print('4')
                 #   samefile = yaml.safe_load(check)
                    
                 #   print(samefile)
                    
                    
                    
                    #default={'file':'default name'}
                    #with open(doc,'w') as y:
                     #   yaml.dump(default,y ,default_style=None)
                   
                    #if samefile and 'file' in samefile and samefile['file'].endswith(fileName) or samefile['file']=='default name':
                        
                        #print(f'File with name {fileName} already exists in the document.yaml')
                        
                        
                # Upload the file to Firebase Storage
                blob.upload_from_filename(fileName)
                print('file uploaded')

                            
                # Make the uploaded file public
                blob.make_public()
                
                self.file_url=blob.public_url
                #keep track of time uploaded
                # Get the current date and time
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                
                # Print success message with the file URL
                

                message = {
                    'ref': ref,
                    'file': fileName,
                    'url': self.file_url,
                    'time': current_time,
                    '#':'----------------------------------------------'
                }
                
                
                self.save_message_to_yaml(message, message_yml)
                logger.info(f'file uploaded {ref}')
                
            
            except Exception as e:
                    logger.error(f" {fileName} Error uploading file: {e}")
                    print(f"Error uploading file: {e}")
        else:
                    logger.info('document.yaml file not created: create a document.yaml in catalog')
                     











    def get_file(self,file_url,local_folder='dossier'):
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
            logger.info(f" {file_name} downloaded successfully.")
            print(f"File '{file_name}' downloaded successfully.")

        except Exception as e:
            logger.error(f" {file_name} Error downloading this file: {e}")
            print(f"Error downloading file: {e}")
            