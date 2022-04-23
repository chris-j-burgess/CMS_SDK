In top level folder:
        CMS_SDK
        |- docs
        |- src
        |- tests
        |- LICENSE
        |- requirements.txt
        |- setup.py
    
docs - documentation for the project.  Set up to use Sphinx later in the project once all the docstrings are in.  But contains .md file explaining set-up and use.

src -  main source code

tests - all tests for Test Driven Development

requirements.txt - to load all dependencies.  See *Setting up on Ubuntu* below.

setup.py - 


--------------------------------
**Setting up on Ubuntu**

# Check Linux Distro is up to date
# Either:

sudo apt update && sudo apt upgrade -y

# Or:

sudo apt update
sudo apt upgrade


# Check Python version

python --version

# Install Git

sudo apt-get install git
git --version

# Upgrade PIP to latest version

python3 -m pip install --upgrade pip

------------------------------------------

# Create Dev Directory

mkdir dev

cd dev

# Clone the Git repository

git clone https://github.com/chris-j-burgess/CMS_SDK.git

# change directory into cloned directory

cd CMS_SDK

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source ./venv/bin/activate

# Install requirements file
pip install -r requirements.txt

# Let's use the project

---------------------------------
**Using the Project**

Inside the src code:

    src
    |- CMS_SDK
    |- Output

output - folder for capturing files downloaded from CMS.  These can be deleted or stored elsewhere after use.

Inside the main CMS_SDK code:
    
    CMS_SDK
    |- templates
    |- variables
    |- __init__.py
    |- __main__.py
    |- api_calls.py
    |- convert_to_yaml.py
    |- init.py

**Getting Started**

* Ensure config.cfg file in 'variables' folder includes the correct log in details. 'test' parameter is not currently set, is designed to be used to change the Verify settings in the API in function method_choice in 'api_calls.py'.

* __init__.py has a variable for the file path of variables/config.cfg.  This may need changing.

* __main__.py is the main entry point, and is entered from src folder:
        admin@LINUX_DEVICE:/mnt/c/python/CMS_SDK/src$ python CMS_SDK -m coSpaces
    There are various CLI commands which can be used:
        "python CMS_SDK -m <method_name>"  - will output the method
        "python CMS_SDK -m get_facts"  - will run all the methods against the CMS server and save the JSON output.
        "python CMS_SDK -m set_up"  - will run through files in a chosen input file (variable at top of init.py), and then run POST calls against each of the methods to generate content in CMS
 


