OKadminFinder: Easy way to find admin panel of site
===================================================

OKadminFinder is an Apache2 Licensed util, written in Python 2.7.*, for human who want find admin panel of site.
In this time find tool for this work too hard. You can find .exe utils, but it dangerous.

OKadminFinder created for `Pentest Box <https://pentestbox.com/>`_, but it can use as alone util

If you use it without Pentest Box, you should install library `Requests <https://github.com/kennethreitz/requests/>`_ for Python

Used
----
in Python:

.. code-block:: python

    >>> okadminfinder.py
    ...

in Bash:

.. code-block:: bash

    $ python okadminfinder.py
    ...

in Pentest Box (if customaliase are):

.. code-block:: cmd

    C:/PentestBoxDir okadminfinder
    ...

If you wanna use that util in `Pentest Box <https://pentestbox.com/>`_, place this files to directory PentestBox Directory\bin\WebApplications\okadminfinder
After that, you must add custom alias.

#. (If you don't have customaliases file) Create a file with name customaliases and place it in PentestBox Directory/bin. Please note file should not have any extension and make sure encoding is ANSI

#. Write to this file: okadminfinder=python "%pentestbox_ROOT%\bin\WebApplications\okadminfinder\okadminfinder.py" $*


Extensions
----------
If you know potential admin panels, you can addin their to LinkFile/links.txt

All links use %s variable. %s = our site

Example: site = test.com -> %s/admin -> test.com/admin


In Future
---------
#. Config file with network params, like proxy, headers etc.
#. Adding some params like time-outs
#. Multithreading work, for faster work. Adding more potential admin panel pages
#. Console work with params, like: okadminfinder -u --proxy --threads

