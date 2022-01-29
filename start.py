#!/usr/bin/env python

"""
Author: Chris Burgess
Purpose: Initiate session an import key variables.
"""

import argparse
from xmlrpc.client import Boolean
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
    cms_parser.add_argument('--data', metavar='path', type=str,
                    help='relative address for the config data file to be passed to method')
    cms_parser.add_argument('--interactive', type=bool,
                    help='to interactively access the methods')

    
    # Execute the parse_args method()
    args = cms_parser.parse_args()

    if args.config:
        connection = init.Session(args.config)
    else:
        connection = init.Session()

    print(connection.rest_test())

if __name__ == "__main__":
    main()