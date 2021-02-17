from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.list import ThreeLineListItem
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.dialog import MDDialog

from Class.globalF import globalFuncs
from Screens.HELPERS import viewUserHelper

class ViewUserScreen(MDScreen):
    def __init__(self):
        super(ViewUserScreen, self).__init__()
        self.name = "viewuser"


        self.content = Builder.load_string(viewUserHelper)
        self.add_widget(self.content)

    def insertUser(self,user):
        return

    def updateUserDetails(self):
        print("updated???!")
        return

    def setDate(self, date):
        self.content.ids.dateEntry.ids.dateEntry.text = date.strftime("%d/%m/%Y")
        return

    def autoGenID(self):
        self.content.ids.orgIDEntry.ids.numEntry.text = globalFuncs.database.generateNewORGID()

    def selectCalendar(self):
        date_dialog = MDDatePicker(callback=self.setDate)
        date_dialog.open()

        return


class ClickableTextFieldRound(RelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()

class ClickableTextFieldRound2(RelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()