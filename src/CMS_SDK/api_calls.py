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


# Test Getters to be deleted
def xml_Decorator(f) -> dict:
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
        output_dir = "output"
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


def _getarequest(uri, auth, params=None):
    "A test wrapper for GET Requests for Restconf XML requests"
    headers = {"Accept": "application/yang-data+xml, application/yang-data.errors+xml"}
    response = requests.get(uri, auth=auth, headers=headers, params=params)
    return response.content


def restconf_test(ip, auth):
    "This only a test RESTCONF request to show handling for XML"
    url = "https://" + ip + "/restconf/data/openconfig-interfaces:interfaces"
    return _getarequest(url, auth)


def ucsm_xml_api_test(ip, auth):
    "Needs completing - This only a second test to UCS to show handling for XML"
    pass


# GET Requests API calls for Cisco Meeting Server


methods = {
    "coSpaces": "/api/v1/coSpaces",
    "coSpace_bulk_params": "/api/v1/coSpaceBulkParameterSets",
    "coSpace_bulk_sync": "/api/v1/coSpaceBulkSyncs",
    "coSpace_templates": "/api/v1/coSpaceTemplates",
    "dial_plan_outbound": "/api/v1/outboundDialPlanRules",
    "dial_transforms": "/api/v1/dialTransforms",
    "call_profiles": "/api/v1/callProfiles",
    "rest_test": "/api/v1/callBrandingProfiles",
    "callBrandingProfiles": "/api/v1/callBrandingProfiles",
    "callBridgeGroups": "/api/v1/callBridgeGroups",
    "callBridges": "/api/v1/callBridges",
    "callLegProfiles": "/api/v1/callLegProfiles",
    "calls": "/api/v1/calls",
    "compatibilityProfiles": "/api/v1/compatibilityProfiles",
    "dtmfProfiles": "/api/v1/dtmfProfiles",
    "forwarding_rules": "/api/v1/forwardingDialPlanRules",
    "inboundDialPlanRules": "/api/v1/inboundDialPlanRules",
    "ivrs": "/api/v1/ivrs",
    "ldapMappings": "/api/v1/ldapMappings",
    "ldapServers": "/api/v1/ldapServers",
    "ldapSources": "/api/v1/ldapSources",
    "ldapSyncs": "/api/v1/ldapSyncs",
    "ldapUserCoSpaceTemplateSources": "/api/v1/ldapUserCoSpaceTemplateSources",
    "list_calls": "/api/v1/calls",
    "outboundDialPlanRules": "/api/v1/outboundDialPlanRules",
    "participants": "/api/v1/participants",
    "systemAlarms": "/api/v1/system/alarms",
    "cdrReceivers": "/api/v1/system/cdrReceivers",
    "configCluster": "/api/v1/system/configuration/cluster",
    "configXMPP": "/api/v1/system/configuration/xmpp",
    "systemDiag": "/api/v1/system/diagnostics",
    "licensing": "/api/v1/system/licensing",
    "status": "/api/v1/system/status",
    "tenantGroups": "/api/v1/tenantGroups",
    "tenants": "/api/v1/tenants",
    "turnServers": "/api/v1/turnServers",
    "userProfiles": "/api/v1/userProfiles",
    "users": "/api/v1/users",
    "webBridges": "/api/v1/webBridges",
}


@xml_Decorator
def _getrequest(uri, auth, verify=False, params=None):
    headers = {"Accept": "application/xml"}
    response = requests.get(
        uri, auth=auth, headers=headers, params=params, verify=False
    )
    return response.content


def _postrequest(uri, auth, body, verify=False, params=None):
    headers = {"Accept": "application/xml", "Content-Type": "application/xml"}
    response = requests.post(
        uri, auth=auth, headers=headers, params=params, verify=verify, data=body
    )
    return response.status_code


def method_choice(
    method: str,
    call: str,
    ip: str,
    auth: tuple,
    test=True,
    body=False,
) -> dict:

    "This allows args.method to choose a method and make a call.  The CMS calls need building as instance methods, like self.rest_test"
    url = f"https//{ip}" + methods.get(method)
    if test:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        verify = False
    else:
        verify = True
    if call == "POST" and body != None:
        return _postrequest(url, auth, body, verify)
    else:
        return _getrequest(url, auth, verify)
