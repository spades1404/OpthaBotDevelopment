from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from Screens.HELPERS import searchScreenHelper

class SearchScreen(MDScreen):
    def __init__(self):
        super(SearchScreen, self).__init__()
        self.name = "SEARCH"
        self.content = Builder.load_string(searchScreenHelper)
        self.add_widget(self.content)
        self.searchItems = ["Patients","Scans"]

