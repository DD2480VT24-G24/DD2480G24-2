# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Continuous Integration - Group 24'
copyright = '2024, Andreas Hammarstrand (aeha@kth.se), Martin Lindefors (lindefor@kth.se), Victor Österman (vios@kht.se), Adam Sjöberg (adamsjo@kth.se), Casper Kristiansson (casperkr@kth.se)'
author = 'Andreas Hammarstrand (aeha@kth.se), Martin Lindefors (lindefor@kth.se), Victor Österman (vios@kht.se), Adam Sjöberg (adamsjo@kth.se), Casper Kristiansson (casperkr@kth.se)'
release = '[1.0]'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_rtd_theme',
    'rst2pdf.pdfbuilder'
]

templates_path = ['_templates']
exclude_patterns = []

pdf_documents = [('index', u'rst2pdf', u'Software Engineering Fundamentals Group 24', u'Andreas Hammarstrand (aeha@kth.se), Martin Lindefors (lindefor@kth.se), Victor Österman (vios@kht.se), Adam Sjöberg (adamsjo@kth.se), Casper Kristiansson (casperkr@kth.se)')]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

# -- Path setup --------------------------------------------------------------
import os
import sys

sys.path.insert(0, os.path.abspath('../../src'))
