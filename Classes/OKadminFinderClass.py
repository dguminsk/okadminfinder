#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from colorama import Fore, Back

class OKadminFinder():

    header = {'user-agent': 'OKadminFinder/1.0'}

    def credits(self):

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
        site = raw_input(Fore.WHITE + 'Enter Site Name \n(ex : example.com, www.example.com, '
                         'http://example.com or http://www.example.com ): ')
        try:
            site = site.replace('http://', '')
            req = requests.get('http://' + site, headers=self.header)
            req.raise_for_status()
        except requests.exceptions.RequestException as e:
            print Fore.RED + 'Something wrong with url'
            exit()
        print Fore.GREEN + '\nSite %s is stable\n' % site
        return site

    def parsingLinks(self, site):

        adminFound = 0
        totalScan = 0

        f = open('LinkFiles/links.txt', 'r')
        fSub = open('LinkFiles/link_subdomain.txt', 'r')
        print(Fore.WHITE + '\t [+] Scanning ' + site + '...\n\n')

        # check domain
        while True:
            sub_link = f.readline().replace('\n', '')
            if not sub_link:
                break
            reqLink = 'http://' + site + '/' + sub_link
            print (Fore.YELLOW + '\t [#] Checking ' + reqLink)
            totalScan += 1
            try:
                req = requests.get(reqLink, headers=self.header)
                req.raise_for_status()
            except requests.exceptions.RequestException as e:
                continue
            else:
                adminFound += 1
                print Fore.GREEN + '%s %s' % ('\n\n>>>' + reqLink, 'Admin page found!')
                raw_input(Fore.WHITE + 'Press enter to continue scanning.\n')

        # check subdomain
        while True:
            sub_link = fSub.readline().replace('\n', '')
            if not sub_link:
                break
            site = site.replace('www.', '')
            reqLink = 'http://' + sub_link + '.' + site
            print (Fore.YELLOW + '\t [#] Checking ' + reqLink)
            totalScan += 1
            try:
                req = requests.get(reqLink, headers=self.header)
                req.raise_for_status()
            except requests.exceptions.RequestException as e:
                continue
            else:
                adminFound += 1
                print Fore.GREEN + '%s %s' % ('\n\n>>>' + reqLink, 'Admin page found!')
                raw_input(Fore.WHITE + 'Press enter to continue scanning.\n')

        print(Fore.GREEN + '\n\nCompleted \n')
        print Fore.WHITE + str(adminFound), ' Admin pages found'
        print Fore.WHITE + str(totalScan), ' total pages scanned'
        raw_input(Fore.GREEN + '[/] Scanning over; Press Enter to Exit')