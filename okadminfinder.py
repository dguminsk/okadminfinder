#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Change main dir to this (need for Pentest Box)
import os
os.chdir(os.path.dirname(__file__))

from Classes import OKadminFinderClass

try:
    from colorama import Fore

    # Get main class object
    OKadminFinder = OKadminFinderClass.OKadminFinder()

    # Get site and verify it
    site = OKadminFinder.getSite()

    # Start finding admin panel
    OKadminFinder.checkingLinks(site)

    # This magic for Pentest Box. This is return normal color style of console
    print Fore.WHITE

except (KeyboardInterrupt, SystemExit):
    print Fore.RED + '\n\t[!] Session cancelled'

    # This magic for Pentest Box. This is return normal color style of console
    print Fore.WHITE

except:
    print Fore.RED + '\n\t[!] Session Cancelled; Unknown error'

    # This magic for Pentest Box. This is return normal color style of console
    print Fore.WHITE

