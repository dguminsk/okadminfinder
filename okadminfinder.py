#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    # Change main dir to this (need for Pentest Box)
    import os
    os.chdir(os.path.dirname(__file__))

    from Classes import (Credits,
                         OKadminFinderClass,
                         MessengerClass)

    # Get Messenger class to print information
    messenger = MessengerClass.Messenger()

except():
    exit('\n\t[!] Session Cancelled; Something wrong with import modules')

try:
    # Get credits and print it
    messenger.writeMessage(Credits.getCredits(), 'green')

    # Get main class object
    OKadminFinder = OKadminFinderClass.OKadminFinder()

    # Additional params
    if not messenger.writeRawInputWithYesNo('Do you want use default params?'):
        timeout = messenger.writeInput('Change timeout. Please write value in seconds: ')
        OKadminFinder.timeout = timeout

    # Get site
    site = messenger.writeRawInput('Enter Site Name \n(example : example.com or www.example.com ')

    # Verify target url
    if OKadminFinder.checkUrl(site):
        messenger.writeMessage('\nSite %s is stable\n' % site,'green')
    else:
        messenger.writeMessage('Something wrong with url', 'red')
        exit(SystemExit)

    # Get links for checking
    urls = OKadminFinder.getUrls()

    # Counters for total links, and admin panel find
    totalCount = len(urls)
    adminCount = 0

    # Checking all links
    for url in urls:

        # Create test link with getting params from input and links.txt file
        reqLink = OKadminFinder.createReqLink(site, url)
        messenger.writeMessage('\t [#] Checking http://' + reqLink, 'yellow')

        # Test created link for HTTPerrors. If not error - potential admin panel
        if OKadminFinder.checkUrl(reqLink):
            adminCount += 1
            messenger.writeMessage('%s %s' % ('\n\n>>> http://' + reqLink, 'Admin page found!'), 'green')

            # Stopped process? and waiting for input for continue
            messenger.writeRawInput('Press enter to continue scanning.\n')

        # If HTTPerrors continue testing other links
        else:
            continue

    # Write last information about scanning with counters
    messenger.writeMessage('\n\nCompleted \n', 'green')
    messenger.writeMessage(str(adminCount) + ' Admin pages found', 'white')
    messenger.writeMessage(str(totalCount) + ' total pages scanned', 'white')
    messenger.writeRawInput('[/] Scanning over; Press Enter to Exit', 'green')

    # This magic for Pentest Box. This is return normal color style of console
    messenger.writeMessage('','white')

except (KeyboardInterrupt, SystemExit):
    messenger.writeMessage('\n\t[!] Session Cancelled', 'red')

    # This magic for Pentest Box. This is return normal color style of console
    messenger.writeMessage('','white')

except():
    messenger.writeMessage('\n\t[!] Session Cancelled; Unknown error', 'red')

    # This magic for Pentest Box. This is return normal color style of console
    messenger.writeMessage('','white')

