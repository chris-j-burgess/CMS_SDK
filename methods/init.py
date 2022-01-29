#!/usr/bin/env python

"""
Author: Chris Burgess
Purpose: Initiate Session, Meetings, Calls and other events

"""

from mimetypes import init
from urllib.parse import urljoin
import yaml, json
import os
import methods.api_calls as api


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

    def prettyJSON(text):
        output = json.loads(text)   
        return json.dumps(output, indent=4, sort_keys=True)

    def rest_test(self):
        return api.restconf_test(self.ip, self.auth)

    def ucsm_xml_api_test(self):  
        return api.ucsm_xml_api_test(self.ip, self.auth)

    def method_choice(self, method):
        return {
        'coSpaces': api.coSpaces,
        'coSpaces_detail': api.coSpaces_detail,
        'coSpaces_entry_detail': api.coSpaces_entry_detail,
        'coSpaces_listMembers': api.coSpaces_listMembers,
        'rest_test': self.rest_test,
        }.get(method)()

