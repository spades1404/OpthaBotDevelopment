from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import ThreeLineAvatarIconListItem,OneLineListItem,IconLeftWidget
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from Class.globalF import globalFuncs
from Class.scan import Scan

from Screens.HELPERS import homeContentHelper

from threading import Thread


class HomeScreen(MDScreen):
    def __init__(self):
        super(HomeScreen, self).__init__()
        self.name = "HOME"
        self.content = Builder.load_string(homeContentHelper)
        self.content.ids.currentImage.source = globalFuncs.directories.emptyImageIcon
        self.add_widget(self.content)

        self.firstScan = OneLineListItem(text="Nothing Here Yet... Try Upload an Image!")
        self.content.ids.listView.add_widget(self.firstScan)

        return

    def addScanToListView(self,scan):
        if self.firstScan != True:
            self.content.ids.listView.remove_widget(self.firstScan)
            self.firstScan=True
        item = ThreeLineAvatarIconListItem(
            text = "Scan {}".format(scan.scanTime.strftime("%H:%M:%S")),
            secondary_text = "{}% Certainty of {}".format(int(scan.resultList[0][1]*100),scan.resultList[0][0]),
            tertiary_text = "Click To View Full Results"

        )
        item.on_release = lambda:self.displayScanPopup(scan)
        item.add_widget(IconLeftWidget(icon = scan.postProcessDir))

        self.content.ids.listView.add_widget(item)
        return

    def displayScanPopup(self,scan=None):
        dialog = MDDialog(
            title = "Scan Results",
            text = scan.generateDescription(),
            buttons=[
                MDFlatButton(text="Close"),
                MDFlatButton(text="Link Record"),
                MDFlatButton(text="Update")
            ]
        )
        dialog.open()
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
                    text="No ID entered",
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
                    scan = Scan(filename)
                    scan.generateTemp()
                    self.content.ids.currentImage.source = scan.postProcessDir


                    if (self.content.ids.pxidField.text).replace(" ", "") == "":
                        scan.custID = self.content.ids.pxidField.text

                    self.updateInfoText("Analyzing Image")
                    scan.analyze()
                    self.addScanToListView(scan)
                    self.updateInfoText("Image Processed Successfully")

                    if globalFuncs.appSettings["Automatically Upload Scans"] == True:
                        globalFuncs.database.uploadScan(scan)
                    self.updateInfoText("Uploading Scan To Server")
                    self.updateInfoText("Done!")
                except:
                    self.updateInfoText("Image not compatible")

            globalFuncs.exit_event.set()
            self.content.ids.progressBar.value = 100


        Thread(target=function, daemon=True).start()

        return


