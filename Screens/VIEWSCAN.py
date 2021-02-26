#THIS SCREEN IS TO VIEW A SINGLE SCAN

from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from Screens.HELPERS import viewScanHelper
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from functools import partial

from Class.scan import Scan

class ViewScanScreen(MDScreen):
    def __init__(self):
        super(ViewScanScreen, self).__init__()
        self.name = "VIEWSCAN"
        self.content = Builder.load_string(viewScanHelper)
        self.add_widget(self.content)
        self.scan = Scan()

        # Clock.schedule_once(self.initDropDown)

        self.on_pre_enter = self.configure

        return

    def configure(self):
        self.content.ids.updateButt.on_release = self.updateDetail
        self.content.ids.deleteButt.on_release = self.deleteScan

    def updateDetail(self):
        print(0)
        self.scan.updateDetails(self.content.ids.orgid.text, self.content.ids.field.text)

    def initDropDown(self, interval):
        menuItems = [
            {"text": "Normal"},
            {"text": "Diabetic Retinopathy"},
            {"text": "Glaucoma"},
            {"text": "Cataracts"},
            {"text": "Age Related Macular Degeneration"},
            {"text": "Hypertension"},
            {"text": "Myopia"},
            {"text": "Other Abnormalities"},
        ]
        self.menu = MDDropdownMenu(
            caller=self.content.ids.field,
            items=menuItems,
            width_mult=4,

        )
        self.menu.bind(on_release=self.set_item)

    def insertScan(self, scan, *args):
        self.scan = scan

        self.content.ids.results.text = scan.generateDescription()
        self.content.ids.orgid.text = scan.details["custID"]
        self.content.ids.field.text = scan.details["diagnosis"]
        self.content.ids.image.source = scan.postProcessDir
        return

    def deleteScan(self, *args):
        scan = self.scan
        scan.dbobj.reference.delete()
        self.content.ids.field.text = "DELETED"
        self.content.ids.orgid.text = "DELETED"
        scan.custID = "DELETED"
        self.content.ids.updateButt.on_release = self.dud
        self.content.ids.deleteButt.on_release = self.dud

        print("done")


    def insertScanLoadImage(self,scan):
        self.scan = scan
        self.content.ids.results.text = scan.generateDescription()
        self.content.ids.orgid.text = scan.details["custID"]
        self.content.ids.field.text = scan.details["diagnosis"]
        scan.grabImage()
        self.content.ids.image.source = scan.postProcessDir

        print(scan.details)

    def set_item(self, instance_menu, instance_menu_item):
        def set_item(interval):
            self.content.ids.field.text = instance_menu_item.text
            instance_menu.dismiss()
            print(instance_menu_item.text)
            self.content.ids.field.text = instance_menu_item.text
        Clock.schedule_once(set_item, 0.5)

    def dud(self):
        print("Ah mate hate to be brisk with ya but that aint gonna work the second time around")
