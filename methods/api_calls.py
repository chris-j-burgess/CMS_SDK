#!/usr/bin/env python

"""
Author: Chris Burgess
Purpose: Make API calls 

"""

import requests
import xmltodict
import functools

# Test Getters to be deleted
def xml_Decorator(f):
    "A Decorator to ensure that the XML output is converted to Python Dict for management elsewhere"

    @functools.wraps(f)
    def wrap(*args, **kwargs):
        text = f(*args, **kwargs)
        return xmltodict.parse(text)

    return wrap


def __getarequest__(uri, auth, params=None):
    "A wrapper for all GET Requests"
    headers = {
        "Accept": "application/yang-data+json, application/yang-data.errors+json"
    }
    return requests.get(uri, auth=auth, headers=headers, params=params)


def restconf_test(ip, auth):
    url = "https://" + ip + "/restconf/data/openconfig-interfaces:interfaces"
    call = __getarequest__(url, auth)
    return call.json()


@xml_Decorator
def ucsm_xml_api_test(ip, auth):
    pass


# Getter API calls for Cisco Meeting Server


def __getrequest__(uri, auth, params=None):
    return requests.get(uri, auth=auth, params=params)


def coSpaces(ip, auth):
    url = "https://" + ip + "/api/v1/coSpaces"
    call = __getrequest__(url, auth)
    return call.text()


# Params is the 'coSpaceID' from earlier Getter Calls


def coSpaces_detail(ip, auth, coSpaceID):
    url = "https://" + ip + "/api/v1/coSpaces/" + coSpaceID
    call = __getrequest__(url, auth)
    return call.text()


def coSpaces_entry_detail(ip, auth, coSpaceID):
    url = "https://" + ip + "/api/v1/coSpaces/" + coSpaceID + "/meetingEntryDetail"
    call = __getrequest__(url, auth)
    return call.text()


def coSpaces_listMembers(ip, auth, coSpaceID, callLegProfileID=None):
    url = "https://" + ip + "/api/v1/coSpaces/" + coSpaceID + "/coSpaceUsers"
    if callLegProfileID:
        call = __getrequest__(url, auth, params=callLegProfileID)
    else:
        call = __getrequest__(url, auth)
    return call.text()


def coSpaces_listMembers(ip, auth, coSpaceID, userID, callLegProfileID=None):
    url = "https://" + ip + "/api/v1/coSpaces/" + coSpaceID + "/coSpaceUsers/" + userID
    if callLegProfileID:
        call = __getrequest__(url, auth, params=callLegProfileID)
    else:
        call = __getrequest__(url, auth)
    return call.text()
