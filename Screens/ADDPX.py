from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.button import MDFlatButton

from Screens.HELPERS import addPXHelper
from Class.globalF import globalFuncs
from threading import Thread
from functools import partial

class AddPXScreen(MDScreen):
    def __init__(self):
        super(AddPXScreen, self).__init__()
        self.content = Builder.load_string(addPXHelper)
        self.add_widget(self.content)
        self.name = "adduser"

    def addPX(self):
        def function():
            self.content.ids.spinner.active = True

            fname = (self.content.ids.fNameEntry.text).replace(" ", "")
            lname = (self.content.ids.lNameEntry.text).replace(" ", "")
            id = (self.content.ids.orgIDEntry.ids.numEntry.text).replace(" ", "")
            email = (self.content.ids.emailEntry.text).replace(" ", "")
            phone = (self.content.ids.phoneEntry.text).replace(" ", "")
            addy = (self.content.ids.addy1Entry.text).replace(" ", "")
            postcode = (self.content.ids.postcodeEntry.text).replace(" ", "")
            dob = (self.content.ids.dateEntry.ids.dateEntry.text).replace(" ", "")

            f = [fname, lname, email, id, postcode, phone, addy]
            c = 0
            for i in f:
                if i.replace(" ", "") == "":
                    c += 1

            if c > 0:
                globalFuncs.dialog = MDDialog(
                    title="Would you like to continue?",
                    text="There are missing fields, would you like to continue anyways?",
                    buttons=[
                        MDFlatButton(text="Yes"),
                        MDFlatButton(text="No")
                    ],
                    auto_dismiss=False
                )
                globalFuncs.dialog.buttons[0].on_release = partial(execute, fname, lname, email, id, postcode, phone,
                                                                   addy, dob)
                globalFuncs.dialog.buttons[1].on_release = globalFuncs.dialog.dismiss

                globalFuncs.dialog.open()
                self.content.ids.spinner.active = False
            return

        def execute(fname, lname, email, id, postcode, phone, addy, dob, *args):
            self.content.ids.spinner.active = True
            globalFuncs.dialog.dismiss()
            if globalFuncs.validation.validatePlainString(fname, numCheck=True) == False and fname.replace(" ",
                                                                                                           "") != "" or globalFuncs.validation.validatePlainString(
                    lname, numCheck=True) == False and lname.replace(" ", "") != "":
                globalFuncs.dialog = MDDialog(
                    title="Error",
                    text="The names entered are not valid",
                    buttons=[MDFlatButton(text="Try Again", on_release=globalFuncs.dialog.dismiss)]
                )
                globalFuncs.dialog.open()
                self.content.ids.spinner.active = False
                return

            if globalFuncs.validation.checkEmail(email) == False and globalFuncs.appSettings[
                "Always verify emails"] == True and email.replace(" ", "") != "":
                globalFuncs.dialog = MDDialog(
                    title="Error",
                    text="The email entered is not valid",
                    buttons=[MDFlatButton(text="Try Again", on_release=globalFuncs.dialog.dismiss)]
                )
                globalFuncs.dialog.show()
                self.content.ids.spinner.active = False
                return

            if globalFuncs.validation.validatePlainString(id) == False:
                globalFuncs.dialog = MDDialog(
                    title="Error",
                    text="The ID entered is not valid, an ID is a required field",
                    buttons=[MDFlatButton(text="Try Again", on_release=globalFuncs.dialog.dismiss)]
                )
                globalFuncs.dialog.open()
                self.content.ids.spinner.active = False
                return

            if globalFuncs.validation.checkNumber(phone) == False and globalFuncs.appSettings[
                "Always check phone numbers"] == True and phone.replace(" ", "") != "":
                globalFuncs.dialog = MDDialog(
                    title="Error",
                    text="The number entered is not valid",
                    buttons=[MDFlatButton(text="Try Again", on_release=globalFuncs.dialog.dismiss)]
                )
                globalFuncs.dialog.open()
                self.content.ids.spinner.active = False
                return

            if globalFuncs.validation.checkDate(dob) == False and dob.replace(" ", "") != "":
                globalFuncs.dialog = MDDialog(
                    title="Error",
                    text="The date of birth entered is not valid",
                    buttons=[MDFlatButton(text="Try Again", on_release=globalFuncs.dialog.dismiss)]
                )
                globalFuncs.dialog.open()
                self.content.ids.spinner.active = False
                return

            # if globalFuncs.validation.validatePlainString(addy) == False:
            #    return "Address is not a valid string"

            if globalFuncs.validation.checkPostcode(postcode) == False and postcode.replace(" ", "") != "":
                globalFuncs.dialog = MDDialog(
                    title="Error",
                    text="The postcode entered is not valid",
                    buttons=[MDFlatButton(text="Try Again", on_release=globalFuncs.dialog.dismiss)]
                )
                globalFuncs.dialog.open()
                self.content.ids.spinner.active = False
                return
            result = globalFuncs.database.addNewPX(fname, lname, email, id, postcode, phone, addy, dob)
            self.content.ids.infoLabel.text = "Done!"
            self.content.ids.spinner.active = False

        Thread(target=function, daemon=True).start()

    def setDate(self, date):
        self.content.ids.dateEntry.ids.dateEntry.text = date.strftime("%d/%m/%Y")
        return

    def autoGenID(self):
        self.content.ids.orgIDEntry.ids.numEntry.text = globalFuncs.database.generateNewIDFromDB("orgID", u"patients")

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