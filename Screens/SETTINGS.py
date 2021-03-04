from kivy.lang.builder import Builder
from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.selectioncontrol import MDSwitch

from Class.globalF import globalFuncs
from Screens.HELPERS import settingsScreenHelper


class SettingsScreen(MDScreen):
    def __init__(self):
        super(SettingsScreen, self).__init__()
        self.name = "SETTINGS"
        self.content = Builder.load_string(settingsScreenHelper)
        self.add_widget(self.content)
        self.setupSwitchView()

        # will change this later to just have the name
        self.org = globalFuncs.appInfo["org"]
        self.practice = globalFuncs.appInfo["practice"]

        print(self.org)

        #this doesnt work for some reason
        #x = globalFuncs.database.fsdb.collection(u"organisations").document(self.org).get().to_dict()["name"]
        #y = globalFuncs.database.fsdb.collection(u"practices").document(self.org).get().to_dict()["name"]

        self.content.ids.orgname.text = self.org
        self.content.ids.pracname.text = self.practice
    def setupSwitchView(self):
        self.switches = []
        print(globalFuncs.appSettings)
        for key in globalFuncs.appSettings:
            description = key
            state = bool(globalFuncs.appSettings[key])
            print(globalFuncs.appSettings[key])
            print(state)
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
            globalFuncs.config.set("settings",key,str(index.active))

        globalFuncs.saveConfig()


