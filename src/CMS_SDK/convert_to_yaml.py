
from importlib.abc import Loader
import xmltodict
import os
import yaml

#  Script to open XML and convert to YAML

# for file_name in os.listdir('src/output'):
#     if file_name.endswith('.xml'):
#         filename, extension = file_name.split('.')
#         with open(f"src/output/{file_name}", "r") as store:
#             file_format = xmltodict.parse(store.read())
#             yaml_data = yaml.dump(file_format)
#             with open(f"src/CMS_SDK/template/{filename}.yaml", "w") as new_format:
#                 new_format.write(yaml_data)
#     else:
#         continue

with open(f"src/CMS_SDK/template/callBridgeGroups.yaml", "r") as store:
    file_format = yaml.safe_load(store)
    xml_data = xmltodict.unparse(file_format)
    with open(f"src/CMS_SDK/template//back2xml/callBridgeGroups.xml", "w") as new_format:
        new_format.write(xml_data)



