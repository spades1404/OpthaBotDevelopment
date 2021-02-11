from Class.globalF import globalFuncs
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from Screens.LOGIN import LogInScreen
from Screens.PRIMARY import PrimaryScreen
from threading import Thread
from kivy.core.window import Window

class OpthaBotApp(MDApp):
    def build(self):

        self.on_stop = self.onClose
        #Themes
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.secondary_palette = "Purple"
        #self.theme_cls.theme_style = "Dark"
        self.icon = globalFuncs.directories.icon
        Window.maximize()



        #Screen stuff
        self.screenManager = ScreenManager()
        self.loginScreen = LogInScreen()
        self.primaryScreen = PrimaryScreen()


        self.screenManager.add_widget(self.loginScreen)
        self.screenManager.add_widget(self.primaryScreen)

        return self.screenManager

    def onClose(self):

        def function():
            print("Initiating Shutdown")
            print("Clearing Temp Folder")
            globalFuncs.clearTemp()

        Thread(target=function, daemon=True).start()


OpthaBotApp().run()