from win32com.client import Dispatch
import os
import yaml
import re

root_dir = os.path.realpath('./')
shortcut_dir = root_dir + "/shortcut"

#remove spaces in meetingID
def meeting_convert(ID):
    split = re.split(r"\s+", ID)
    newMeetingID = split[0] + split[1] + split[2]
    return(newMeetingID)

#create shortcut
def create_shortcuts(classcode, exe_path, startin, icon_path, args, directory):
    shell = Dispatch('WScript.Shell')
    shortcut_file = os.path.join(directory, classcode + '.lnk')
    shortcut = shell.CreateShortCut(shortcut_file)
    shortcut.Targetpath = exe_path
    shortcut.Arguments = args
    shortcut.WorkingDirectory = startin
    shortcut.IconLocation = icon_path
    shortcut.save()
    print("Shortcut for [ {} ] created...".format(classcode))

#open + parse config.yaml
with open("config.yaml", "r") as stream:
    data = yaml.safe_load(stream)

    appdata = os.getenv("APPDATA")
    dir_zoom = appdata + "/Zoom/bin"
    exe_zoom = dir_zoom + "/Zoom.exe"
    num_course = data["num_course"] + 1

    for i in range(1, num_course, 1):
        try:
            dict = data[i]

            course = dict["course"]
            meetingID = dict["meetingID"]

            newID = meeting_convert(meetingID)
            TARGET = '"--url=zoommtg://zoom.us/join?action=join&confno={}"'.format(str(newID))

            create_shortcuts(course, exe_zoom, dir_zoom, exe_zoom, TARGET, shortcut_dir)
        except(TypeError):
            print("ERROR: [TypeError]")
            pass
