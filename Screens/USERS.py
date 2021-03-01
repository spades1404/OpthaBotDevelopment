from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.lang.builder import Builder
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from Screens.HELPERS import addUserHelper, viewUserHelper, viewAllUsersHelper

from Class.globalF import globalFuncs
from functools import partial

from threading import Thread


class ViewUsersScreen(MDScreen):
    def __init__(self):
        super(ViewUsersScreen, self).__init__()
        self.name = "USERS"
        self.sm = ScreenManager()

        self.viewAllScreen = Builder.load_string(viewAllUsersHelper)
        self.addUserScreen = Builder.load_string(addUserHelper)
        self.viewUserScreen = Builder.load_string(viewUserHelper)

        self.sm.add_widget(self.viewAllScreen)
        self.sm.add_widget(self.addUserScreen)
        self.sm.add_widget(self.viewUserScreen)

        self.add_widget(self.sm)

        self.on_pre_enter = self.grabUser
        self.on_pre_leave = self.eraseList

        self.val = 2

    def grabUser(self):
        [self.viewAllScreen.ids.listview.add_widget(
            OneLineListItem(
                text="{} {}".format(i.to_dict()["fName"], i.to_dict()["lName"]),
                on_release=partial(self.viewUser, i)
            )
        ) for i in globalFuncs.database.returnUsers()]

    def eraseList(self):  # cba to do this now
        return

    def setAccessLevel(self, name):
        self.ref = name
        globalFuncs.dialog = MDDialog(
            title="Select Access Level",
            type="custom",
            content_cls=Builder.load_string(content),
            auto_dismiss=False,
            buttons=[MDFlatButton(text="Set", on_release=self.dialogFunc)]
        )
        globalFuncs.dialog.open()

        return

    def dialogFunc(self, *args):
        globalFuncs.closeDialog()
        if globalFuncs.dialog.content_cls.ids.one.active == True:
            self.val = 1
            x = "Admin"
        if globalFuncs.dialog.content_cls.ids.two.active == True:
            self.val = 2
            x = "Standard"
        if globalFuncs.dialog.content_cls.ids.three.active == True:
            self.val = 3
            x = "Limited"

        if self.name == "ADDUSER":
            self.addUserScreen.ids.setacc.text = x
        if self.name == "VIEWUSER":
            self.viewUserScreen.ids.setacc.text = x

        return

    def addUser(self):
        self.addUserScreen.ids.spinner.active = True
        data = {
            "fName": self.addUserScreen.ids.fnameEntry.text,
            "lName": self.addUserScreen.ids.lnameEntry.text,
            "email": self.addUserScreen.ids.emailEntry.text,
            "username": self.addUserScreen.ids.usernameEntry.text,
            "password": self.addUserScreen.ids.passwordEntry.text,
            "accessLevel": self.val,
            "practice": globalFuncs.permaSet["practice"]
        }

        for key in data:
            if str(data[key]).replace(" ", "") == "":
                globalFuncs.dialog = MDDialog(
                    title="Error",
                    text="Please fill in all boxes"
                )
                globalFuncs.dialog.open()
                self.addUserScreen.ids.spinner.active = False
                return
        result = globalFuncs.database.fsdb.collection(u"users").add(data)

        # print(globalFuncs.password.checkHash(pw,globalFuncs.database.fsdb.collection(u"users").document(result[1].id).get().to_dict()["password"]))
        self.addUserScreen.ids.spinner.active = False
        return

    def updateUser(self):
        data = {
            "fName": self.viewUserScreen.ids.fnameEntry.text,
            "lName": self.viewUserScreen.ids.lnameEntry.text,
            "email": self.viewUserScreen.ids.emailEntry.text,
            "username": self.viewUserScreen.ids.usernameEntry.text,
            "password": self.viewUserScreen.ids.passwordEntry.text,
            "accessLevel": self.val,
            "practice": globalFuncs.permaSet["practice"]
        }

        globalFuncs.database.fsdb.collection(u"users").document(self.user.id).update(data)

        return

    def viewUser(self, user, *args):
        self.user = user
        self.sm.current = "VIEWUSER"

        x = user.to_dict()

        self.viewUserScreen.ids.fnameEntry.text = x["fName"]
        self.viewUserScreen.ids.lnameEntry.text = x["lName"]
        self.viewUserScreen.ids.emailEntry.text = x["email"]
        self.viewUserScreen.ids.usernameEntry.text = x["username"]
        self.viewUserScreen.ids.passwordEntry.text = x["password"]
        self.val = x["accessLevel"]

        return


content = '''
GridLayout:
    rows:2
    cols:4
    Check:
        id:one
    MDLabel:
        text:"Admin"
    Check
        id:two
        active:True
    MDLabel:
        text:"Standard"
    Check:
        id:three
    MDLabel:
        text:"Limited"
        
     
'''
