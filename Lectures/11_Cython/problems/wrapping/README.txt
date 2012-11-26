Wrapping a C library
====================

Example of wrapping a C library.


Contents
--------

- ``stuff.pyx``: wrapper for the C library (write this yourself!)

- ``run.py``: Sample script using the wrapper for something

- ``setup.py``: Build script

- ``src/*.[ch]``: Some C library


Building & running
------------------

To build:

    python setup.py build_ext -i

To run:

    python run.py
