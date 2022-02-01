#!/usr/bin/env python

"""
Author: Chris Burgess
Purpose: Initiate Session, Meetings, Calls and other events

"""

import yaml, json
import os
from . import api_calls as api
import functools


def prettyJSON(f):
    "Decorator to be used to take the dictionary out of most api_calls and make easier to read"

    @functools.wraps(f)
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return json.dumps(x, indent=4, sort_keys=True)

    return wrap


class Session:
    def __init__(self, file="variables/config.cfg"):

        #  Load the config file with key detail
        with open(file, "rt") as handle:
            config = yaml.safe_load(handle)
            self.__ip = config["config"]["ip"]
            self.__username = config["config"]["username"]
            if config["config"]["password"]:
                self.__password = config["config"]["password"]
            else:
                self.__password = os.getenv(
                    CMS_PASS
                )  # if password stored in Env Var, capture it.
            self.__auth = (self.__username, self.__password)

    # Decorator to be used to take the dictionary out of most api_calls and make easier to read

    simple_get_methods = {
        "coSpaces": self.coSpaces,
        "coSpace_bulk_params": self.coSpace_bulk_params,
        "coSpace_bulk_sync": self.coSpace_bulk_sync,
        "coSpace_templates": self.coSpace_templates,
        "dial_transforms": self.dial_transforms,
        "call_profiles": self.call_profiles,
        "rest_test": self.rest_test,
    }

    @prettyJSON
    def rest_test(self):
        "Run a test RESTCONF API call designed for an XE device, to test the code"
        return api.restconf_test(self.__ip, self.__auth)

    def ucsm_xml_api_test(self):
        "Run a test API call designed for an UCSM device"
        return api.ucsm_xml_api_test(self.__ip, self.__auth)

    def method_choice(self, method):
        "This allows args.method to choose a method and make a call.  The CMS calls need building as instance methods, like self.rest_test"
        return simple_get_methods.get(method)()

    @prettyJSON
    def coSpaces(self):
        return api.coSpaces(self.__ip, self.__auth)

    @prettyJSON
    def coSpace_bulk_params(self):
        return api.coSpace_bulk_params(self.__ip, self.__auth)

    @prettyJSON
    def coSpace_bulk_sync(self):
        return api.coSpace_bulk_sync(self.__ip, self.__auth)

    @prettyJSON
    def coSpace_templates(self):
        return api.coSpace_templates(self.__ip, self.__auth)

    @prettyJSON
    def dial_transforms(self):
        return api.dial_transforms(self.__ip, self.__auth)

    @prettyJSON
    def call_profiles(self):
        return api.call_profiles(self.__ip, self.__auth)

    # Params is the 'coSpaceID' from earlier Getter Calls


class Meeting(Session):
    def __init__(self, coSpaceID, callLegProfileID=None):
        self.coSpaceID = coSpaceID
        if callLegProfileID:
            self.callLegProfileID = callLegProfileID
        else:
            self.callLegProfileID = None

    def __call__(self, *args, **kwargs):
        return self(*args, **kwargs)

    meeting_get_methods = {
        "coSpaces": self.coSpaces,
        "coSpace_bulk_params": self.coSpace_bulk_params,
        "coSpace_bulk_sync": self.coSpace_bulk_sync,
        "coSpace_templates": self.coSpace_templates,
        "dial_transforms": self.dial_transforms,
        "call_profiles": self.call_profiles,
        "rest_test": self.rest_test,
    }

    def method_choice(self, method):
        "This allows args.method to choose a method and make a call.  The CMS calls need building as instance methods, like self.rest_test"
        return meeting_get_methods.get(method)()

    def coSpaces_detail(self):
        pass

    @prettyJSON
    def coSpaces_entry_detail(self):
        return api.coSpaces_entry_detail(self.__ip, self.__auth, self.coSpaceID)

    @prettyJSON
    def coSpaces_listMembers(self):
        if callLegProfileID:
            call = api.coSpaces_entry_detail(
                self.__ip,
                self.__auth,
                self.coSpaceID,
                callLegProfileID=self.callLegProfileID,
            )
        else:
            call = api.coSpaces_entry_detail(self.__ip, self.__auth, self.coSpaceID)
        return call

    @prettyJSON
    def coSpaces_listMembers(self):
        if callLegProfileID:
            call = api.coSpaces_entry_detail(
                self.__ip,
                self.__auth,
                self.coSpaceID,
                self.userID,
                callLegProfileID=self.callLegProfileID,
            )
        else:
            call = api.coSpaces_entry_detail(
                self.__ip, self.__auth, self.userID, self.coSpaceID
            )
        return call
