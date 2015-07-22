#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Messenger():
    """
    Class for printing colored messages
    """

    def __init__(self):
        from colorama import Fore
        # Creating styling for simple use
        self.style = {'white': Fore.WHITE, 'red': Fore.RED, 'green': Fore.GREEN, 'yellow': Fore.YELLOW}


    def writeMessage(self, message, color='white'):
        """
        Write message to console with color. Colors - white, red, green, yellow
        :param message: string
        :param color: string
        :return:
        """

        print self.style[color] + message


    def writeInput(self, message, color='white'):
        """
        Create raw_input with color text. Colors - white, red, green, yellow
        :param message: string
        :param color: string
        :return: raw_input
        """

        return raw_input(self.style[color] + message)
