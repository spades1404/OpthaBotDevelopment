from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from Screens.HELPERS import settingsScreenHelper
from Class.globalF import globalFuncs
from kivy.metrics import dp
class SettingsScreen(MDScreen):
    def __init__(self):
        super(SettingsScreen, self).__init__()
        self.name = "SETTINGS"
        self.content = Builder.load_string(settingsScreenHelper)
        self.add_widget(self.content)
        self.setupSwitchView()

        self.org = globalFuncs.permaSet["org"]
        self.practice = globalFuncs.permaSet["practice"]


    def setupSwitchView(self):
        self.switches = []
        for key in globalFuncs.appSettings:
            description = key
            state = bool(globalFuncs.appSettings[key])
            switch = MDSwitch(active = state,height = dp(30),size_hint_y = None,size_hint_x = None, width = dp(100))
            label = MDLabel(text = description,valign="center")
            listitem = MDBoxLayout(orientation="horizontal",spacing=1,size_hint_y = None, height = 50)
            listitem.add_widget(label)
            listitem.add_widget(switch)
            listitem.add_widget(MDLabel(text="",size_hint_x=None,width=25))
            self.content.ids.flipSwitchView.add_widget(listitem)
            self.switches.append(switch)


    def saveSettings(self):
        for key, index in zip(globalFuncs.appSettings,self.switches):
            globalFuncs.appSettings[key] = index.active

        globalFuncs.saveAppSettings()


