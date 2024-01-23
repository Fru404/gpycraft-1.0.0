import yaml
import os
from tqdm import tqdm
from time import sleep
import textwrap

class Admin:
    def __init__(self) -> None:
        with open('app_config.yaml', 'r') as admin_credentials:
            admin_credentials_data = yaml.safe_load(admin_credentials)

            self.credentials_path = admin_credentials_data['credentials_path']
            self.storage_bucket = admin_credentials_data['storage_bucket']

            # Store sheets in a dictionary for easy lookup
            self.sheets = {str(sheet['sheet_number']): sheet for sheet in admin_credentials_data['sheets']}
    
    def sheet_url(self, sheet_number=''):
        # Convert sheet_number to string
        sheet_number_str = str(sheet_number)

        # Check if the sheet number exists
        if sheet_number_str in self.sheets or sheet_number_str=='0':
            return self.sheets[sheet_number_str]['sheet_url']
        else:
            raise ValueError(f"Sheet with number {sheet_number_str} not found")
    
    def begin():
        project_name = input("Enter project name: ")
        os.environ['project_name'] = project_name
        print("\033[32mbegin  :  \033[0m",project_name  )
        # Add a loading animation
        print("\033[32mInitialization...\033[0m")
        print("\033[32mCreating catalog.....\033[0m")
        print("\033[32mCreating dossier...\033[0m")
        print("\033[32mWritting contents...\033[0m")
       
       
        for _ in tqdm(range(10), desc="Progress", unit="file"):
             sleep(0.1)
        print("\033[32mCreating Private key...\033[0m")
        print("\033[32mCreating public key...\033[0m")
        for _ in tqdm(range(10), desc="Progress", unit="file"):
            sleep(0.1)  # Simulating some work

        # Content to be written in workfile.py
        workfile_content = textwrap.dedent("""
            # import package
            from gpycraft.googleSheet.gsheetsdb import gsheetsdb as gb
            from gpycraft.fireStore.firestoreupload import firestoreupload
            from gpycraft.app_config import Admin
            import os

            # Instantiate the Admin class
            admin_instance = Admin()
            os.environ['SHEET_NUMBER'] = '0'
            # Access the variables from the admin instance
            credentials_path = admin_instance.credentials_path
            sheetNumber = os.environ.get('SHEET_NUMBER')
            sheet_url = admin_instance.sheet_url(sheet_number=sheetNumber)
            storage_bucket = admin_instance.storage_bucket

            # begin by instanciating the class
            gsheets_instance = gb(credentials_path, sheet_url, sheet_number=sheetNumber)
            fire_instance = firestoreupload(storage_bucket=storage_bucket, credentials_path=credentials_path)
        """)

        # Content to be written in app_config.yaml
        app_config_content = textwrap.dedent("""
            credentials_path: credentials.json
            storage_bucket: 
            sheets:
             - sheet_number: '0'
                sheet_name: 'None'
                sheet_url: 'None'  
                #Start project from here                        
             - sheet_number: 
                sheet_name: 
                sheet_url: 
        """)
        PATH=['catalog','dossier']
        for path in PATH:
            
            path
            if not os.path.exists(path):
                os.makedirs(path)
            else:
              print(f'{path} already exist....')
            catalog='catalog'
            dossier='dossier'

        
        FILEPATH=[os.path.join(dossier,'publickey.pem'),os.path.join(catalog,'document.yaml')]
        
        
        for filepath in FILEPATH:
           if os.path.exists(filepath):
            print(f'{filepath} already exist ....')
            pass
           else:
                with open(filepath,'w'):
                        pass
            
        if os.path.exists('workfile.py'):
            print('workfile already present.......')
            pass
        else:
        # Write content to workfile.py
            with open('workfile.py', 'w') as file:
                file.write(workfile_content)

        
        if os.path.exists('app_config.yaml'):
         print('app_config already present...')
         pass
        else:
        # Write content to app_config.yaml
            with open('app_config.yaml', 'w') as file:
                file.write(app_config_content)

    