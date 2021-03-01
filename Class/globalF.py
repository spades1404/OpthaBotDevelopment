import time
from Class.directories import Directories
from Database.firebase import Database
from Class.validation import Validation
from Class.password import Password
global globalFuncs
from threading import Event
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import json
import os, shutil
from threading import Thread


class GLOBAL(): #This will store global information that may need to be accessed from multiple screens
    def __init__(self):
        self.database = Database()
        self.directories = Directories()
        self.currentUser = None
        self.validation = Validation()
        self.password = Password()
        self.getAppSettings()

        # Global app triggers and dialogs
        self.exit_event = Event()
        self.dialog = None  # This wil handle all dialog boxes for the program - its easier to manage

    def closeDialog(self, *args):
        self.dialog.dismiss()

    def updateProgressBar(self, progressRange, timeLapse, target):  # the filled example will run for 100 seconds
        self.exit_event.clear()
        for i in range(progressRange[0], progressRange[1]):
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

    def jsonSave(self,data,dir):
        with open(dir, 'w') as fp:
            json.dump(data, fp)

    def getAppSettings(self):
        self.appSettings = self.jsonLoad(self.directories.appConfigFile)
        self.permaSet = self.jsonLoad(self.directories.appPermaSets)

    def saveAppSettings(self):
        self.jsonSave(self.appSettings,self.directories.appConfigFile)

    def clearTemp(self):
        folder = self.directories.temp
        shutil.rmtree(folder)  # this deletes the directory
        os.mkdir(folder)

    def compareDate(self, date1, date2):
        if date1.strftime("%d:%m:%Y") == date2.strftime("%d:%m:%Y"):
            return True
        else:
            return False

    def threadedSet(self, var, val):
        def function():
            var = val

        Thread(target=function, daemon=True).start()

globalFuncs = GLOBAL() #We need the class to be static from start!
