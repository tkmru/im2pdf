#!/usr/bin/env python
# coding: UTF-8

__description__ = 'Tool to convert images to pdf and unite them.'
__author__ = '@tkmru'
__version__ = '0.1'
__date__ = '2014/12/29'
__minimum_python_version__ = (2, 7, 6)
__maximum_python_version__ = (3, 4, 2)
__copyright__ = 'Copyright (c) @tkmru'
__license__ = 'MIT License'

import PIL
import PIL.Image
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import argparse

verbose = False


def convert(input_file, output_file):
    im = PIL.Image.open(input_file)
    im.save(output_file, 'PDF', resoultion = 100.0)
    if verbose:
        print('completed.')
        print(input_file + ' --> ' + output_file)


def union(input_files, output_file):
    output = PdfFileWriter()
    part_files_handles = [] # [fh, created=True/False]

    for input_file in input_files:
        if input_file.endswith('.pdf'):
            fh = open(input_file, 'rb')
            part_files_handles.append([fh, False])
            input = PdfFileReader(fh)
            num_pages = input.getNumPages()

            for i in range(0, num_pages):
                output.addPage(input.getPage(i))

        else: # input_file isn't pdf ex. jpeg, png
            im = PIL.Image.open(input_file)
            input_file_pdf = input_file.split('.')[0]+'.pdf'
            im.save(input_file_pdf, 'PDF', resoultion = 100.0)

            fh = open(input_file_pdf, 'rb')
            part_files_handles.append([fh, True])
            input = PdfFileReader(fh)
            num_pages = input.getNumPages()

            for i in range(0, num_pages):
                output.addPage(input.getPage(i))

    with open(output_file, 'wb') as outputStream:
        output.write(outputStream)

    for f in part_files_handles:
        part_path = f[0].name
        f[0].close() # Close each file.
        if f[1]:
            os.remove(part_path) # If 'created' flag is True, remove file a it was created in this process.

    if verbose:
        print('completed.')
        print('Union of some file is ' + output_file)


if __name__ == '__main__':
    verbose = True
    parser = argparse.ArgumentParser(description='convert image to pdf and union them.')
    parser.add_argument('-o', '--output', default='output.pdf')
    parser.add_argument('-i', '--input', nargs='*', required=True)
    parser.add_argument('-v', '--version', action='version', version=__version__)

    args = vars(parser.parse_args())

    if len(args['input']) == 1:
        convert(args['input'][0], args['output'])

    elif len(args['input']) > 1:
        union(args['input'], args['output'])

    else:
        pass
