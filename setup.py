# setup.py

from setuptools import setup,find_packages

with open('README.md', 'r') as f:
    description = f.read()

setup(
    name='gpycraft',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'firebase-admin',
        'gspread',
        'oauth2client',
        'pandas',
        'PyYAML',
        'tqdm',
        'xlsxwriter',
        'openpyxl',
    ],
    description='A Python package for manipulating google sheets directly on any coding platform and perform CRUD process easily. Sheets can be stored and retrieved in firebase storage',
    entry_points={
        'console_scripts': [
            'begin = gpycraft.app_config:Admin.begin'
        ],
    },
    long_description=description,
    long_description_content_type='text/markdown',
)