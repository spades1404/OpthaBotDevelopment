#THIS SCREEN IS TO VIEW A SINGLE SCAN

from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from Screens.HELPERS import viewScanHelper
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock


class ViewScanScreen(MDScreen):
    def __init__(self):
        super(ViewScanScreen, self).__init__()
        self.name = "VIEWSCAN"
        self.content = Builder.load_string(viewScanHelper)
        self.add_widget(self.content)

        Clock.schedule_once(self.initDropDown)


        return

    def initDropDown(self,interval):
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
            position="bottom",
            width_mult=4,
        )
        self.menu.bind(on_release=self.set_item)

    def insertScan(self,scan):
        self.content.ids.results.text = scan.generateDescription()
        self.content.ids.orgid.text = scan.custID
        self.content.ids.image.source = scan.postProcessDir
        self.content.ids.updateButt.on_release = lambda:scan.updateDetails(self.content.ids.orgid.text,self.content.ids.field.text)
        self.content.ids.deleteButt.on_release = lambda:self.deleteScan(scan)
        return

    def deleteScan(self,scan):
        scan.dbobj.reference.delete()
        self.content.ids.field.text = "DELETED"
        self.content.ids.orgid.text = "DELETED"
        self.content.ids.updateButt.on_release = self.dud
        self.content.ids.deleteButt.on_release = self.dud
        print("done")


    def insertScanLoadImage(self,scan):
        self.content.ids.results.text = scan.generateDescription()
        self.content.ids.orgid.text = scan.custID
        scan.grabImage()
        self.content.ids.image.source = scan.postProcessDir
        self.content.ids.updateButt.on_release = lambda: scan.updateDetails(self.content.ids.orgid.text)
        self.content.ids.deleteButt.on_release = lambda: self.deleteScan(scan)


    def set_item(self, instance_menu, instance_menu_item):
        print(instance_menu,instance_menu_item)
        def set_item(interval):
            self.content.ids.field.text = instance_menu_item.text
            instance_menu.dismiss()
            self.menu.dismiss()
        Clock.schedule_once(set_item, 0.5)

    def dud(self):
        print(":(")
