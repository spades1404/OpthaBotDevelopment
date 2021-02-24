from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.card import MDCard
from kivy.uix.image import AsyncImage
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from Class.scan import Scan
from Class.globalF import globalFuncs
from Screens.HELPERS import viewPXHelper
from functools import partial


class ViewPXScreen(MDScreen):
    def __init__(self):
        super(ViewPXScreen, self).__init__()
        self.name = "viewuser"

        self.content = Builder.load_string(viewPXHelper)
        self.listContent = []
        self.add_widget(self.content)

    def insertUser(self, user):
        self.user = user
        self.content.ids.fNameEntry.text = user.fname
        self.content.ids.lNameEntry.text = user.lname
        self.content.ids.emailEntry.text = user.email
        self.content.ids.phoneEntry.text = user.phoneNum
        self.content.ids.addy1Entry.text = user.addressLine
        self.content.ids.postcodeEntry.text = user.postcode
        self.content.ids.dateEntry.ids.dateEntry.text = user.dob
        self.content.ids.orgIDEntry.ids.numEntry.text = user.orgID

        # remove previous scans
        [self.content.ids.listview.remove_widget(i) for i in self.listContent]

        scans = [Scan().initialiseFromDB(i) for i in globalFuncs.database.returnScansFromUser(user.orgID)]
        self.listContent = []
        for i in scans:
            card = ScanCard(i)
            card.on_release = partial(self.showScan, i)
            self.listContent.append(card)
            self.content.ids.listview.add_widget(card)
            card.delButt.on_release = partial(self.deleteScan, card)

        return

    def deleteScan(self, card):
        card.scan.dbobj.reference.delete()
        self.listContent.remove(card)
        self.content.ids.listview.remove_widget(card)

    def showScan(self, scan, *args):
        self.parent.current = "VIEWSCAN"
        self.parent.current_screen.insertScan(scan)

    def updateUserDetails(self, *args):
        result = self.user.updatePXdetails(
            self.content.ids.fNameEntry.text,
            self.content.ids.lNameEntry.text,
            self.content.ids.emailEntry.text,
            self.content.ids.orgIDEntry.ids.numEntry.text,
            self.content.ids.postcodeEntry.text,
            self.content.ids.phoneEntry.text,
            self.content.ids.addy1Entry.text,
            self.content.ids.dateEntry.ids.dateEntry.text
        )
        print(result)
        return

    def setDate(self, date):
        self.content.ids.dateEntry.ids.dateEntry.text = date.strftime("%d/%m/%Y")
        return

    def autoGenID(self):
        self.content.ids.orgIDEntry.ids.numEntry.text = globalFuncs.database.generateNewIDFromDB("orgID", u"patients")

    def selectCalendar(self):
        date_dialog = MDDatePicker(callback=self.setDate)
        date_dialog.open()
        return



class ScanCard(MDCard):
    def __init__(self, scan):
        super(ScanCard, self).__init__()
        self.scan = scan
        self.orientation = "horizontal"
        self.spacing = 15
        self.md_bg_color = (216 / 255, 216 / 255, 216 / 255, 1)
        self.size_hint_x = None
        self.padding = 10
        self.width = 250
        self.elevation = 10

        try:
            print(scan.postProcessDir)
        except:
            scan.grabImage()
        self.add_widget(AsyncImage(source=scan.postProcessDir, size_hint_x=None, width=60))

        self.layout = MDBoxLayout(orientation="vertical", spacing=5)
        self.layout.add_widget(MDLabel(text="Taken {}".format(scan.scanTime.strftime("%d/%m/%Y"))))
        self.delButt = MDIconButton(icon="delete")
        self.layout.add_widget(self.delButt)
        self.add_widget(self.layout)
