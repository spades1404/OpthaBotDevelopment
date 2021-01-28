from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import ThreeLineListItem

from Screens.HELPERS import searchScreenHelper
from Class.globalF import globalFuncs
from threading import Thread



class SearchScreen(MDScreen):
    def __init__(self):
        super(SearchScreen, self).__init__()
        self.name = "SEARCH"
        self.content = Builder.load_string(searchScreenHelper)
        self.add_widget(self.content)
        self.currentListItems = []


    def search(self):
        def function():
            self.content.ids.spinner.active = True
            result = globalFuncs.database.searchPX(
                fName=self.content.ids.fNameEntry.text,
                lName=self.content.ids.lNameEntry.text,
                email=self.content.ids.emailEntry.text,
                id=self.content.ids.orgIDEntry.text,
                postcode=self.content.ids.postcodeEntry.text,
                phone=self.content.ids.phoneEntry.text,
                addy=self.content.ids.addy1Entry.text
            )
            if result == []:
                self.content.ids.spinner.active = False
                return

            #Next clear the list using some list comprehension
            [self.content.ids.resultListView.remove_widget(i) for i in self.currentListItems]

            #Next create a new widget list with some list comprehension

            self.currentListItems = [
                ThreeLineListItem(
                    text = "{} {}".format(i["fName"],i["lName"]),
                    secondary_text = "ID: {}".format(i["orgID"]),
                    tertiary_text = "Click to show details"
                ) for i in result
            ]

            #Finally insert the new list items

            [self.content.ids.resultListView.add_widget(i) for i in self.currentListItems]
            self.content.ids.spinner.active = False



        Thread(target=function,daemon=True).start()



