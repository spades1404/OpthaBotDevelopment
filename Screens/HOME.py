from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import ThreeLineAvatarIconListItem,OneLineListItem,IconLeftWidget
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager
from functools import partial


from Class.globalF import globalFuncs
from Class.scan import Scan

from Screens.HELPERS import homeContentHelper
from Screens.VIEWSCAN import ViewScanScreen


from threading import Thread


class HomeScreen(MDScreen):
    def __init__(self):
        super(HomeScreen, self).__init__()
        self.name = "HOME"
        self.sm = ScreenManager()

        self.content = Builder.load_string(homeContentHelper)
        self.content.ids.currentImage.source = globalFuncs.directories.emptyImageIcon
        self.viewScanScreen = ViewScanScreen()
        self.viewScanScreen.content.ids.back.on_release = partial(self.switchScreen, "home")

        self.sm.add_widget(self.content)
        self.sm.add_widget(self.viewScanScreen)
        self.add_widget(self.sm)

        self.firstScan = OneLineListItem(text="Nothing Here Yet... Try Upload an Image!")
        self.content.ids.listView.add_widget(self.firstScan)

        self.listItems = []
        self.on_pre_enter = self.refreshView
        self.on_enter = self.refreshView

        return

    def refreshView(self):
        for i in self.listItems:
            if i[1].custID == "DELETED":
                try:
                    self.content.ids.listView.remove_widget(i[0])
                except:
                    pass

    def addScanToListView(self, scan, *args):
        if self.firstScan != True:
            self.content.ids.listView.remove_widget(self.firstScan)
            self.firstScan = True
        item = ThreeLineAvatarIconListItem(
            text="Scan {}".format(scan.scanTime.strftime("%H:%M:%S")),
            secondary_text="{}% Certainty of {}".format(int(scan.resultList[0][1] * 100), scan.resultList[0][0]),
            tertiary_text="Click To View Full Results",
            on_release=partial(self.showScan, scan)

        )
        item.add_widget(IconLeftWidget(icon=scan.postProcessDir))
        self.listItems.append([item, scan])

        self.content.ids.listView.add_widget(item)
        return

    def switchScreen(self,name):
        self.sm.current = name
        self.parent.current = "HOME"

    def showScan(self,scan,*args):
        self.switchScreen("VIEWSCAN")
        self.viewScanScreen.insertScan(scan)
        return

    def updateInfoText(self,text):
        self.content.ids.infoText.text = text

    def select(self, ob=None):  # select file
        def function():
            self.updateInfoText("File Selection")
            filename = globalFuncs.askforafile()
            Thread(target=globalFuncs.updateProgressBar, args=([0, 80], 0.1, self.content.ids.progressBar,), daemon=True).start()

            self.updateInfoText("File Found! - Testing")

            if bool(globalFuncs.appSettings["Require Customer ID's on Scan"]) == True and (self.content.ids.pxidField.text).replace(" ", "") == "":
                MDDialog(
                    title="Error",
                    text="No ID Has been entered, please enter one and retry",
                ).open()
                globalFuncs.exit_event.set()
                self.content.ids.progressBar.value = 100
                self.updateInfoText("Scan Aborted - No ID entered")

                return

            if globalFuncs.validation.checkImage(filename) == False:
                self.updateInfoText("File is not an image - aborted")
                globalFuncs.exit_event.set()
                return


            else:
                try:
                    scan = Scan().initialiseFromProg(filename)
                    scan.generateTemp()
                    self.content.ids.currentImage.source = scan.postProcessDir

                    if self.content.ids.pxidField.text.replace(" ", "") != "":
                        scan.custID = self.content.ids.pxidField.text
                        print("added")

                    self.updateInfoText("Analyzing Image")
                    scan.analyze()
                    self.addScanToListView(scan)
                    self.updateInfoText("Image Processed Successfully")

                    # if globalFuncs.appSettings["Automatically Upload Scans"] == True:
                    #    globalFuncs.database.uploadScan(scan)
                    self.updateInfoText("Uploading Scan To Server")
                    globalFuncs.database.uploadScan(scan)
                    self.updateInfoText("Done!")
                except Exception as e:
                    print(e)
                    self.updateInfoText("Image not compatible")

            globalFuncs.exit_event.set()
            self.content.ids.progressBar.value = 100


        Thread(target=function, daemon=True).start()

        return
