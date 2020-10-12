import schedule
import pyautogui
import cv2
import time
import os
import sys

auto = pyautogui

class weekday:
    # Obtain variable data
    def __init__(self, num_days, course, meeting_id, password, start_time, weekday):
        # Run zoom shortcut + enter password
        self.root = os.getcwd()
        self.dirShortcut = self.root + "/shortcut"
        self.ocr = self.root + '/resources/OCR.png'

        #parse
        self.num_days = num_days
        self.course = course
        self.meeting_id = meeting_id
        self.start_time = start_time
        self.password = password
        self.weekday = weekday

    # Script for open zoom + enter pwd
    def job(self, course_name, password, path):
        os.startfile(path + '/' + course_name + '.lnk')
        time.sleep(5)
        coord = auto.locateCenterOnScreen(self.ocr, confidence=.6)
        xcoor = coord[0]
        ycoor = coord[1]

        auto.click(xcoor, ycoor, 1, 0, 'left')
        auto.write(str(password))
        auto.press('enter')

    # Interpret weekdays
    def interpret(self):
        # Switch-case for weekday recognition
        for k in range(0, self.num_days, 1):
            try:
                if self.weekday[k] == 'monday':
                    schedule.every().monday.at(self.start_time).do(self.job, self.course, self.password, self.dirShortcut)
                elif self.weekday[k] == 'tuesday':
                    schedule.every().tuesday.at(self.start_time).do(self.job, self.course, self.password, self.dirShortcut)
                elif self.weekday[k] == 'wednesday':
                    schedule.every().wednesday.at(self.start_time).do(self.job, self.course, self.password, self.dirShortcut)
                elif self.weekday[k] == 'thursday':
                    schedule.every().thursday.at(self.start_time).do(self.job, self.course, self.password, self.dirShortcut)
                elif self.weekday[k] == 'friday':
                    schedule.every().friday.at(self.start_time).do(self.job, self.course, self.password, self.dirShortcut)
                elif self.weekday[k] == 'saturday':
                    schedule.every().saturday.at(self.start_time).do(self.job, self.course, self.password, self.dirShortcut)
                elif self.weekday[k] == 'sunday':
                    schedule.every().sunday.at(self.start_time).do(self.job, self.course, self.password, self.dirShortcut)
                else:
                    print("ERROR: " + "[Invalid date format]")
                    print("Please update the config file")
                    sys.exit(1)
            except Exception as e:
                print("ERROR: [{}]".format(str(e)))
                print("Please update the config file")
                sys.exit(1)
