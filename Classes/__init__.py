#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '1.1.0'
__author__ = 'o.koleda'

# Print credits
from colorama import Fore, Back
print Back.BLACK + Fore.GREEN + '''
 _____ _   __          _           _      ______ _           _
|  _  | | / /         | |         (_)     |  ___(_)         | |
| | | | |/ /  __ _  __| |_ __ ___  _ _ __ | |_   _ _ __   __| | ___ _ __
| | | |    \ / _` |/ _` | '_ ` _ \| | '_ \|  _| | | '_ \ / _` |/ _ \ '__|
\ \_/ / |\  \ (_| | (_| | | | | | | | | | | |   | | | | | (_| |  __/ |
 \___/\_| \_/\__,_|\__,_|_| |_| |_|_|_| |_\_|   |_|_| |_|\__,_|\___|_| version %s
                                          easy way to find admin panel
                                               special for Pentest Box
                                                              %s
''' % (__version__, __author__)