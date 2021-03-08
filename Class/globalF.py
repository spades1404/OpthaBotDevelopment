import time

from Class.crypto import Password, AES
from Class.database import Database
from Class.directories import Directories
from Class.validation import Validation

global globalFuncs
from threading import Event
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import shutil
from threading import Thread
import logging

import configparser


class GLOBAL(): #This will store global information that may need to be accessed from multiple screens
    def __init__(self):
        self.directories = Directories().makeTemp()
        self.validation = Validation()
        self.password = Password()
        self.aes = AES()

        self.currentUser = None

        self.aes.loadKey(self.directories.aeskey)
        self.aes.decrypt(self.directories.configfilecrypted,self.directories.configfile)

        # Global app triggers and dialogs
        self.exit_event = Event()
        self.dialog = None  # This wil handle all dialog boxes for the program - its easier to manage
        self.logger = logging.getLogger("OPTHABOT")

        #configuration
        self.config = configparser.ConfigParser()
        self.config.optionxform = str #STOPS CONFIGPARSER FROM MAKING EVERYTHING LOWERCASE
        self.config.read(self.directories.configfile,encoding="utf-8")
        self.appSettings = self.formatDictionary(self.config._sections["settings"])
        self.appInfo = self.formatDictionary(self.config._sections["appinfo"])

        print(self.appInfo)

        self.database = Database()

        time.sleep(5) ##Allows all async functions to catch up before we continue



    def formatDictionary(self,dict):
        for key in dict:
            if dict[key] == "True" or dict[key] == "true":
                dict[key] = True
            elif dict[key] == "False" or dict[key] == "false":
                dict[key] = False
            else:
                continue

        return dict




    def closeDialog(self, *args):
        try:
            self.dialog.dismiss()
        except:
            print("Hm thats odd maybe theres no dialog here?")

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
        x.call('wm', 'attributes', '.', '-topmost', True)
        f = askopenfilename()
        x.destroy()
        return f
    ''' no longer needed - deprecated - will be removed in later versions
    def jsonLoad(self,filename):
        with open(filename) as f_in:
            return (json.load(f_in))

    def jsonSave(self,data,dir):
        with open(dir, 'w') as fp:
            json.dump(data, fp)
    '''
    def saveConfig(self):
        with open(self.directories.configfile, 'w') as configfile:
            self.config.write(configfile)

        globalFuncs.aes.encrypt(globalFuncs.directories.configfile, globalFuncs.directories.configfilecrypted)


    #def saveAppSettings(self):
    #    self.jsonSave(self.appSettings,self.directories.appConfigFile)

    def clearTemp(self):
        shutil.rmtree(self.directories.temp)  # this deletes the directory

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

if __name__ == "__main__":
    print("")