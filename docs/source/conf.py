# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import better
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = 'gpycraft'
copyright = '2024, Fru Ngwa'
author = 'Fru Ngwa'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.todo","sphinx.ext.autodoc","sphinx.ext.viewcode","sphinx.ext.linkcode"]

templates_path = ['_templates']
exclude_patterns = ['_build','Thumbs.db','DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'better'
html_theme_path = [better.better_theme_path]

def linkcode_resolve(domain, info):
    """
    Determine the URL corresponding to Python object references.
    """
    if domain != 'py':
        return None
    if not info['module']:
        return None

    filename = info['module'].replace('.', '/')
    if filename.endswith('index'):
        filename = filename.rsplit('/', 1)[0]

    return f'https://github.com/Fru404/https---github.com-Fru404-googlepycraft-tree-googlepycraft-1.0.0'
