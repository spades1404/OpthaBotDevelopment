from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget

from functools import partial

from Screens.HELPERS import primaryScreenHelper
from Screens.HOME import HomeScreen
from Screens.ABOUT import AboutScreen
from Screens.SETTINGS import SettingsScreen
from Screens.SEARCH import SearchScreen
from Screens.SCANS import ScanListViewScreen
from Screens.VIEWSCAN import ViewScanScreen
from Screens.USERS import ViewUsersScreen




class PrimaryScreen(MDScreen):
    def __init__(self):
        super(PrimaryScreen, self).__init__()
        self.name = "PRIMARY"

        self.content = Builder.load_string(primaryScreenHelper)  # Define the gui
        self.add_widget(self.content)  # add it to our screen

        # Def Screens
        self.homeScreen = HomeScreen()
        self.aboutScreen = AboutScreen()
        self.settingsScreen = SettingsScreen()
        self.searchScreen = SearchScreen()
        self.viewScansScreen = ScanListViewScreen()
        self.viewSingleScanScreen = ViewScanScreen()
        self.viewUsers = ViewUsersScreen()

        # Add screens to manager
        self.content.ids.primaryScreenManager.add_widget(self.homeScreen)
        self.content.ids.primaryScreenManager.add_widget(self.aboutScreen)
        self.content.ids.primaryScreenManager.add_widget(self.settingsScreen)
        self.content.ids.primaryScreenManager.add_widget(self.searchScreen)
        self.content.ids.primaryScreenManager.add_widget(self.viewScansScreen)
        self.content.ids.primaryScreenManager.add_widget(self.viewSingleScanScreen)
        self.content.ids.primaryScreenManager.add_widget(self.viewUsers)

        self.homeItem = OneLineIconListItem(
            text="Home",
            on_release=partial(self.setDrawer, "HOME"),
        )
        self.homeItem.add_widget(IconLeftWidget(icon="home"))

        self.searchItem = OneLineIconListItem(
            text="Search",
            on_release=partial(self.setDrawer, "SEARCH"),
        )
        self.searchItem.add_widget(IconLeftWidget(icon="magnify"))

        self.scanItem = OneLineIconListItem(
            text="Scans",
            on_release=partial(self.setDrawer, "LISTSCAN"),
        )
        self.scanItem.add_widget(IconLeftWidget(icon="selection-search"))

        self.settingItem = OneLineIconListItem(
            text="Settings",
            on_release=partial(self.setDrawer, "SETTINGS"),
        )
        self.settingItem.add_widget(IconLeftWidget(icon="cogs"))

        self.aboutItem = OneLineIconListItem(
            text="About",
            on_release=partial(self.setDrawer, "ABOUT"),
        )
        self.aboutItem.add_widget(IconLeftWidget(icon="information"))

        self.usersItem = OneLineIconListItem(
            text="Users",
            on_release=partial(self.setDrawer, "USERS"),
        )
        self.usersItem.add_widget(IconLeftWidget(icon="account"))

        self.logoutItem = OneLineIconListItem(
            text="Logout",
        )
        self.logoutItem.add_widget(IconLeftWidget(icon="logout-variant"))

    def configureMenu(self, accessLevel):
        if accessLevel == 3:
            self.menuItems = [self.homeItem, self.aboutItem, self.logoutItem]
        if accessLevel == 2:
            self.menuItems = [self.homeItem, self.searchItem, self.scanItem, self.settingItem, self.aboutItem,
                              self.logoutItem]
        if accessLevel == 1 or accessLevel == 0:
            self.menuItems = [self.homeItem, self.searchItem, self.scanItem, self.settingItem, self.usersItem,
                              self.aboutItem, self.logoutItem]

        [self.content.ids.listMenu.add_widget(i, index=1) for i in self.menuItems]

        return

    def setDrawer(self, name, *args):
        self.content.ids.primaryScreenManager.current = name
        self.content.ids.navDraw.toggle_nav_drawer()
