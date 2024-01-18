.. image:: https://raw.githubusercontent.com/Fru404/Web/main/1497441839.svg
   :align: right
   :width: 150
   :height: 200

Introduction
------------
.. container:: justified
   `gpycraft` is a versatile Python package designed to simplify common tasks related to Firebase and Google Sheets integration. Whether you need to upload files to Firebase Storage, interact with Firestore, or manage data in Google Sheets as a database, `gpycraft` provides intuitive modules to streamline these operations.

   Key Features:
   - **Firestore Upload Module:** Simplifies uploading files to Firebase Storage with convenient methods and error handling.
   - **Google Sheets Database Module:** Enables seamless communication with Google Sheets, allowing users to read and manipulate data effortlessly.

   Get started with `gpycraft` and make your Firebase and Google Sheets integrations a breeze!

Installation
------------
To install `gpycraft`, you can use `pip`. Open your terminal and run:

.. code-block:: bash

   >>  pip install gpycraft

On terminal run the command `begin` to create files(app_config.yaml and workfile.py) for a smooth start:


.. code-block:: bash

   >> begin

Or just create file manually then copy and paste content to the files.

In `app_config.yaml`, you can include more than one googlesheet.
.. code-block:: bash

      credentials_path: credentials.json
      storage_bucket: 
      sheets:
      - sheet_number: 
         sheet_name: 
         sheet_url: 
The `workfile.py` already contains all neccessary module importation and initialization, all is left is to start working.
.. code-block:: bash

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
Usage
-----

1. **Firestore Upload Module**

   .. automodule:: gpycraft.firestoreupload
      :members:
      :undoc-members:
      :show-inheritance:

   .. autoclass:: gpycraft.firestoreupload.firestoreupload
      :members:
      :undoc-members:

2. **Google Sheets Database Module**

   .. automodule:: gpycraft.gsheetsdb
      :members:
      :undoc-members:
      :show-inheritance:

   .. autoclass:: gpycraft.gsheetsdb.gsheetsdb
      :members:
      :undoc-members:

Example
-------
.. code-block:: console

   # Create an instance of FirestoreUpload
   uploader = firestoreupload.firestoreupload(credentials_path='path/to/credentials.json', storage_bucket='your_storage_bucket')

   # Upload a file
   uploader.upload_file(local_file_path='path/to/local/file.txt')

   from gpycraft import gsheetsdb

   # Create an instance of GSheetsDB
   db = gsheetsdb.gsheetsdb(credentials_path='path/to/credentials.json', sheet_url='your_sheet_url', sheet_number='your_sheet_number')

   # Read data from Google Sheets
   data = db.read_sheet(key='your_key', number_of_rows=5)

Basic Features
--------------



.. toctree::
   :maxdepth: 1

   googlesheet
   firebase
