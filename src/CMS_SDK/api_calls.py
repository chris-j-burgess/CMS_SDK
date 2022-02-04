#!/usr/bin/env python

"""
Author: Chris Burgess
Purpose: Make API calls 

"""

import requests
import xmltodict, json
import functools

# Test Getters to be deleted
def xml_Decorator(f):
    "A Decorator to ensure that the XML output is converted to Python Dict for management elsewhere"

    @functools.wraps(f)
    def wrap(*args, **kwargs):
        text = f(*args, **kwargs)
        return xmltodict.parse(text)

    return wrap



def json_Decorator(f):
    "A Decorator to ensure that the XML output is converted to Python Dict for management elsewhere"

    @functools.wraps(f)
    def wrap(*args, **kwargs):
        text = f(*args, **kwargs)
        return json.loads(text)

    return wrap


#  GET Requests - Tests

def __getarequest__(uri, auth, params=None):
    "A test wrapper for GET Requests for Restconf XML requests"
    headers = {"Accept": "application/yang-data+xml, application/yang-data.errors+xml"}
    response = requests.get(uri, auth=auth, headers=headers, params=params)
    return response.content

@xml_Decorator
def restconf_test(ip, auth):
    "This only a test RESTCONF request to show handling for XML"
    url = "https://" + ip + "/restconf/data/openconfig-interfaces:interfaces"
    return __getarequest__(url, auth)


def ucsm_xml_api_test(ip, auth):
    "Needs completing - This only a second test to UCS to show handling for XML"
    pass


# GET Requests API calls for Cisco Meeting Server


def __getrequest__(uri, auth, params=None):
    headers = {"Accept": "application/json"}
    response = requests.get(uri, auth=auth, headers=headers, params=params)
    return response.content


@json_Decorator
def coSpaces(ip, auth):
    url = "https://" + ip + "/api/v1/coSpaces"
    return __getrequest__(url, auth)


# Params is the 'coSpaceID' from earlier Getter Calls


@json_Decorator
def coSpaces_detail(ip, auth, coSpaceID):
    url = "https://" + ip + "/api/v1/coSpaces/" + coSpaceID
    return __getrequest__(url, auth)


@json_Decorator
def coSpaces_entry_detail(ip, auth, coSpaceID):
    url = "https://" + ip + "/api/v1/coSpaces/" + coSpaceID + "/meetingEntryDetail"
    return __getrequest__(url, auth)


@json_Decorator
def coSpaces_listMembers(ip, auth, coSpaceID, callLegProfileID=None):
    url = "https://" + ip + "/api/v1/coSpaces/" + coSpaceID + "/coSpaceUsers"
    if callLegProfileID:
        params = {"callLegProfileID": callLegProfileID}
    else:
        params = None
    call = __getrequest__(url, auth, params=params)
    return call


@json_Decorator
def coSpaces_listMembers(ip, auth, coSpaceID, userID, callLegProfileID=None):
    url = "https://" + ip + "/api/v1/coSpaces/" + coSpaceID + "/coSpaceUsers/" + userID
    if callLegProfileID:
        params = {"callLegProfileID": callLegProfileID}
    else:
        params = None
    call = __getrequest__(url, auth, params=params)
    return call


@json_Decorator
def coSpace_bulk_params(ip, auth):
    url = "https://" + ip + "/api/v1/coSpaceBulkParameterSets"
    return __getrequest__(url, auth)


@json_Decorator
def coSpace_bulk_sync(ip, auth):
    url = "https://" + ip + "/api/v1/coSpaceBulkSyncs"
    return __getrequest__(url, auth)


@json_Decorator
def coSpace_templates(ip, auth):
    url = "https://" + ip + "/api/v1/coSpaceTemplates"
    return __getrequest__(url, auth)


@json_Decorator
def dial_plan_outbound(ip, auth, tenantID=None):
    url = "https://" + ip + "/api/v1/outboundDialPlanRules"
    if tenantID:
        params = {"tenantID": tenantID}
    else:
        params = None
    call = __getrequest__(url, auth, params=params)
    return call


@json_Decorator
def dial_transforms(ip, auth):
    url = "https://" + ip + "/api/v1/dialTransforms"
    return __getrequest__(url, auth)


@json_Decorator
def inbound_rules(ip, auth, tenantID=None):
    url = "https://" + ip + "/api/v1/inboundDialPlanRules"
    if tenantID:
        params = {"tenantID": tenantID}
    else:
        params = None
    call = __getrequest__(url, auth, params=params)
    return call


@json_Decorator
def forwarding_rules(ip, auth, tenantID=None):
    url = "https://" + ip + "/api/v1/forwardingDialPlanRules"
    if tenantID:
        params = {"tenantID": tenantID}
    else:
        params = None
    call = __getrequest__(url, auth, params=params)
    return call


@json_Decorator
def list_calls(ip, auth, coSpaceID=None, tenantID=None):
    url = "https://" + ip + "/api/v1/calls"
    if tenantID and coSpaceID:
        params = {"tenantID": tenantID, "coSpaceID": coSpaceID}
    elif tenantID:
        params = {"tenantID": tenantID}
    elif coSpaceID:
        params = {"coSpaceID": coSpaceID}
    else:
        params = None
    call = __getrequest__(url, auth, params=params)
    return call


@json_Decorator
def call_profiles(ip, auth):
    url = "https://" + ip + "/api/v1/callProfiles"
    return __getrequest__(url, auth)
