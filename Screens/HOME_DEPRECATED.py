from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineListItem, MDList,ThreeLineAvatarIconListItem, ImageLeftWidget
from kivymd.uix.list import IconLeftWidget
from kivymd.uix.button import MDTextButton, MDFillRoundFlatIconButton
from kivy.uix.image import AsyncImage
from Class.globalF import globalFuncs
from threading import Thread
from Class.scan import Scan
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.textfield import MDTextField
from Screens.HELPERS import homeContentHelper
from kivy.clock import Clock

#THIS CODE IS NO LONGER USED, WILL BE DELETED SOON

class HomeContent(Screen):
    def __init__(self, **kwargs):
        super(HomeContent, self).__init__(**kwargs)
        self.name = "PRIMARYHOME"

        self.layout1 = BoxLayout(orientation="horizontal", padding=10)
        self.layout2 = BoxLayout(orientation="vertical", padding=15)
        self.layout2.add_widget(MDLabel(text="Current Image", font_style="Subtitle2", size_hint_y=None, height=20))
        self.currentImage = AsyncImage()
        self.currentImage.source = globalFuncs.directories.emptyImageIcon
        self.layout2.add_widget(self.currentImage)

        #anchor = AnchorLayout(anchor_x = "center", anchor_y="bottom",size_hint_y = None, height= 10)
        anchor = BoxLayout(orientation="horizontal",padding = 15,size_hint_y = None, height = 15)
        anchor.add_widget(MDFillRoundFlatIconButton(icon="cloud-upload", on_release=self.select, text="Upload Image"))
        self.pxIDField = MDTextField()
        self.pxIDField.hint_text = "Patient ID"
        anchor.add_widget(self.pxIDField)
        self.layout2.add_widget(anchor)
        self.progressBar = MDProgressBar(value=0, size_hint_y=None, height=15)
        self.infoText = MDLabel(text="Awaiting a Scan", size_hint_y=None, height=10, halign="center",font_style="Overline")
        self.layout2.add_widget(self.progressBar)
        self.layout2.add_widget(self.infoText)
        self.layout1.add_widget(self.layout2)

        self.layout3 = BoxLayout(orientation="vertical", padding=10, spacing=5)
        self.layout3.add_widget(MDLabel(text="Recent Results", font_style="Subtitle2", size_hint_y=None, height=20))
        self.scroll = ScrollView()
        self.listView = MDList()
        self.scroll.add_widget(self.listView)
        self.layout3.add_widget(self.scroll)
        self.layout1.add_widget(self.layout3)

        self.add_widget(self.layout1)
        # self.testListView()

    def testListView(self):
        for i in range(20):
            icon = IconLeftWidget(icon="android")
            item = OneLineListItem(text="Hello world{}".format(str(i)))
            item.add_widget(icon)
            self.listView.add_widget(item)

    def addScanToListView(self, scan):
        item = ThreeLineAvatarIconListItem()
        image = IconLeftWidget(icon = scan.postProcessDir)
        item.add_widget(image)
        item.text = "Scan {}".format(scan.scanTime.strftime("%H:%M:%S"))
        item.secondary_text = "{}% Certainty of {}".format(int(scan.resultList[0][1])*100,scan.resultList[0][0])
        item.tertiary_text = "Click To View Full Results"
        item.on_release = self.displayScanPopup
        self.listView.add_widget(item,index=0)
        return

    def displayScanPopup(self,scan):
        print("guh")
        return

    def threaded(self, func=None):
        try:
            Thread(target=func, daemon=True).start()
        except Exception as e:
            print(e)

    def select(self, ob=None):  # select file
        def function():
            self.infoText.text = "File Selection"
            filename = globalFuncs.askforafile()
            Thread(target=globalFuncs.updateProgressBar, args=([0, 80], 0.1, self.progressBar,), daemon=True).start()
            self.infoText.text = "File Found! - Testing"
            if globalFuncs.validation.checkImage(filename) == False:
                self.infoText.text = "File is not an image - aborted"
                print("Failed")
            else:
                scan = Scan(filename)
                self.currentImage.source = scan.generateTemp()
                self.infoText.text = "Analyzing Image"
                scan.analyze()
                print(scan.result)
                self.addScanToListView(scan)
                self.infoText.text = "Image Processed Successfully!"
                globalFuncs.exit_event.set()

            globalFuncs.exit_event.set()
            self.progressBar.value = 100

        Thread(target=function, daemon=True).start()

        return