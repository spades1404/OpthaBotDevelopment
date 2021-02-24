from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from threading import Thread
from Class.globalF import globalFuncs

from Screens.LOGIN import LogInScreen
from Screens.PRIMARY import PrimaryScreen
from Screens.SETUP import SetupScreen


class OpthaBotApp(MDApp):
    def build(self):
        self.on_stop = self.onClose
        # Themes
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.secondary_palette = "Purple"
        #self.theme_cls.theme_style = "Dark"
        self.icon = globalFuncs.directories.icon
        Window.maximize()

        # Screen stuff
        self.screenManager = ScreenManager()
        self.loginScreen = LogInScreen()
        self.primaryScreen = PrimaryScreen()
        self.setup = SetupScreen()

        self.screenManager.add_widget(self.loginScreen)
        self.screenManager.add_widget(self.primaryScreen)
        self.screenManager.add_widget(self.setup)

        self.checkFirstStartup()

        return self.screenManager

    def checkFirstStartup(self):
        print(globalFuncs.permaSet)
        if bool(globalFuncs.permaSet["firstBoot"]) == True:
            self.screenManager.current = "SETUP"

    def onClose(self):
        def function():
            print("Initiating Shutdown")
            print("Clearing Temp Folder")
            globalFuncs.clearTemp()

        Thread(target=function, daemon=True).start()


OpthaBotApp().run()