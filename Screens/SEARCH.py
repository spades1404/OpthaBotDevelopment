from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.list import ThreeLineListItem
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.dialog import MDDialog


from Screens.HELPERS import searchScreenHelper
from Screens.ADDPX import AddPXScreen
from Screens.VIEWPX import ViewPXScreen
from Class.globalF import globalFuncs
from Class.user import Patient
from threading import Thread
from functools import partial
from Screens.VIEWSCAN import ViewScanScreen


class SearchScreen(MDScreen):
    def __init__(self):
        super(SearchScreen, self).__init__()
        self.name = "SEARCH"

        self.screenManager = ScreenManager()

        self.mainContent = Builder.load_string(searchScreenHelper)
        self.addUserScreen = AddPXScreen()
        self.viewPXScreen = ViewPXScreen()
        self.viewScanScreen = ViewScanScreen()
        self.viewScanScreen.content.ids.back.on_release = partial(self.switchScreen,"viewuser")



        self.screenManager.add_widget(self.mainContent)
        self.screenManager.add_widget(self.addUserScreen)
        self.screenManager.add_widget(self.viewPXScreen)
        self.screenManager.add_widget(self.viewScanScreen)
        self.add_widget(self.screenManager)
        self.currentListItems = []


    def switchScreen(self,name):
        self.screenManager.current = name


    def search(self): #THIS FUNCTION NEEDS TO BE FIXED CAPS BREAK IT
        def function():
            self.mainContent.ids.spinner.active = True

            if globalFuncs.validation.checkDate(self.mainContent.ids.dateEntry.ids.dateEntry.text) == False and (self.mainContent.ids.dateEntry.ids.dateEntry.text).replace(" ","") != "":
                MDDialog(title="Error",text="Invalid Date")

            result = globalFuncs.database.searchPX(
                fName=self.mainContent.ids.fNameEntry.text,
                lName=self.mainContent.ids.lNameEntry.text,
                email=self.mainContent.ids.emailEntry.text,
                id=self.mainContent.ids.orgIDEntry.text,
                postcode=self.mainContent.ids.postcodeEntry.text,
                phone=self.mainContent.ids.phoneEntry.text,
                addy=self.mainContent.ids.addy1Entry.text,
                date=self.mainContent.ids.dateEntry.ids.dateEntry.text
            )
            if result == []:
                [self.mainContent.ids.resultListView.remove_widget(i) for i in self.currentListItems] #removing widgets
                self.mainContent.ids.spinner.active = False
                return



            #Next clear the list using some list comprehension
            [self.mainContent.ids.resultListView.remove_widget(i) for i in self.currentListItems]

            #Next create a new widget list with some list comprehension

            self.currentListItems = [
                ThreeLineListItem(
                    text = "{} {}".format(i.fname,i.lname),
                    secondary_text = "ID: {}".format(i.orgID),
                    tertiary_text = "Click to show details",
                    on_release = partial(self.displayPX, i) #DEAR FUTURE RAJIB, THIS IS HOW YOU CAN PASS PARAMETERS THROUGH A FUNCTION CALL

                ) for i in result
            ]

            #Finally insert the new list items

            [self.mainContent.ids.resultListView.add_widget(i) for i in self.currentListItems]
            self.mainContent.ids.spinner.active = False



        Thread(target=function,daemon=True).start()



    def setDate(self,date):
        self.mainContent.ids.dateEntry.ids.dateEntry.text = date.strftime("%d/%m/%Y")
        return

    def selectCalendar(self):
        date_dialog = MDDatePicker(callback=self.setDate)
        date_dialog.open()
        return

    def displayPX(self,px,*args):
        self.screenManager.current = "viewuser"
        self.viewPXScreen.insertUser(px)
        print(id)
