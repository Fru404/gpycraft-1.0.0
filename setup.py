# setup.py

from setuptools import setup,find_packages

setup(
    name='googlepycraft',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'firebase-admin',
        'gspread',
        'oauth2client',
        'pandas',
        'PyYAML',
    ],
    description='A Python package for manipulating google sheets directly on any coding platform and perform CRUD process easily. Sheets can be stored and retrieved in firebase storage'
)