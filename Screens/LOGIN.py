from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from threading import Thread

from Class.globalF import globalFuncs
from Class.user import User
from Screens.HELPERS import loginScreenHelper


# Screen Classes
class LogInScreen(MDScreen):

    def __init__(self, **kwargs):
        super(LogInScreen, self).__init__(**kwargs)
        self.name = "LOGIN"
        self.content = Builder.load_string(loginScreenHelper)
        self.add_widget(self.content)

    def login(self):

        def function():
            self.content.ids.spinner.active = True
            result = globalFuncs.database.signIn(self.content.ids.userEntry.text, self.content.ids.passEntry.text)
            if result != None:
                globalFuncs.currentUser = User(result)
                self.parent.current = "PRIMARY"
                self.parent.current_screen.content.ids.navBarSubtitle.text = "{} {}".format(globalFuncs.currentUser.fname,globalFuncs.currentUser.lname)
            else:
                print("Failed")
                self.logInFailed()

            self.content.ids.spinner.active = False

        def bypassLogin():  # FOR DEV PURPOSE
            self.parent.current = "PRIMARY"


        Thread(target=bypassLogin, daemon=True).start() #bypasses login for us
        #Thread(target=function, daemon=True).start()

    def logInFailed(self):
        self.content.ids.userEntry.error = True
        self.content.ids.passEntry.error = True
