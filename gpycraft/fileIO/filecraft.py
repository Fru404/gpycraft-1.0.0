import pandas as pd
from io import StringIO
import os
import json

from gpycraft.fileIO.dotstacks import dotstacks
from gpycraft.fileIO.radix import radix

class filecraft:
    def __init__(self) -> None:
        pass

    def dotfile_aspd(self,filePath):
        self.filePath=filePath
        dot_stacks=dotstacks()

        with open(filePath, 'r') as file:
           data_string = file.read()
        dataFile = StringIO(data_string).getvalue()

        dot_stacks.process_text(dataFile)
        
        # Convert the data_list to a single string with newline characters
        data_str = '\n'.join(dot_stacks.display_stacks())

        # Read the fixed-width data using pandas.read_fwf
        df = pd.read_fwf(StringIO(data_str), header=0)

        # Replace empty strings with NaN
        df.replace('', pd.NA, inplace=True)

        # Display the DataFrame
        return df
    
    def pd_asdotfile(self, df, filePath='',spacing=10):
        """
        Convert a dataframe to dotfile
        """
        if not filePath:
            filePath = 'default_dotfile.txt'  # Provide a default file name or modify as needed

        # Convert the DataFrame to a dotfile format
        dotfile_content = ''

        # Add column names as the first line with increased spacing
        dotfile_content += ' '.join([f'{column:<{spacing}}' for column in df.columns])+".\n"

        # Add rows with data
        for _, row in df.iterrows():
            # Increase spacing between each column value
            dotfile_content += ' '.join([f'{str(value):<{spacing}}' for value in row])+".\n"

        # Write the dotfile content to the specified file path
        with open(filePath, 'w') as file:
            file.write(dotfile_content)


    #converting xl to a dotfile
    def xl_asdotfile(self, xl_filePath='', column=None, engine='openpyxl', spacing=10):
        self.xl_filePath = xl_filePath  # path to excel file
        separation = radix()

        """
        This method converts sheet to dotfile format
        1. convert sheet to DataFrame
        2. convert DataFrame to dotfile
        """

        data = pd.read_excel(xl_filePath, engine=engine)  # 1
        number_of_columns = data.shape[1]
        columns = data.columns.to_list()
        number_of_rows = data.shape[0]

        xl_name = os.path.basename(xl_filePath)

        metafile = os.path.splitext(xl_name)[0] + ".json"
        FILEMETADATA = {
            'name of file': xl_name,
            'number of columns': number_of_columns,
            'columns': columns,
            'number of rows': number_of_rows,
            'spacing': spacing,
        }

        print(f'File: {xl_name}______FILEMETADATA: {FILEMETADATA}\n')
        directory = '_METADATA'
        os.makedirs(directory, exist_ok=True)

        # Create and append JSON data to file
        file_metadata_path = os.path.join(directory, metafile)
        with open(file_metadata_path, 'a') as file:
            # Move the cursor to the end of the file before appending
            file.seek(0, os.SEEK_END)
            if file.tell() == 0:
                # If the file is empty, add an opening bracket
                file.write('[')
            else:
                # If not the first entry, add a comma and newline before appending
                file.write(',\n')
            json.dump(FILEMETADATA, file, indent=4)

        convert = separation.to_comma(data, column=column)

        dotfile_path = os.path.splitext(xl_name)[0] + ".txt"
        as_dotfile = self.pd_asdotfile(convert, filePath=dotfile_path, spacing=spacing)

        # print(f'File: {dotfile_path} created')
        return as_dotfile
    
    def dotfile_asxl(self, dotfile_name, sheet_name='Sheet1', engine='xlsxwriter',columnAdd=[],fieldNumber=None, byPass=False):
        """
        Method to convert the dotfile to Excel
        1. Convert the dotfile to DataFrame
        2. Convert the DataFrame to Excel 
        """
        try:
            dotfile_df = self.dotfile_aspd(dotfile_name)
            print(f'{dotfile_df} \n')
            
            if fieldNumber is None:
                warning = {
                    'message': 'Specify the number of columns',
                    'do': 'Look at File metadata for the number of columns(fieldNumber)',
                }
                print(f'Error: {warning}')
        
            else:
                if dotfile_df.shape[1] == fieldNumber and byPass is not False:
                    # Extract the file name without extension
                    excel_file_name = os.path.splitext(dotfile_name)[0]
                    excel_file_name = f'{excel_file_name}.xlsx'  # Provide a default file name or modify as needed
                    dotfile_df.to_excel(excel_file_name, index=False, header=True, sheet_name=sheet_name, engine=engine)
                    print(f'File {excel_file_name} created ')
                    print('\033[93m'+'NOTE: If byPass is True, .xlsx file will be created without checking if column added was found')
                else:
                    
                    if dotfile_df.shape[1] > fieldNumber and columnAdd==[]:
                        print(f'SpacingError: Number of columns in dotfile {dotfile_df.shape[1]} does not match {fieldNumber} ')
                        
                    else:
                        
                        for col in columnAdd:
                            if col in dotfile_df.columns and columnAdd!=[]:
                                
                                continue
                            else:
                                
                                print('FieldError: Column(s) not found in dotfile ')
                        if dotfile_df.shape[1] < fieldNumber and byPass is not True:
                            print('\033[91m'+'WARNING: byPass needs to be True if fields were removed or added to validate process')
                                
                        elif byPass is False:
                            print('\033[91m'+'WARNING: byPass needs to be True to validate process')
                        else:
                            print(f'SpacingError: Number of columns in dotfile {dotfile_df.shape[1]} does not match {fieldNumber}')
                            
                    

        except Exception as e:
            print(f"Error: {e} :")
            return None