from kivymd.uix.dialog import MDDialog
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDFlatButton
from kivy.metrics import dp

#THIS CODE IS NO LONGER USED, WILL BE DELETED SOON

class scanDialog(MDDialog):
    def __init__(self,scan):
        super(scanDialog, self).__init__()
        self.title = "Scan Details"

        details = scan.resultList
        for i in details:
            f = i[1] * 100
            i[1] = "{}%".format(str(f))

        self.buttons = [
            MDFlatButton(text="Close",on_release = self.dismiss),
            MDFlatButton(text="Link Record"),
            MDFlatButton(text="Update")
        ]
        self.add_widget(MDDataTable(
            column_data = [
                ("Diagnosis",dp(30)),
                ("Certainty",dp(30))
            ],
            row_data = [
                ("guh","guh")
            ]
        ))

        #self.add_widget()