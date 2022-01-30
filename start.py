#!/usr/bin/env python

"""
Author: Chris Burgess
Purpose: Initiate session an import key variables.
"""

import argparse
import methods.init as init


def main():

    if args.config:
        connection = init.Session(args.config)
    else:
        connection = init.Session()

    if args.interactive:
        print("Let's go interactive")
    else:
        print("Session Mode")

    if args.method:
        print(f"Method is:  {args.method} \n \n")
        try:
            print(connection.method_choice(args.method))
        except TypeError as e:
            print(f"Method {args.method} not recognised as an actual function")
    else:
        print("No Method Selected")

    if args.data:
        print(f"Data file located at:  {args.data}")
    else:
        print("No Data File this time")


#  print(connection.rest_test())

if __name__ == "__main__":

    # Start ArgParse section to ingest CLI commands
    # Create the parser
    cms_parser = argparse.ArgumentParser(
        prog="start.py",
        description="** CMS_SDK:  Interact with CMS from the Command Line **",
        epilog="For more help see the README.md file",
    )

    # Add the arguments
    cms_parser.add_argument(
        "-c",
        "--config",
        metavar="path",
        type=str,
        help="relative address for config file.  Default=variables/config.cfg",
    )
    cms_parser.add_argument(
        "-m", "--method", help="call a particular method - options include: "
    )
    cms_parser.add_argument(
        "-d",
        "--data",
        metavar="path",
        type=str,
        help="relative address for the config data file to be passed to method",
    )
    cms_parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="to interactively access the methods",
    )

    # Execute the parse_args method()
    args = cms_parser.parse_args()

    main()
