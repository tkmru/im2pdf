#!/usr/bin/env python
# coding: UTF-8

from setuptools import setup
import os
import shutil

if not os.path.exists('scripts'):
    os.makedirs('scripts')
shutil.copyfile('im2pdf.py', 'scripts/im2pdf')

with open('README.rst', 'r') as f:
    readme_file = f.read()

setup(
    name = 'im2pdf',
    version = '0.1.1',
    author = '@tkmru',
    author_email = 'i.am.tkmru@gmail.com',
    install_requires = ['Pillow', 'PyPDF2'],
    py_modules = ['im2pdf'],
    scripts=['scripts/im2pdf'],
    url = 'https://github.com/tkmru/im2pdf',
    license = 'MIT License',
    keywords = ['pdf','jpeg'],
    description = 'Tool to convert image to pdf and unite them.',
    long_description = readme_file,
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License'
    ]
)
