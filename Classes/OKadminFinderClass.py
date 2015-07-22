#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from colorama import Fore

class OKadminFinder():
    """
    Main class for work OKadminFinder
    """

    # Create headers information to requests
    header = {'user-agent': 'OKadminFinder/1.1.1'}

    def getSite(self):
        """
        Function for getting target site and checking for valid url
        :return: site without http://
        """

        # Getting site from input
        site = raw_input(Fore.WHITE + 'Enter Site Name \n(ex : example.com, www.example.com, '
                         'http://example.com or http://www.example.com ): ')
        try:
            # Strip http://
            site = site.replace('http://', '')

            # Get connection to target and raise exception if have errors
            req = requests.get('http://' + site, headers=self.header)
            req.raise_for_status()

        except requests.RequestException as e:
            print Fore.RED + 'Something wrong with url'
            exit()

        print Fore.GREEN + '\nSite %s is stable\n' % site
        return site

    def checkingLinks(self, site):
        """
        Checking requests from potential admin panel urls
        :param site: target url (without http://)
        """

        # Variables for counting
        adminFound = 0
        totalScan = 0

        # Open files with urls of admin panel.
        f = open('LinkFile/links.txt', 'r')

        print(Fore.WHITE + '\t [+] Scanning ' + site + '...\n\n')

        # Check all links for url
        while True:

            # Magic kill of endspace symbol (from line in link file)
            sub_link = f.readline().replace('\n', '')

            if not sub_link:
                break

            # Checking for domain or subdomain
            if sub_link[0:3] == '%s/':
                # Create a full target url
                reqLink = 'http://' + sub_link % site

            else:
                # Checking for www. and kill it
                if site[0:4] == 'www.':
                    site = site.replace('www.', '')

                    # Create a full target url for subdomains with www
                    reqLink = 'http://www.' + sub_link % site

                else:
                    # Create a full target url for subdomains without www
                    reqLink = 'http://' + sub_link % site

            print (Fore.YELLOW + '\t [#] Checking ' + reqLink)
            totalScan += 1

            try:
                # Try to get request to target url without errors
                req = requests.get(reqLink, headers=self.header)
                req.raise_for_status()
            except requests.exceptions.RequestException as e:
                continue
            else:
                # If we don't have errors, we think that this admin panel
                adminFound += 1
                print Fore.GREEN + '%s %s' % ('\n\n>>>' + reqLink, 'Admin page found!')

                # Waiting some key, before restart cheking
                raw_input(Fore.WHITE + 'Press enter to continue scanning.\n')

        # Print all information about checking and waiting some key before exit from util
        print(Fore.GREEN + '\n\nCompleted \n')
        print Fore.WHITE + str(adminFound), ' Admin pages found'
        print Fore.WHITE + str(totalScan), ' total pages scanned'

        raw_input(Fore.GREEN + '[/] Scanning over; Press Enter to Exit')