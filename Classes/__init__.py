#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '1.1.1'
__author__ = 'o.koleda'

# Print credits
from colorama import Fore, Back
print Back.BLACK + Fore.GREEN + '''
   ____  __ __          __          _       _______           __
  / __ \/ //_/___ _____/ /___ ___  (_)___  / ____(_)___  ____/ /__  _____
 / / / / ,< / __ `/ __  / __ `__ \/ / __ \/ /_  / / __ \/ __  / _ \/ ___/
/ /_/ / /| / /_/ / /_/ / / / / / / / / / / __/ / / / / / /_/ /  __/ /
\____/_/ |_\__,_/\__,_/_/ /_/ /_/_/_/ /_/_/   /_/_/ /_/\__,_/\___/_/ version %s
                                       easy way to find admin panel
                                           special for Pentest Box
                                                         %s
''' % (__version__, __author__)