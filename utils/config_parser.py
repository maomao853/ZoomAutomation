import os
import yaml
import time
import schedule
import re
import sys
from . import weekday_interpreter

root = os.getcwd()
dir_config = root + "/config.yaml"

def start():
    # Open config and parse 'number of courses'
    with open(dir_config, "r") as stream:
        data = yaml.safe_load(stream)
        num_course = data["num_course"] + 1

    # Loop + Parse each course info
    for i in range(1, num_course, 1):
        dict = data[i]

        course = dict["course"]
        meetingID = dict["meetingID"]
        password = dict["password"]
        startTime = dict["start_time"]
        weekDict = dict["weekday"]

        # parse weekdays + number of days
        weekSchedule = re.split(',', weekDict)
        numDays = len(weekSchedule)

        # Check if shortcuts exist
        root_dir = os.getcwd()
        lnk_dir = root_dir + "/shortcut/"
        file = lnk_dir + course + ".lnk"

        file_exist = os.path.exists(file)

        if file_exist:
            # call week_interpret class
            week = weekday_interpreter.weekday(numDays, course, meetingID, password, startTime, weekSchedule)
            week.interpret()
            print("Initialized  [ {} ]".format(course))
        else:
            sys.exit("Problem with course: " + course)

    # Scheduler run 24/7
    while True:
        schedule.run_pending()
        time.sleep(1)
