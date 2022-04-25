#!/usr/bin/env python

"""
Author: Chris Burgess
Purpose: Initiate Session, Meetings, Calls and other events

"""

from datetime import date
import yaml, json
import os
import api_calls as api
import functools
from urllib.parse import urlencode
import pprint


input_dir = "CMS_SDK/templates"
output_dir = "output1"
file_path = "/mnt/c/Users/alpinist/python/CMS_SDK/src/CMS_SDK/variables/config.cfg"
date = date.today().strftime("%b-%d-%Y")


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

    def __init__(self, file_path=file_path, method=None):

        #  Load the config file with key detail
        with open(file_path, "rt") as handle:
            config = yaml.safe_load(handle)
            self.file = file_path
            self.test = config["config"]["test"]
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

    # @prettyJSON
    def method_choice(self, method, call, data, uri=None):
        "This allows args.method to choose a method and make a call.  The CMS calls need building as instance methods, like self.rest_test"
        return api.method_choice(
            method, call, self._ip, self._auth, self.test, body=data, uri=uri
        )

    def write_file(self, name, call):
        print(f"Performing REST call against {name}")
        try:
            method_ouput = self.method_choice(name, call)
            print(f"Saving JSON output of {name} to {output_dir} directory")
            with open(f"{output_dir}/{name}-{date}.txt", "w") as f:
                f.write(method_ouput)
        except TypeError:
            print(f"Unable to perform REST request against: {name}")

    def get_facts(self):
        """
        Creates an output directory, if one doesn't already exist
        Gets a list of methods.
        Performs a GET Request against each method and
        Converts to JSON response and saves to .json file in output folder

        Args: None

        Returns:
            REST Response content

        Raises:
            requests.exceptions.RequestException:  (includes ConnectionError, HTTPError, Timeout, TooManyRedirects)
            OSError, TypeError - file handling
        """
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)
            print(f"Creating {output_dir} directory .....")
        methods = api.list_methods()
        for method in methods:
            try:
                print(f"Performing REST call against {method}")
                text = self.method_choice(method=method, call="GET", data=None)
                print(f"Saving JSON output of {method} to {output_dir} directory")
                with open(f"{output_dir}/{method}-{date}.json", "w") as jfile:
                    jfile.write(text)
            except (ConnectionError, HTTPError, Timeout, TooManyRedirects):
                print(f"Unable to perform REST request against: {method}")
            except (OSError, TypeError):
                print(f"Unable to save file for {method}")
            except Exception as err:
                print(f"Unexpected error with {method} is", repr(err))
                sys.exit(1)

    def _yaml2dict(self, file_input):
        return yaml.safe_load(file_input)

    def _json2dict(self, file_input):
        return json.load(file_input)

    def set_up(self):
        """
        Set-up a CMS Server with existing XML files.


        Args: None

        Returns:
            Success or failure codes of REST POST request

        Raises:
            requests.exceptions.RequestException:  (includes ConnectionError, HTTPError, Timeout, TooManyRedirects)
            OSError, TypeError - file handling
        """
        call = "POST"
        for file_name in os.listdir(input_dir):
            filename, extension = file_name.split(".")
            with open(f"{input_dir}/{file_name}", "r") as template:
                read_input = template.read()
                if extension == "yaml" or extension == "yml":
                    data = _yaml2dict(read_input)
                if extension == "json" or extension == "jsn":
                    data = _json2dict(read_input)
                else:
                    data = read_input

                api_call = self.method_choice(filename, call, data)

                print(api_call)

                # if int(api_call) >= 200 and int(api_call) <= 300:
                #     print(f"API call to {filename} successful")
                # if int(api_call) >= 300:
                #     print(
                #         f"API Call to {filename} unsuccessful - Status Code {api_call}"
                #     )


class Space(Session):
    def __init__(self, coSpaceID=None, callLegProfileID=None):
        super().__init__()
        if coSpaceID:
            self.coSpaceID = coSpaceID
        if callLegProfileID:
            self.callLegProfileID = callLegProfileID
        self.stored_values = {}
        self.stored_value_tracker = 0

    def interactive(self, coSpaceID=None):
        if coSpaceID:
            self.coSpaceID = coSpaceID
            print(f"Current coSpaceID is:  {self.coSpaceID}")
        else:
            print(f"No Current coSpaceID exists")
        choice = input("""\n What would you like to do? \n
        1. Create a coSpace 
        2. Modify a coSpace
        3. Delete a coSpace
        4. List coSpaces
        5. Select a value from a coSpace
        6. Print stored values
        7. Add a coSpace Member
        8.  Post to a message board of a coSpace
        9. Others
        \n?
        """)
        if int(choice) == 1:
            get_request=self.create_coSpace()
            coSpaceID = get_request['coSpace']['@id']
            self.interactive(coSpaceID)
        if int(choice) == 3:
            self.delete_coSpace()
        if int(choice) == 4:
            self.list_coSpaces()
        if int(choice) == 5:
            self.select_coSpace_value()
        if int(choice) == 6:
            self.print_stored_values()
        else:
            print("Choice not recognised")


    def create_coSpace(self):
        """
        POST of template - returns the Location from the header"""
        with open(f"{input_dir}/coSpaces.yaml", "r") as template:
            read_input=yaml.safe_load(template)
            encoded_input = urlencode(read_input)
            api_call = self.method_choice("coSpaces", "POST", data=encoded_input, uri=None)
            get_request = self.method_choice(
                "coSpaces", "GET", data=None, uri=api_call
            )
            coSpaceID = get_request['coSpace']['@id']
            self.coSpaceID = coSpaceID
            return get_request

    def change_coSpace(self, coSpaceID):
        # change = self.method_choice("coSpaces", "PUT", data=encoded_input, uri=api_call)
        pass

    def delete_coSpace(self, coSpaceID=None):
        if coSpaceID:
            print(f"Deleting {coSpaceID}")
            self._continue
        else:
            coSpaceID = input("No coSpaceID.  Input coSpaceID: ")
            print(f"Deleting {coSpaceID}")
            self._continue
        try:
            delete_request = self.method_choice(
                "coSpaces", "DELETE", data=None, uri=f"/api/v1/coSpaces/{coSpaceID}"
            )
            print(f"Deleted {coSpaceID}")
        except:
            pass
        return self.interactive()

    def select_coSpace_value(self, coSpaceID=None):
        if coSpaceID:
            print(f"Collecting values for {coSpaceID}")
            self._continue
        else:
            coSpaceID = input("No coSpaceID.  Input coSpaceID: ")
            print(f"Collecting values for {coSpaceID}")
            self._continue()
            try:
                response = self.method_choice(
                    "coSpaces", "GET", data=None, uri=f"/api/v1/coSpaces/{coSpaceID}"
                )
            except KeyError:
                self.interactive()

            dictionary = {}
            count_i = 0
    

            for key, value in response['coSpace'].items():
                dictionary[count_i] = (f" Key: {key}", f" Value: {value}" )
                count_i = count_i + 1
            pprint.pprint(dictionary)
            selection = input("Select a value by entering a number or any key to exit: ")
            try:    
                print(f"You chose: {selection}\n")
                choice = dictionary.get(int(selection))
                key_value = dictionary.get(0)
                print(f"You chose: {selection}, {choice[0]}  = {choice[1]} \n")
                self.insert_stored_value(key_value[1], choice[1])
            except Exception as err:
                print(repr(err))
                print("Choice not recognised")
        return self.interactive()
    
    def insert_stored_value(self, key, value):
        self.stored_values[self.stored_value_tracker] = (key,value)
        self.stored_value_tracker = self.stored_value_tracker + 1
        print(f"Current stored values:  {self.stored_values}")

    def print_stored_values(self):
        print(f"Current stored values:")
        pprint.pprint(self.stored_values)
        return self.interactive()

    def pretty_print_results(self, data):
        dictionary = {}
        key = 0
        coSpace = data['coSpaces']['coSpace']
        for result in coSpace:
            dictionary[key] = (f" Cospace: {result['@id']}", f" Name: {result['name']}" )
            key = key + 1
        pprint.pprint(dictionary)

    def _continue(self):
        choice = input("Continue y/n ?\n")
        if choice == 'y' or choice == 'Y':
            return True
        else:
            quit(self.interactive())

        
    def list_coSpaces(self):
        get_request = self.method_choice(
                "coSpaces", "GET", data=None, uri=None
            )
        total = int(get_request['coSpaces']['@total'])
        print(f"""\nTotal number of coSpaces currently is: {total}\n
        Loading in batches of 20\n""")
        
        get_request = self.method_choice(
                "coSpaces", "GET", data=None, uri="/api/v1/coSpaces/?offset=0&limit=20"
            )
        self.pretty_print_results(get_request)
        self._continue()
        
        
        count = total - 20
        offset = 20
        limit = 20

        while count > 0:
            uri = f"/api/v1/coSpaces/?offset={offset}&limit={limit}"
            next_request = self.method_choice(
                 "coSpaces", "GET", data=None, uri=uri
                )
            self.pretty_print_results(next_request)
            self._continue()
            count = count - 20
            offset = offset + 20
        
        return self.interactive()

    def filter_coSpaces(self):
        #"?offset=&limit=&filter=&tenantFilter=&callLegProfileFilter="
        # use filters provided as docs:
        # https://ciscocms.docs.apiary.io/#reference/cospace-related-methods/retrieving-cospaces/retrieving-cospaces
        pass


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
