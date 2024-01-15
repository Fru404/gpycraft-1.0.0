gpycraft.googleSheet package
============================

The `gsheetsdb` module in the `gpycraft` package provides a convenient interface for interacting with Google Sheets as a database. It offers methods to read data from Google Sheets, convert it to a Pandas DataFrame, JSON, and save it as an Excel file.

Initialization
--------------

To use the `gsheetsdb` module, create an instance of the `gsheetsdb` class by providing the necessary parameters during initialization:

```python
from gpycraft.gsheetsdb import gsheetsdb

# Specify the path to the Google Sheets service account credentials JSON file
credentials_path = 'path/to/credentials.json'

# Specify the URL of the Google Sheets document
sheet_url = ''

# Create an instance of gsheetsdb
db = gsheetsdb(credentials_path, sheet_url)
Submodules
----------

gpycraft.googleSheet.gsheetsdb module
-------------------------------------

.. automodule:: gpycraft.googleSheet.gsheetsdb
   :members:
   :undoc-members:
   :show-inheritance:

Module contents
---------------

.. automodule:: gpycraft.googleSheet
   :members:
   :undoc-members:
   :show-inheritance:
