from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty
from kivymd.uix.picker import MDDatePicker

from Screens.HELPERS import addUserHelper
from Class.globalF import globalFuncs
from threading import Thread

class AddUserScreen(MDScreen):
    def __init__(self):
        super(AddUserScreen, self).__init__()
        self.content = Builder.load_string(addUserHelper)
        self.add_widget(self.content)
        self.name = "adduser"

    def addUser(self):
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

            def validate():
                f = [fname, lname, email, id, postcode, phone, addy]
                for i in [i.replace(" ", "") for i in f]:
                    if i == "":
                        return "Not all fields filled"

                if globalFuncs.validation.validatePlainString(fname,numCheck=True) == False or globalFuncs.validation.validatePlainString(lname, numCheck=True) == False:
                    return "Name must not have numbers"

                if globalFuncs.validation.checkEmail(email) == False and globalFuncs.appSettings["Always verify emails"] == True:
                    return "Invalid Email"

                if globalFuncs.validation.validatePlainString(id) ==False:
                    return "ID is not a valid string"

                if globalFuncs.validation.checkNumber(phone) == False and globalFuncs.appSettings["Always check phone numbers"] == True:
                    return "Invalid Number"

                if globalFuncs.validation.checkDate(dob) == False:
                    return "Invalid Date"

                #if globalFuncs.validation.validatePlainString(addy) == False:
                #    return "Address is not a valid string"

                if globalFuncs.validation.checkPostcode(postcode) == False:
                    return "Postcode is not valid"

                return True

            result = validate()
            if result != True:
                MDDialog(title="Error",text=result).open()
                self.content.ids.spinner.active = False
                return

            result = globalFuncs.database.addNewPX(fname, lname, email, id, postcode, phone, addy, dob)
            self.content.ids.infoLabel.text = "Done!"
            self.content.ids.spinner.active = False
            return
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