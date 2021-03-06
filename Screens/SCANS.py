from functools import partial

from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget, IconRightWidget
from kivymd.uix.screen import MDScreen

from Class.globalF import globalFuncs
from Class.scan import Scan
from Screens.HELPERS import viewScansHelper
from Screens.VIEWSCAN import ViewScanScreen


class ScanListViewScreen(MDScreen):
    def __init__(self):
        super(ScanListViewScreen, self).__init__()
        self.name = "LISTSCAN"
        self.sm = ScreenManager()

        self.content = Builder.load_string(viewScansHelper)
        self.viewScanScreen = ViewScanScreen()
        self.viewScanScreen.content.ids.back.on_release = partial(self.switchScreen, "listview")

        self.sm.add_widget(self.content)
        self.sm.add_widget(self.viewScanScreen)
        self.add_widget(self.sm)
        self.currentListItems = []
        self.loadScans()

        self.on_pre_enter = self.loadScans

    def switchScreen(self, name):
        self.sm.current = name

    def loadScans(self):
        filter = 1

        if self.content.ids.day.active == True:
            filter = 1
        elif self.content.ids.week.active == True:
            filter = 2
        elif self.content.ids.month.active == True:
            filter = 3

        relevant = globalFuncs.database.returnRecentScans(filter)
        converted = []
        for i in relevant:
            converted.append(Scan().initialiseFromDB(i))
        print(len(relevant))

        #clear list
        [self.content.ids.listview.remove_widget(i) for i in self.currentListItems]

        #add new items
        for scan in converted:
            item = ThreeLineAvatarIconListItem(
                text="Scan {}".format(scan.scanTime.strftime("%H:%M:%S")),
                secondary_text="{}% Certainty of {}".format(int(scan.resultList[0][1] * 100), scan.resultList[0][0]),
                tertiary_text="Patient ID: {}".format(scan.custID),
                on_release= partial(self.showScan, scan)
            )
            item.add_widget(IconLeftWidget(icon = "camera"))
            item.add_widget(IconRightWidget(icon = "delete",on_release = partial(self.deleteScan,scan,item)))
            self.content.ids.listview.add_widget(item)
            self.currentListItems.append(item)
        return

    def deleteScan(self,scan,listitem,*args):
        self.currentListItems.remove(listitem)
        self.content.ids.listview.remove_widget(listitem)
        globalFuncs.database.fsdb.collection(u"images").document(scan.dbobj.id).delete()
    def showScan(self,scan,*args):
        self.switchScreen("VIEWSCAN")
        self.viewScanScreen.insertScanLoadImage(scan)



