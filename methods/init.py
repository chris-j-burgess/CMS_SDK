#!/usr/bin/env python

"""
Author: Chris Burgess
Purpose: Initiate session an import key variables.
"""

from urllib.parse import urljoin
import yaml
import os
import requests

class Session():

    def __init__(self, file='variables/config.cfg'):

        with open(file, 'rt') as handle:
            config = yaml.safe_load(handle)
            self.ip = config['config']['ip']           
            self.username = config['config']['username']
            if config['config']['password']:
                self.password = config['config']['password']
            else:
                self.password = os.getenv(CMS_PASS)
            self.auth = (self.username, self.password)

    def __getrequest__(self, uri):
        headers = {'Accept': 'application/yang-data+json, application/yang-data.errors+json'}
        return requests.get(uri, auth=self.auth, headers=headers)


    def restconf_test(self):
        url = "https://"+self.ip+'/restconf/data/openconfig-interfaces:interfaces'
        call = self.__getrequest__( url)
        return call.json()

        