from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivy.uix.scrollview import ScrollView
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dropdownitem import MDDropDownItem


class SomeScreen(Screen):
    def __init__(self, **kwargs):
        super(SomeScreen, self).__init__(**kwargs)

        self.grid = MDGridLayout(
            cols=1,
            padding=150,
            spacing=50,
            size_hint=(1, None),
            width=900
        )

        self.grid.bind(
            minimum_height=self.grid.setter('height')
        )

        self.ScrollviewLayout = ScrollView(
            bar_width=10,
            size_hint=(1, 0.95),
            size=(900, 620),
            pos_hint={'center_x': .5, 'center_y': .4},
            do_scroll_x=False
        )

        self.createMenuButtons()
        self.ScrollviewLayout.add_widget(self.grid)
        self.add_widget(self.ScrollviewLayout)

    def createMenuButtons(self):
        self.button1 = MDRectangleFlatButton()
        self.button1.text = "Button1"
        self.button1.font_size = 15
        self.button1.size = (480, 50)
        self.button1.size_hint = (1, None)
        self.button1.halign = 'center'
        self.button1.valign = 'middle'

        self.button2 = MDRectangleFlatButton()
        self.button2.text = "Button2"
        self.button2.font_size = 15
        self.button2.size = (480, 50)
        self.button2.size_hint = (1, None)
        self.button2.halign = 'center'
        self.button2.valign = 'middle'

        items1 = [{"icon": "git", "text": f"{thing}"} for thing in ["Stuff", "More Stuff"]]
        menu1 = MDDropdownMenu(
            caller=self.button1, items=items1,
            width_mult=4,
        )

        items2 = [{"icon": "git", "text": f"{thing}"} for thing in ["Stuff", "More Stuff"]]
        menu2 = MDDropdownMenu(
            caller=self.button2, items=items2,
            width_mult=4,
        )

        self.button1.on_press = menu1.open
        self.button2.on_press = menu2.open

        bl = BoxLayout()
        bl.spacing = 10

        bl.add_widget(self.button1)
        bl.add_widget(self.button2)
        self.grid.add_widget(bl)


class TestApp(MDApp):
    def build(self):
        return SomeScreen()


TestApp().run()