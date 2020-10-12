import time
import os
import json
import utils.config_parser as cfgParser

# Get root and sub-paths
root_dir = os.getcwd()
shortcut_dir = root_dir + "/shortcut"
json_dir = root_dir + "/resources/first_time.json"

# Config files
INCOMPLETE = "Please update the config file"
COMPLETE = {
    "firstTime":False
}

#Greeting
GREETING = """
===========Zoom Automation============
Please setup the config file with your
course schedule before proceeding...
======================================

Is the config file ready? [y/n]
"""


#First time running program
def first_time():
    while True:
        with open(json_dir, "r") as fr:
            data = json.load(fr)
        if not data["firstTime"]:
            cfgParser.start()
        else:
            userInput = input(GREETING)
            if (userInput == "n") or (userInput == "N"):
                print(INCOMPLETE)
                time.sleep(3)
                continue
            elif (userInput == "y") or (userInput == "Y"):
                with open(json_dir, "w") as fw:
                    json.dump(COMPLETE, fw, indent=4)
                    import utils.shortcut
                    time.sleep(5)
                    continue
            else:
                print('Please enter "y" or "n"...')
                time.sleep(3)
                    
# Make /shortcut directory
try:
    os.mkdir(shortcut_dir)
except(FileExistsError):
    pass

# Run startup program
first_time()
