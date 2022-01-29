#!/usr/bin/env python

"""
Author: Chris Burgess
Purpose: Initiate session an import key variables.
"""

import argparse
import methods.init as init
import sys

def main():

    # Start ArgParse section to ingest CLI commands
    # Create the parser
    cms_parser = argparse.ArgumentParser(prog='CMS SDK', description='Interact with CMS from the Command Line',
                    epilog='For more help see the README.md file')

    # Add the arguments
    cms_parser.add_argument('--config', metavar='path', type=str,
                    help='relative address for config file.  Default=variables/config.cfg')
    cms_parser.add_argument('--method', 
                    help='call a particular method - options include: ')

    # Execute the parse_args method()
    args = cms_parser.parse_args()

    if args.config:
        connection = init.Session(args.config)
    else:
        connection = init.Session()

    print(connection.restconf_test())

if __name__ == "__main__":
    main()