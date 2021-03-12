import os
import sys
from threading import Thread

import kivy
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from Class.globalF import globalFuncs
from Screens.LOGIN import LogInScreen
from Screens.PRIMARY import PrimaryScreen
from Screens.SETUP import SetupScreen
from kivy.config import Config
import time

class OpthaBotApp(MDApp):
    def build(self):

        #Functions to run when we open/close the app
        self.on_start = self.onOpen
        self.on_stop = self.onClose

        # Themes
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.secondary_palette = "Purple"
        # self.theme_cls.theme_style = "Dark"

        self.icon = globalFuncs.directories.icon #Sets Top left icon
        Window.maximize()

        # Screen stuff
        self.screenManager = ScreenManager()
        self.loginScreen = LogInScreen()
        self.primaryScreen = PrimaryScreen()
        self.setup = SetupScreen()

        self.screenManager.add_widget(self.loginScreen)
        self.screenManager.add_widget(self.primaryScreen)
        self.screenManager.add_widget(self.setup)

        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')



        return self.screenManager

    def onOpen(self):
        def function():
            print("Checking for first boot")
            if bool(globalFuncs.appInfo["firstboot"]) == True:
                self.screenManager.current = "SETUP"
            print("Checking for new model updates")
            #if globalFuncs.database.checkModelUpdate() == True:
            #    self.modelUpdate = True
            #else:
            #    self.modelUpdate = False

            return

        Thread(target=function,daemon=True).start()

    def onClose(self):
        print("Initiating Shutdown")
        print("Re-encrypting settings")
        globalFuncs.aes.encrypt(globalFuncs.directories.configfile,globalFuncs.directories.configfilecrypted)
        print("Clearing Temp Folder")
        globalFuncs.clearTemp()


def resourcePath():
    '''Returns path containing content - either locally or in pyinstaller tmp file'''
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS)

    return os.path.join(os.path.abspath("."))


if __name__ == "__main__":
    kivy.resources.resource_add_path(resourcePath())  #For our deployment hooks
    OpthaBotApp().run() #Runs the program
