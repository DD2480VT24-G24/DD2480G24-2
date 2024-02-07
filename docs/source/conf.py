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

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
