#!/usr/bin/env python
#
# name file : strgen.py
# This file is the main class of StringGenerator program
# 
# Public License

import string
import random
import re


class StringGenerator:

    # For new instance
    def __init__(self):
        self.alpha = string.letters
        self.alphanum = string.letters + string.digits
        self.printable = string.letters + string.digits + string.punctuation

    # function for generate random characters, 
    # only uppercase and lowercase
    def alpha_char(self, length):
        self.length = length

        while True:
            self.strings = ""
            for i in range(self.length):
                self.strings += self.alpha[random.randint(0, len(self.alpha))-1]

            if (re.search("[a-z]", self.strings) and
                re.search("[A-Z]", self.strings)):
                break
            else:
                continue

        return self.strings

    # function for generate random characters
    # uppercase, lowercase, and digits
    def alphanum_char(self, length):
        self.length = length

        while True:
            self.strings = ""
            for i in range(self.length):
                self.strings += self.alphanum[random.randint(0, len(self.alphanum))-1]

            if (re.search("[a-z]", self.strings) and
                re.search("[A-Z]", self.strings) and re.search("\d", self.strings)):
                break   
            else:
                continue

        return self.strings

    # function for generate random characters
    # uppercase, lowercase, digits, and special characters
    def printable_char(self, length):
        self.length = length

        while True:
            self.strings = ""
            for i in range(self.length):
                self.strings += self.printable[random.randint(0, len(self.printable))-1]

            if (re.search("[a-z]", self.strings) and re.search("[A-Z]", self.strings) and
                re.search("\d", self.strings) and re.search("\W", self.strings)):
                break
            else:
                continue

        return self.strings
