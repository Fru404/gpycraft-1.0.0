
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

   pip install gpycraft

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
