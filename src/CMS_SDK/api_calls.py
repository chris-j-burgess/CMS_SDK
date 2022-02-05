#!/usr/bin/env python

"""
Author: Chris Burgess
Purpose: Make API calls 

"""

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import xmltodict, json
import functools
import os

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

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


def save_Decorator(f):
    "A Decorator to save a copy of the output of REST API"

    @functools.wraps(f)
    def wrap(*args, **kwargs):
        output_dir ='output'
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)
            print(f"Creating {output_dir} directory .....")
        text = f(*args, **kwargs).decode("utf-8") 
        print(text)
        name = str(f.__name__)
        with open(f"{output_dir}/{name}.xml", "w") as store:
            store.write(text)
        return None

    return wrap
    
#  GET Requests - Tests

def __getarequest__(uri, auth, params=None):
    "A test wrapper for GET Requests for Restconf XML requests"
    headers = {"Accept": "application/yang-data+xml, application/yang-data.errors+xml"}
    response = requests.get(uri, auth=auth, headers=headers, params=params)
    return response.content



def restconf_test(ip, auth):
    "This only a test RESTCONF request to show handling for XML"
    url = "https://" + ip + "/restconf/data/openconfig-interfaces:interfaces"
    return __getarequest__(url, auth)


def ucsm_xml_api_test(ip, auth):
    "Needs completing - This only a second test to UCS to show handling for XML"
    pass


# GET Requests API calls for Cisco Meeting Server


def __getrequest__(uri, auth, params=None):
    headers = {"Accept": "application/xml"}
    
    response = requests.get(uri, auth=auth, headers=headers, params=params, verify=False)
    return response.content


@xml_Decorator
@save_Decorator
def coSpaces(ip, auth):
    url = "https://" + ip + "/api/v1/coSpaces"
    return __getrequest__(url, auth)


# Params is the 'coSpaceID' from earlier Getter Calls


@xml_Decorator
@save_Decorator
def coSpaces_detail(ip, auth, coSpaceID):
    url = "https://" + ip + "/api/v1/coSpaces/" + coSpaceID
    return __getrequest__(url, auth)


@xml_Decorator
@save_Decorator
def coSpaces_entry_detail(ip, auth, coSpaceID):
    url = "https://" + ip + "/api/v1/coSpaces/" + coSpaceID + "/meetingEntryDetail"
    return __getrequest__(url, auth)


@xml_Decorator
@save_Decorator
def coSpaces_listMembers(ip, auth, coSpaceID, callLegProfileID=None):
    url = "https://" + ip + "/api/v1/coSpaces/" + coSpaceID + "/coSpaceUsers"
    if callLegProfileID:
        params = {"callLegProfileID": callLegProfileID}
    else:
        params = None
    call = __getrequest__(url, auth, params=params)
    return call


@xml_Decorator
@save_Decorator
def coSpaces_listMembers(ip, auth, coSpaceID, userID, callLegProfileID=None):
    url = "https://" + ip + "/api/v1/coSpaces/" + coSpaceID + "/coSpaceUsers/" + userID
    if callLegProfileID:
        params = {"callLegProfileID": callLegProfileID}
    else:
        params = None
    call = __getrequest__(url, auth, params=params)
    return call


@xml_Decorator
@save_Decorator
def coSpace_bulk_params(ip, auth):
    url = "https://" + ip + "/api/v1/coSpaceBulkParameterSets"
    return __getrequest__(url, auth)


@xml_Decorator
@save_Decorator
def coSpace_bulk_sync(ip, auth):
    url = "https://" + ip + "/api/v1/coSpaceBulkSyncs"
    return __getrequest__(url, auth)


@xml_Decorator
@save_Decorator
def coSpace_templates(ip, auth):
    url = "https://" + ip + "/api/v1/coSpaceTemplates"
    return __getrequest__(url, auth)


@xml_Decorator
@save_Decorator
def dial_plan_outbound(ip, auth, tenantID=None):
    url = "https://" + ip + "/api/v1/outboundDialPlanRules"
    if tenantID:
        params = {"tenantID": tenantID}
    else:
        params = None
    call = __getrequest__(url, auth, params=params)
    return call


@xml_Decorator
@save_Decorator
def dial_transforms(ip, auth):
    url = "https://" + ip + "/api/v1/dialTransforms"
    return __getrequest__(url, auth)


@xml_Decorator
@save_Decorator
def inbound_rules(ip, auth, tenantID=None):
    url = "https://" + ip + "/api/v1/inboundDialPlanRules"
    if tenantID:
        params = {"tenantID": tenantID}
    else:
        params = None
    call = __getrequest__(url, auth, params=params)
    return call


@xml_Decorator
@save_Decorator
def forwarding_rules(ip, auth, tenantID=None):
    url = "https://" + ip + "/api/v1/forwardingDialPlanRules"
    if tenantID:
        params = {"tenantID": tenantID}
    else:
        params = None
    call = __getrequest__(url, auth, params=params)
    return call


@xml_Decorator
@save_Decorator
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


@xml_Decorator
@save_Decorator
def call_profiles(ip, auth):
    url = "https://" + ip + "/api/v1/callProfiles"
    return __getrequest__(url, auth)



@xml_Decorator
@save_Decorator
def callBrandingProfiles(ip, auth):
    url = "https://" + ip + "/api/v1/callBrandingProfiles"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def callBridgeGroups(ip, auth):
    url = "https://" + ip + "/api/v1/callBridgeGroups"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def callBridges(ip, auth):
    url = "https://" + ip + "/api/v1/callBridges"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def callLegProfiles(ip, auth):
    url = "https://" + ip + "/api/v1/callLegProfiles"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def calls(ip, auth):
    url = "https://" + ip + "/api/v1/calls"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def compatibilityProfiles(ip, auth):
    url = "https://" + ip + "/api/v1/compatibilityProfiles"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def dtmfProfiles(ip, auth):
    url = "https://" + ip + "/api/v1/dtmfProfiles"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def inboundDialPlanRules(ip, auth):
    url = "https://" + ip + "/api/v1/inboundDialPlanRules"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def ivrs(ip, auth):
    url = "https://" + ip + "/api/v1/ivrs"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def layoutTemplates(ip, auth):
    url = "https://" + ip + "/api/v1/layoutTemplates"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def ldapMappings(ip, auth):
    url = "https://" + ip + "/api/v1/ldapMappings"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def ldapServers(ip, auth):
    url = "https://" + ip + "/api/v1/ldapServers"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def ldapSources(ip, auth):
    url = "https://" + ip + "/api/v1/ldapSources"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def ldapSyncs(ip, auth):
    url = "https://" + ip + "/api/v1/ldapSyncs"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def ldapUserCoSpaceTemplateSources(ip, auth):
    url = "https://" + ip + "/api/v1/ldapUserCoSpaceTemplateSources"
    return __getrequest__(url, auth)

# ===================================================

@xml_Decorator
@save_Decorator
def outboundDialPlanRules(ip, auth):
    url = "https://" + ip + "/api/v1/outboundDialPlanRules"
    return __getrequest__(url, auth)


@xml_Decorator
@save_Decorator
def participants(ip, auth):
    url = "https://" + ip + "/api/v1/participants"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def systemAlarms(ip, auth):
    url = "https://" + ip + "/api/v1/system/alarms"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def cdrReceivers(ip, auth):
    url = "https://" + ip + "/api/v1/system/cdrReceivers"
    return __getrequest__(url, auth)


@xml_Decorator
@save_Decorator
def configCluster(ip, auth):
    url = "https://" + ip + "/api/v1/system/configuration/cluster"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def configXMPP(ip, auth):
    url = "https://" + ip + "/api/v1/system/configuration/xmpp"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def systemDiag(ip, auth):
    url = "https://" + ip + "/api/v1/system/diagnostics"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def licensing(ip, auth):
    url = "https://" + ip + "/api/v1/system/licensing"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def status(ip, auth):
    url = "https://" + ip + "/api/v1/system/status"
    return __getrequest__(url, auth)


@xml_Decorator
@save_Decorator
def tenantGroups(ip, auth):
    url = "https://" + ip + "/api/v1/tenantGroups"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def tenants(ip, auth):
    url = "https://" + ip + "/api/v1/tenants"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def turnServers(ip, auth):
    url = "https://" + ip + "/api/v1/turnServers"
    return __getrequest__(url, auth)


@xml_Decorator
@save_Decorator
def userProfiles(ip, auth):
    url = "https://" + ip + "/api/v1/userProfiles"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def users(ip, auth):
    url = "https://" + ip + "/api/v1/users"
    return __getrequest__(url, auth)

@xml_Decorator
@save_Decorator
def webBridges(ip, auth):
    url = "https://" + ip + "/api/v1/webBridges"
    return __getrequest__(url, auth)








