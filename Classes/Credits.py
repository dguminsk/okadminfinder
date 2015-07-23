#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '1.4.0'
__author__ = 'o.koleda'
__license__ = 'Apache 2.0'

def getCredits():

    return '''
       ____  __ __          __          _       _______           __
      / __ \/ //_/___ _____/ /___ ___  (_)___  / ____(_)___  ____/ /__  _____
     / / / / ,< / __ `/ __  / __ `__ \/ / __ \/ /_  / / __ \/ __  / _ \/ ___/
    / /_/ / /| / /_/ / /_/ / / / / / / / / / / __/ / / / / / /_/ /  __/ / version %s
    \____/_/ |_\__,_/\__,_/_/ /_/ /_/_/_/ /_/_/   /_/_/ /_/\__,_/\___/_/ license %s
                                               special for Pentest Box
                                                             %s
    ''' % (__version__, __license__, __author__,)