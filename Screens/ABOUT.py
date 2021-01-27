from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from Screens.HELPERS import aboutScreenHelper

class AboutScreen(MDScreen):
    def __init__(self):
        super(AboutScreen, self).__init__()
        self.name = "ABOUT"
        self.content = Builder.load_string(aboutScreenHelper)
        self.add_widget(self.content)
