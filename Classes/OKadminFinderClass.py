#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

class OKadminFinder():
    """
    Main class for work OKadminFinder
    """

    def __init__(self):
        # Create headers information to requests
        self.header = {'user-agent': 'OKadminFinder/1.2.1'}


    def checkUrl(self, url):
        """
        Check target url for HTTPerrors. If Error -> False, If Not Errors-> True
        :param url: string
        :return: boolean
        """

        try:
            # Get connection to target and raise exception if have errors
            req = requests.get('http://' + url, headers=self.header)
            req.raise_for_status()
            return True

        except requests.RequestException:
            return False

    @staticmethod
    def getUrls():
        """
        Create array from file with potential admin panels
        :return: array
        """

        # Open files with urls of admin panel.
        f = open('LinkFile/links.txt', 'r')
        links = []

        # Appending to array all lines from file.
        for line in f.readlines():

            # Strip \n symbols
            links.append(line.replace('\n', ''))
        return links

    @staticmethod
    def createReqLink(site, subLink):
        """
        Create full link to potential admin panel site+sublink or subdomen+site
        :param site: string
        :param subLink: string
        :return: string
        """

        # This checking for domain or subdomain target url
        if subLink[0:3] == '%s/':
            # Create a full target url
            reqLink = subLink % site

        else:
            # Checking for www. and kill it
            if site[0:4] == 'www.':
                site = site.replace('www.', '')

                # Create a full target url for subdomains with www
                reqLink = 'www.' + subLink % site

            else:
                # Create a full target url for subdomains without www
                reqLink = subLink % site

        # Replace http:// for next use in function checkUrl
        return reqLink