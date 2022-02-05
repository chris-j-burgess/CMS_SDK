#!/usr/bin/env python

"""
Author: Chris Burgess
Purpose: Test Cases for Session Methods

"""

from operator import contains
import src.CMS_SDK.init as init
import json


# def test_decorator():
#     text = init.Session.prettyJSON("""OrderedDict([('accessMethods', OrderedDict([('@total', '1'),
#      ('accessMethod', OrderedDict([('@id', '2f32a0b8-3ea9-4b09-85cf-39b2ded369a2'),
#       ('uri', '80570001'), ('callId', '80570001'), ('passcode', '12345'), ('name', 'Chairperson')]))]))])""")
#     json_text = json("""
#         "accessMethod": {
#             "@id": "2f32a0b8-3ea9-4b09-85cf-39b2ded369a2",
#             "callId": "80570001",
#             "name": "Chairperson",
#             "passcode": "12345",
#             "uri": "80570001"
# """)
#     assert json_text['id'] in text.__dict__['id']


def test_methodchoices():
    assert init.Session.method_choice("coSpaces") == "api.coSpaces"

def test_getarequest():
    