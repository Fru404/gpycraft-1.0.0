import yaml

class Admin:
    def __init__(self):
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
        if sheet_number_str in self.sheets:
            return self.sheets[sheet_number_str]['sheet_url']
        else:
            raise ValueError(f"Sheet with number {sheet_number_str} not found")