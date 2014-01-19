#!/usr/bin/env python
#
# This file is part of StringGenerator program
# 
# Public License

import strgen
import argparse

try:
    parser = argparse.ArgumentParser(description="""This program is used to generate random characters, 
                                                    and the results of the random characters are usually used for passwords. 
                                                    Another function of this program can also to avoid dictionary attacks.
                                                    Minimum strings length is 6 characters""")

    parser.add_argument('-a', dest='length_alpha', type=int, metavar="length-characters", help='Generate random characters only lowercase and uppercase (alpha)')
    parser.add_argument('-n', dest='length_alphanum', type=int, metavar="length-characters", help='Generate random characters lowercase, uppercase, and digits (alphanumeric)')
    parser.add_argument('-p', dest='length_printable', type=int, metavar="length-characters", help='Generate random characters printable (with special characters)')
    parser.add_argument('-v', '--version', action='version', version='StringGenerator v1.0')

    args = parser.parse_args()
    generator = strgen.StringGenerator()

    if (args.length_alpha or args.length_alphanum or args.length_printable) > 5: 
        if args.length_alpha:
            print(generator.alpha_char(abs(args.length_alpha)))

        elif args.length_alphanum:
            print(generator.alphanum_char(abs(args.length_alphanum)))

        elif args.length_printable:
            print(generator.printable_char(abs(args.length_printable)))

        else:
            parser.parse_args(['-h'])
    else:
        parser.parse_args(['-h'])

except Exception, e:
    print 'Error : ', e
