from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen

from Screens.HELPERS import  primaryScreenHelper
from Screens.HOME import HomeScreen
from Screens.ABOUT import AboutScreen
from Screens.SETTINGS import SettingsScreen
from Screens.SEARCH import SearchScreen
from Screens.SCANS import ScanListViewScreen
from Screens.VIEWSCAN import ViewScanScreen




class PrimaryScreen(MDScreen):
    def __init__(self):
        super(PrimaryScreen, self).__init__()
        self.name = "PRIMARY"

        self.content = Builder.load_string(primaryScreenHelper) #Define the gui
        self.add_widget(self.content) #add it to our screen

        #Def Screens
        self.homeScreen = HomeScreen()
        self.aboutScreen = AboutScreen()
        self.settingsScreen = SettingsScreen()
        self.searchScreen = SearchScreen()
        self.viewScansScreen = ScanListViewScreen()
        self.viewSingleScanScreen = ViewScanScreen()

        #Add screens to manager
        self.content.ids.primaryScreenManager.add_widget(self.homeScreen)
        self.content.ids.primaryScreenManager.add_widget(self.aboutScreen)
        self.content.ids.primaryScreenManager.add_widget(self.settingsScreen)
        self.content.ids.primaryScreenManager.add_widget(self.searchScreen)
        self.content.ids.primaryScreenManager.add_widget(self.viewScansScreen)
        self.content.ids.primaryScreenManager.add_widget(self.viewSingleScanScreen)



