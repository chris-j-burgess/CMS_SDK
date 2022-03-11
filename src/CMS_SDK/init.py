#!/usr/bin/env python

"""
Author: Chris Burgess
Purpose: Initiate Session, Meetings, Calls and other events

"""

import pstats
import yaml, json
import os
import api_calls as api
import functools

input_dir = "input"
output_dir = "output"


def prettyJSON(f):
    "Decorator to be used to take the dictionary out of most api_calls and pass to user interface as JSON"

    @functools.wraps(f)
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return json.dumps(x, indent=4, sort_keys=True)

    return wrap


def typename(obj):
    return type(obj).name


class Session:
    """This is a conceptual class representation the connection to the CMS Server

    :param file: The location of the config file which contains the connection details, defaults to "variables/config.cfg"
    :type file: str, optional
    :param method: A method call which the user has input at command prompt
    :type addr: str, optional
    """

    def __init__(self, file_path="src/CMS_SDK/variables/config.cfg", method=None):

        #  Load the config file with key detail
        with open(file_path, "rt") as handle:
            config = yaml.safe_load(handle)
            self.file = file_path
            self.test = config["config"]["test"]
            if self.test:
                self._ip = config["config"]["ip"]
            else:
                self._ip = config["config"]["ip"] + ":" + config["config"]["port"]
            self._username = config["config"]["username"]
            if config["config"]["password"]:
                self._password = config["config"]["password"]
            else:
                self._password = os.getenv(
                    CMS_PASS
                )  # if password stored in Env Var, capture it.
            self._auth = (self._username, self._password)
            self.method = method

    def __repr__(self) -> str:
        return f"{typename(self).__name__}: (file={self.file}, method={self.method})"

    def __str__(self) -> str:
        return self.__format__

    def __format__(self, format_spec) -> str:
        return f"{typename(self).__name__} connected at {self._ip}"

    # Decorator to be used to take the dictionary out of most api_calls and make easier to read

    @prettyJSON
    def method_choice(self, method, call, data):
        "This allows args.method to choose a method and make a call.  The CMS calls need building as instance methods, like self.rest_test"
        return api.method_choice(method, call, self._ip, self._auth, self.test, data)

    def write_file(self, name, call):
        print(f"Performing REST call against {name}")
        try:
            method_ouput = self.method_choice(name, call)
            print(f"Saving JSON output of {name} to {output_dir} directory")
            with open(f"{output_dir}/{name}.txt", "w") as f:
                f.write(method_ouput)
        except TypeError:
            print(f"Unable to perform REST request against: {name}")

    def get_facts(self):
        call = "GET"
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)
            print(f"Creating {output_dir} directory .....")
        if self.test:
            name = "rest_test"
            self.write_file(name, call)
        else:
            for name in self.methods.keys():
                if name == "rest_test":
                    continue
                else:
                    self.write_file(name, call)

    def _yaml2dict(self, file_input):
        return yaml.safe_load(file_input)

    def _json2dict(self, file_input):
        return json.load(file_input)

    def set_up(self):
        call = "POST"
        for file_name in os.listdir(input_dir):
            filename, extension = file_name.split(".")
            with open(file_name, "r") as read_input:
                if extension == "yaml" or extension == "yml":
                    data = _yaml2dict(read_input)
                if extension == "json" or extension == "jsn":
                    data = _json2dict(read_input)
                else:
                    data = read_input

                api_call = self.method_choice(filename, call, data)

                if api_call >= 200 and api_call <= 300:
                    print(f"API call to {filename} successful")
                if api_call >= 300:
                    print(
                        f"API Call to {filename} unsuccessful - Status Code {api_call}"
                    )


# class Space(Session):
#     def __init__(self, coSpaceID, callLegProfileID=None):
#         super().__init__()
#         self.coSpaceID = coSpaceID
#         if callLegProfileID:
#             self.callLegProfileID = callLegProfileID
#         else:
#             self.callLegProfileID = None

#     def __call__(self, *args, **kwargs):
#         return self(*args, **kwargs)

#     meeting_get_methods = {
#         "coSpaces": self.coSpaces,
#         "coSpace_bulk_params": self.coSpace_bulk_params,
#         "coSpace_bulk_sync": self.coSpace_bulk_sync,
#         "coSpace_templates": self.coSpace_templates,
#         "dial_transforms": self.dial_transforms,
#         "call_profiles": self.call_profiles,
#         "rest_test": self.rest_test,
#     }

#     def method_choice(self, method):
#         "This allows args.method to choose a method and make a call.  The CMS calls need building as instance methods, like self.rest_test"
#         return meeting_get_methods.get(method)()

#     def coSpaces_detail(self):
#         pass

#     @prettyJSON
#     def coSpaces_entry_detail(self):
#         return api.coSpaces_entry_detail(self.__ip, self.__auth, self.coSpaceID)

#     @prettyJSON
#     def coSpaces_listMembers(self):
#         if callLegProfileID:
#             call = api.coSpaces_entry_detail(
#                 self.__ip,
#                 self.__auth,
#                 self.coSpaceID,
#                 callLegProfileID=self.callLegProfileID,
#             )
#         else:
#             call = api.coSpaces_entry_detail(self.__ip, self.__auth, self.coSpaceID)
#         return call

#     @prettyJSON
#     def coSpaces_listMembers(self):
#         if callLegProfileID:
#             call = api.coSpaces_entry_detail(
#                 self.__ip,
#                 self.__auth,
#                 self.coSpaceID,
#                 self.userID,
#                 callLegProfileID=self.callLegProfileID,
#             )
#         else:
#             call = api.coSpaces_entry_detail(
#                 self.__ip, self.__auth, self.userID, self.coSpaceID
#             )
#         return call

# class User(Session):
#     pass

# class Call(Session):
#     pass
