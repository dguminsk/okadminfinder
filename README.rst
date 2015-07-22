OKadminFinder: Easy way to find admin panel of site
=========================
Lite util to find admin panel of website

Created for <a href="https://pentestbox.com/">Pentest Box</a>, but can use as alone util

Based on python 2.7.x

Require library <a href="https://github.com/kennethreitz/requests/">Requests</a>

To use - just run okadminfinder.py


If you wanna use that util in <a href="https://pentestbox.com/">Pentest Box</a>, place this files to directory PentestBox Directory\bin\WebApplications\okadminfinder
After that, you must add custom alias.

1) (If you don't have customaliases file) Create a file with name customaliases and place it in PentestBox Directory/bin. Please note file should not have any extension and make sure encoding is ANSI

2) Write to this file: okadminfinder=python "%pentestbox_ROOT%\bin\WebApplications\okadminfinder\okadminfinder.py" $*


If you know potential admin panels, you can addin their to LinkFile/links.txt

All links use %s variable. %s = our site

Example: site = test.com -> %s/admin -> test.com/admin


TODO:
1) Config file with network params, like proxy, headers etc.

2) Adding some params like time-outs

3) Multithreading work, for faster work. Adding more potential admin panel pages

4) Console work with params, like: okadminfinder -u --proxy --threads