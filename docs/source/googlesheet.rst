.. _google_console_link:


Use Multiple Google Sheets Simultaneously
-----------------------------------------

To use multiple Google Sheets APIs simultaneously, follow these steps:

Enable Google Sheets API in Google Console
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open to the `google console <https://console.cloud.google.com/>`_  on your browser.On your console click on `Navigation Menu>API and Service>click on '+Enable APIs and Services'`.
2. Search for `google sheet` 
3. Enable the Google sheet API

After Enabling the google sheet API, copy the link of googlesheet, make sure it is shareable.

Generating Credentials
^^^^^^^^^^^^^^^^^^^^^

To generate credentials:

1. On console, API and SERVICES click on credentials. 
2. In Service account section you will see yor default App Engine default service account click on it.
3. In `App Engine default service account` click on keys>ADD keys>Create New keys. A json document will be downloaded. Rename the json file as `Credentials.json`(NOTE: Do not expose this file make sure to include it in .gitignore)

Include the credentials.json in working repository.



