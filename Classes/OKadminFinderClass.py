#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from colorama import Fore, Back

class OKadminFinder():
    """
    Main class for work OKadminFinder
    """

    # Create headers information to requests
    header = {'user-agent': 'OKadminFinder/1.0'}

    def credits(self):
        """
        Credits to util
        """

        print Back.BLACK + Fore.GREEN + '''
 _____ _   __          _           _      ______ _           _
|  _  | | / /         | |         (_)     |  ___(_)         | |
| | | | |/ /  __ _  __| |_ __ ___  _ _ __ | |_   _ _ __   __| | ___ _ __
| | | |    \ / _` |/ _` | '_ ` _ \| | '_ \|  _| | | '_ \ / _` |/ _ \ '__|
\ \_/ / |\  \ (_| | (_| | | | | | | | | | | |   | | | | | (_| |  __/ |
 \___/\_| \_/\__,_|\__,_|_| |_| |_|_|_| |_\_|   |_|_| |_|\__,_|\___|_| version 1.0
                                          easy way to find admin panel
                                               special for Pentest Box
                                                              o.koleda
        '''

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
        except requests.exceptions.RequestException as e:
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

        # Open files with urls of admin panel. fSub - for subdomains
        f = open('LinkFiles/links.txt', 'r')
        fSub = open('LinkFiles/link_subdomain.txt', 'r')

        print(Fore.WHITE + '\t [+] Scanning ' + site + '...\n\n')

        # Check all links for url
        while True:

            # Magic kill of endspace symbol (from line in link file)
            sub_link = f.readline().replace('\n', '')

            if not sub_link:
                break

            # Create a full target url
            reqLink = 'http://' + site + '/' + sub_link
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

        # Check all links for subdomain
        while True:

            # Magic kill of endspace symbol (from line in link file)
            sub_link = fSub.readline().replace('\n', '')

            if not sub_link:
                break

            # Create a full target url
            site = site.replace('www.', '')
            reqLink = 'http://' + sub_link + '.' + site
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