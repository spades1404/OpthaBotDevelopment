from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.dialog import MDDialog
from Class.globalF import globalFuncs
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivy.lang.builder import Builder
from functools import partial

from Class.globalF import globalFuncs
from Screens.HELPERS import introScreenHelper, setupExistingHelper, setupNewHelper, setupPracticeHelper, \
    setupAdminAccHelper
from threading import Thread


class SetupScreen(MDScreen):
    def __init__(self):
        super(SetupScreen, self).__init__()
        self.name = "SETUP"
        self.sm = ScreenManager()
        self.add_widget(self.sm)

        self.introScreen = Builder.load_string(introScreenHelper)

        self.setupExisting = Builder.load_string(setupExistingHelper)  # enter practice id here
        self.setupNew = Builder.load_string(setupNewHelper)  # enter org ID here

        self.setupPractice = Builder.load_string(setupPracticeHelper)  # Enter practice details here
        self.setupAdmin = Builder.load_string(setupAdminAccHelper)  # Enter admin account details here

        self.sm.add_widget(self.introScreen)
        self.sm.add_widget(self.setupExisting)
        self.sm.add_widget(self.setupNew)
        self.sm.add_widget(self.setupPractice)
        self.sm.add_widget(self.setupAdmin)

    def switchScreen(self, name, *args):
        self.sm.current = name

        globalFuncs.closeDialog()

    def completeSetup(self, *args):  ##only for setting up an existing practice
        self.parent.current = "LOGIN"

        # saving all the info
        globalFuncs.permaSet["org"] = self.practice.to_dict()["organisation"]
        globalFuncs.permaSet["practice"] = self.practice.id
        globalFuncs.permaSet["firstBoot"] = False
        globalFuncs.jsonSave(globalFuncs.permaSet, globalFuncs.directories.appPermaSets)

        globalFuncs.closeDialog()

    def verifyPracCode(self, code):

        if code.replace(" ", "") == "":
            globalFuncs.dialog = MDDialog(title="Error", text="Please enter a link code").open()
            return
        result = globalFuncs.database.returnPracticeByLink(code)
        if result == []:
            MDDialog(title="No Practice Found", text="Please enter a valid link code").open()
            return

        elif result != []:
            self.practice = result[0]
            globalFuncs.dialog = MDDialog(
                title="Found your practice!",
                text="Is your practice called {}?".format(self.practice.to_dict()["name"]),
                buttons=[
                    MDFlatButton(text="No", on_release=globalFuncs.closeDialog),
                    MDFlatButton(text="Yes", on_release=self.completeSetup)
                ],
                auto_dismiss=False
            )

            globalFuncs.dialog.open()

    def verifyOrgCode(self, code):
        if code.replace(" ", "") == "":
            globalFuncs.dialog = MDDialog(title="Error", text="Please enter a link code").open()
            return

        result = globalFuncs.database.returnOrgByLink(code)
        if result == []:
            MDDialog(title="No Practice Found", text="Please enter a valid link code").open()
            return

        elif result != []:
            self.org = result[0]
            globalFuncs.dialog = MDDialog(
                title="Found your organisation!",
                text="Is your organisation called {}?".format(self.org.to_dict()["name"]),
                buttons=[
                    MDFlatButton(text="No", on_release=globalFuncs.closeDialog),
                    MDFlatButton(text="Yes", on_release=partial(self.switchScreen, "SETUPPRACTICE"))
                ],
                auto_dismiss=False
            )

            globalFuncs.dialog.open()
        return

    def createPractice(self):
        def function():
            self.setupPractice.ids.spinner.active = True
            name = self.setupPractice.ids.pracNameEntry.text
            admin = self.setupPractice.ids.adminNameEntry.text
            email = self.setupPractice.ids.emailEntry.text
            phone = self.setupPractice.ids.phoneEntry.text
            addr = self.setupPractice.ids.addy1Entry.text
            post = self.setupPractice.ids.postcodeEntry.text

            ''' # just a test string here
            name = "specsaver optom"
            admin = "speccies bridgend"
            email = "specsavers@gmail.com"
            phone = "07951308773"
            addr = "anfwibfekjl sdfsdf"
            post = "CF315BG"
            '''

            if name.replace(" ", "") == "" or admin.replace(" ", "") == "" or email.replace(" ",
                                                                                            "") == "" or phone.replace(
                    " ", "") == "" or addr.replace(" ", "") == "" or post.replace(" ", "") == "":
                globalFuncs.dialog = MDDialog(
                    title="Error",
                    text="Please fill out all boxes",
                    buttons=[MDFlatButton(text="Ok", on_release=globalFuncs.closeDialog)],
                    auto_dismiss=False
                )
                globalFuncs.dialog.open()
                self.setupPractice.ids.spinner.active = False
                return

            if globalFuncs.validation.validatePlainString(name.replace(" ", "")) == False:
                globalFuncs.dialog = MDDialog(
                    title="Error",
                    text=" Practice Name is not valid",
                    buttons=[MDFlatButton(text="Ok", on_release=globalFuncs.closeDialog)],
                    auto_dismiss=False
                )
                globalFuncs.dialog.open()
                self.setupPractice.ids.spinner.active = False
                return

            if globalFuncs.validation.validatePlainString(admin.replace(" ", ""), numCheck=True) == False:
                globalFuncs.dialog = MDDialog(
                    title="Error",
                    text="Admin name is not valid, make sure only alphabetic characters are used.",
                    buttons=[MDFlatButton(text="Ok", on_release=globalFuncs.closeDialog)],
                    auto_dismiss=False
                )
                globalFuncs.dialog.open()
                self.setupPractice.ids.spinner.active = False
                return
            '''
            if globalFuncs.validation.checkEmail(email) == False:
                globalFuncs.dialog = MDDialog(
                    title="Error",
                    text="invalid email",
                    buttons=[MDFlatButton(text="Ok",on_release = globalFuncs.closeDialog)],
                    auto_dismiss=False
                )
                globalFuncs.dialog.open()
                self.setupPractice.ids.spinner.active = False
                return
            '''
            '''
            if globalFuncs.validation.validatePlainString(addr.replace(" ","")) == False:
                globalFuncs.dialog = MDDialog(
                    title="Error",
                    text="Address line invalid, only alphanumeric characters can be used",
                    buttons=[MDFlatButton(text="Ok",on_release = globalFuncs.closeDialog)],
                    auto_dismiss=False
                )
                globalFuncs.dialog.open()
                return
            '''

            if globalFuncs.validation.checkPostcode(post.replace(" ", "")) == False:
                globalFuncs.dialog = MDDialog(
                    title="Error",
                    text="Invalid postcode provided, only alphanumeric characters can be used",
                    buttons=[MDFlatButton(text="Ok", on_release=globalFuncs.closeDialog)],
                    auto_dismiss=False
                )
                globalFuncs.dialog.open()
                self.setupPractice.ids.spinner.active = False
                return

            self.setupPractice.ids.spinner.active = False
            self.practice = globalFuncs.database.addNewPractice(name, admin, email, phone, addr, post, self.org.id)

            self.sm.current = "SETUPADMIN"

        Thread(target=function, daemon=True).start()

    def createAdmin(self):
        def function():
            self.setupAdmin.ids.spinner.active = True
            fname = self.setupAdmin.ids.fnameEntry.text
            lname = self.setupAdmin.ids.lnameEntry.text
            email = self.setupAdmin.ids.emailEntry.text
            user = self.setupAdmin.ids.usernameEntry.text
            passw = self.setupAdmin.ids.passwordEntry.text

            if fname.replace(" ", "") == "" or lname.replace(" ", "") == "" or email.replace(" ",
                                                                                             "") == "" or user.replace(
                    " ", "") == "" or passw.replace(" ", "") == "":
                globalFuncs.dialog = MDDialog(
                    title="Error",
                    text="Please fill out all boxes",
                    buttons=[MDFlatButton(text="Ok", on_release=globalFuncs.closeDialog)],
                    auto_dismiss=False
                )
                globalFuncs.dialog.open()
                self.setupAdmin.ids.spinner.active = False
                return
            if globalFuncs.validation.validatePlainString(fname,
                                                          numCheck=True) == False or globalFuncs.validation.validatePlainString(
                    lname, numCheck=True) == False:
                globalFuncs.dialog = MDDialog(
                    title="Error",
                    text=" First or last name is not valid, please make sure only one name is entered",
                    buttons=[MDFlatButton(text="Ok", on_release=globalFuncs.closeDialog)],
                    auto_dismiss=False
                )
                globalFuncs.dialog.open()
                self.setupAdmin.ids.spinner.active = False
                return

            if globalFuncs.validation.checkEmail(email) == False:
                globalFuncs.dialog = MDDialog(
                    title="Error",
                    text="invalid email",
                    buttons=[MDFlatButton(text="Ok", on_release=globalFuncs.closeDialog)],
                    auto_dismiss=False
                )
                globalFuncs.dialog.open()
                self.setupAdmin.ids.spinner.active = False
                return

            if globalFuncs.validation.validatePlainString(user) == False:
                globalFuncs.dialog = MDDialog(
                    title="Error",
                    text="The username is not valid, usernames can only be letters",
                    buttons=[MDFlatButton(text="Ok", on_release=globalFuncs.closeDialog)],
                    auto_dismiss=False
                )
                globalFuncs.dialog.open()

                self.setupAdmin.ids.spinner.active = False

                # saving all the info
                globalFuncs.permaSet["org"] = self.org.id
                globalFuncs.permaSet["practice"] = self.practice.id
                globalFuncs.permaSet["firstBoot"] = False
                globalFuncs.jsonSave(globalFuncs.permaSet, globalFuncs.directories.appPermaSets)
                return
            result = globalFuncs.database.createUser(fname, lname, email, user, passw, 1, self.practice.id)
            self.setupAdmin.ids.spinner.active = False
            self.parent.current = "LOGIN"

        Thread(target=function, daemon=True).start()
