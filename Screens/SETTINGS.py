from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from Screens.HELPERS import settingsScreenHelper

class SettingsScreen(MDScreen):
    def __init__(self):
        super(SettingsScreen, self).__init__()
        self.name = "SETTINGS"
        self.content = Builder.load_string(settingsScreenHelper)
        self.add_widget(self.content)
