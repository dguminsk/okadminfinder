#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.chdir(os.path.dirname(__file__))

from Classes import OKadminFinderClass

try:
    from colorama import Fore, Back, Style
    OKadminFinder = OKadminFinderClass.OKadminFinder()
    OKadminFinder.credits()
    site = OKadminFinder.getSite()
    OKadminFinder.parsingLinks(site)
    print Fore.WHITE
except (KeyboardInterrupt, SystemExit):
    print Fore.RED + '\n\t[!] Session cancelled'
    print Fore.WHITE
except:
    print Fore.RED + '\n\t[!] Session Cancelled; Unknown error'
    print Fore.WHITE

