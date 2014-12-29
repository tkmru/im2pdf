=======
im2pdf
=======

| This is command line tool that convert images to pdf and unite them.
| Supported file: jpeg, png, gif

Installation
============

----
PyPI
----
The recommended process is to install the PyPI package, as it allows easily staying update.

::

    $ pip install im2pdf

------
github
------
| Download from https://github.com/tkmru/im2pdf/.
| Let's push star!!

::

    $ git clone https://github.com/tkmru/im2pdf/
    $ cd im2pdf
    $ python setup.py install

Usage
=====

| The following options are available:
| -i input file name
| -o output file name(default: output.pdf)

| convert single image file to PDF

::

    $ im2pdf -i test.jpg
    completed.
    test.jpg --> output.pdf

    $ im2pdf -i test.jpg -o test.pdf
    completed.
    test.jpg --> test.pdf

| convert some file to single PDF.
| It support some pdf, too.


| ex) test1.jpg, test2.jpg, test3.jpg to output.pdf

::

    $ im2pdf.py -i test*.jpg
    completed.
    Union of some file is output.pdf

| ex) test1.jpg, test2.jpg, test3.jpg to test.pdf

::

    $ im2pdf.py -i test*.jpg -o test.pdf
    completed.
    Union of some file is test.pdf


License
=======

MIT License

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright (c) @tkmru 