import time
from Class.directories import Directories
from Database.firebase import Database
from Class.validation import Validation
global globalFuncs
from threading import Event
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import json


class GLOBAL(): #This will store global information that may need to be accessed from multiple screens
    def __init__(self):
        self.database = Database()
        self.directories = Directories()
        self.currentUser = None
        self.validation = Validation()
        self.getAppSettings()

        self.exit_event = Event()
    def updateProgressBar(self,progressRange, timeLapse, target): #the filled example will run for 100 seconds
        self.exit_event.clear()
        for i in range(progressRange[0],progressRange[1]):
            target.value = i
            time.sleep(timeLapse)

            if self.exit_event.isSet() == True:
                break

    def askforafile(self):
        x = Tk()
        x.withdraw()
        f = askopenfilename()
        x.destroy()
        return f

    def jsonLoad(self,filename):
        with open(filename) as f_in:
            return (json.load(f_in))

    def jsonSave(self,data):
        with open(self.directories.appConfigFile, 'w') as fp:
            json.dump(data, fp)

    def getAppSettings(self):
        self.appSettings = self.jsonLoad(self.directories.appConfigFile)

    def saveAppSettings(self,jsonString):
        self.jsonSave(jsonString)


globalFuncs = GLOBAL() #We need the class to be static from start!
