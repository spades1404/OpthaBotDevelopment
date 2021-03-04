homeContentHelper = '''
Screen:
    name: "home"
    BoxLayout:
        orientation: "horizontal"
        padding: 10

        BoxLayout:
            orientation: "vertical"
            padding: 15
            spacing:10

            MDLabel:
                text: "Current Image"
                font_style: "H5"
                size_hint_y: None
                height: 20
            
            MDSeparator:
            
            AsyncImage:
                id: currentImage
                
            BoxLayout:
                orientation: "horizontal"
                spacing: 10
                size_hint_y: None
                height:15
                MDFillRoundFlatIconButton:
                    id: uploadButton
                    icon: "cloud-upload"
                    text: "Upload Image"
                    on_release: app.primaryScreen.homeScreen.select()
                    
                MDTextField:
                    id: pxidField
                    hint_text: "Patient ID"
                    text:
            
            MDProgressBar:
                id: progressBar
                value: 0
                size_hint_y: None
                height: 15
                
            MDLabel:
                id: infoText
                text: "Awaiting a Scan"
                size_hint_y: None
                height: 10
                halign: "center"
                font_style: "Overline"

        BoxLayout:
            orientation: "vertical"
            padding: 15
            spacing:10
            MDLabel:
                text: "Recent Results"
                font_style: "H5"
                size_hint_y: None
                height: 20
                
            MDSeparator:
            
            ScrollView:
                MDList:
                    id: listView
'''

primaryScreenHelper = '''
Screen:
    ScreenManager:
        Screen:
            BoxLayout:
                orientation: "vertical" 
                MDToolbar:
                    id:toolbar
                    title: "OpthaBot"
                    elevation: 10
                    left_action_items: [["menu", lambda x: navDraw.set_state("toggle")]]
                    
                    
                ScreenManager:
                    id: primaryScreenManager
    
    MDNavigationDrawer:
        id: navDraw
        orientation: "vertical"
        padding: 10
        spacing: 15
    
        AnchorLayout:
            anchor_x: "left"
            size_hint_y: None
            height: avatar.height
    
            Image:
                id: avatar
                size_hint: None, None
                size: "72dp", "72dp"
                source: "Assets\icon.png"
    
        MDLabel:
            id: navBarTitle
            text: "OpthaBot - Development"
            font_style: "Button"
            size_hint_y: None
            height: self.texture_size[1]
    
        MDLabel:
            id: navBarSubtitle
            text: "Developer Mode"
            font_style: "Caption"
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            
        ScrollView:
            MDList:
                id:listMenu
                
                
                OneLineIconListItem:
                    text: "Exit"
                    on_release: 
                        app.stop()
                    IconLeftWidget:
                        icon: "power-plug-off"
                        
                        
    
        
'''

loginScreenHelper = '''
Screen:
        
    MDLabel:
        text:"Welcome to Opthabot!"
        pos_hint: {"center_x":0.5,"center_y":0.65}
        halign: "center"
        font_style: "H3"
    
    MDTextField:
        id: userEntry
        hint_text: "Enter your username"
        icon_right: "face-profile"
        size_hint_x:None
        width: 300
        pos_hint: {"center_x":0.5,"center_y":0.5}
        helper_text: "Invalid Details"
        helper_text_mode: "on_error"
        error: False
        
    MDTextField:
        id: passEntry
        hint_text: "Enter your password"
        icon_right: "account-key"
        size_hint_x:None
        width: 300
        password: True
        pos_hint: {"center_x":0.5,"center_y":0.4}
        helper_text: "Invalid Details"
        helper_text_mode: "on_error"
        error: False
        
    MDRectangleFlatIconButton:
        icon: "login"
        text: "      Login"
        pos_hint: {"center_x":0.5,"center_y":0.3}
        on_release: app.loginScreen.login()
        
    MDSpinner:
        active:False
        id: spinner
        size_hint: None, None
        size: dp(32),dp(32)
        pos_hint: {"center_x":0.5,"center_y":0.2}
        
        
'''

searchScreenHelper = '''

<DateSelector@RelativeLayout>:
    size_hint_y: None
    height: dateEntry.height

    MDTextField:
        id: dateEntry
        hint_text: "Date"
        text: ""
        mode: "rectangle"
        color_active: app.theme_cls.primary_light
        helper_text: "Enter date in dd/mm/yyyy format"
        helper_mode: "persistent"
        
       
    MDIconButton:
        icon: "calendar"
        ripple_scale: .5
        pos_hint: {"center_y": .5}
        pos: dateEntry.width - self.width + dp(8), 0
        on_release: app.primaryScreen.searchScreen.selectCalendar()
            
Screen:
    name: "searchmain"
    MDBoxLayout:
        orientation: "vertical"
        spacing:10
        padding:40
        MDLabel:
            text: "Search"
            font_style: "H4"
            size_hint_y: None
            height: 15
        
        MDSeparator:

        GridLayout:
            cols: 4
            rows: 2
            spacing: [50,5]
            padding: 20
            MDTextField:
                id: fNameEntry
                hint_text: "First Name"
                mode: "rectangle"
                
            MDTextField:
                id: lNameEntry
                hint_text: "Last Name"
                mode: "rectangle"
                
            MDTextField:
                id: emailEntry
                hint_text: "email"
                mode: "rectangle"
                
            MDTextField:
                id: phoneEntry
                hint_text: "Phone Number"
                mode: "rectangle"
               
            MDTextField:
                id: addy1Entry
                hint_text: "Address Line"
                mode: "rectangle"
                
            MDTextField:
                id: postcodeEntry
                hint_text: "Postcode"
                mode: "rectangle"
                
            MDTextField:
                id: orgIDEntry
                hint_text: "ID"
                mode: "rectangle"
            
            DateSelector:
                id:dateEntry
                
            
            
        MDBoxLayout:
            spacing : 15
            MDRaisedButton:
                text: "Search"
                halign:"center"
                valign:"center"
                on_release: app.primaryScreen.searchScreen.search()
                
            MDSpinner:
                size_hint:None,None
                size: dp(40), dp(40)
                active: False
                id: spinner 
                        
                
        MDLabel:
            text: "Results"
            font_style: "H4"
            
        MDSeparator:
        
        ScrollView:
            
            MDList:
                id: resultListView
                
        MDFloatingActionButton:
            icon: "plus"
            on_release: app.primaryScreen.searchScreen.screenManager.current = "adduser"
            md_bg_color: app.theme_cls.primary_color
            
    

            
        
'''

aboutScreenHelper = '''
Screen:
    MDLabel:
        text: "This program was made in 2020-2021 with love by Rajib Ahmed"
        halign: "center"
'''

settingsScreenHelper = '''

Screen:
    MDBoxLayout:
        padding:30
        spacing:10
        orientation: "horizontal"
        MDBoxLayout:
            orientation: "vertical"
            spacing:10
            MDLabel:
                text: "Settings"
                font_style: "H4"
                size_hint_y: None
                height: 34
            ScrollView:
                MDList:    
                    id: flipSwitchView
            MDFillRoundFlatButton:
                text:"Save Settings"
                halign:"center"
                on_release: app.primaryScreen.settingsScreen.saveSettings()
        
        MDBoxLayout:
            orientation:"vertical"
            spacing:25
            MDLabel:
                text: "Software Details"
                font_style: "H4"
                size_hint_y:None
                height:34
                
            MDTextField:
                id: orgname
                disabled: True
                hint_text: "Organisation Name"
            MDTextField:
                id: pracname
                disabled:True
                hint_text: "Practice Name"
                
            Widget:

                
                
                
'''

addPXHelper = '''
<DateSelector@RelativeLayout>:
    size_hint_y: None
    height: dateEntry.height

    MDTextField:
        id: dateEntry
        hint_text: "Date"
        text: ""
        mode: "rectangle"
        color_active: app.theme_cls.primary_light
        helper_text: "Enter date in dd/mm/yyyy format"
        helper_mode: "persistent"
        
       
    MDIconButton:
        icon: "calendar"
        ripple_scale: .5
        pos_hint: {"center_y": .5}
        pos: dateEntry.width - self.width + dp(8), 0
        on_release: app.primaryScreen.searchScreen.addPXScreen.selectCalendar()
        
<IDSelector@RelativeLayout>:
    size_hint_y: None
    height: numEntry.height

    MDTextField:
        id: numEntry
        hint_text: "ID"
        text: ""
        mode: "rectangle"
        color_active: app.theme_cls.primary_light
        helper_text: "Enter date in dd/mm/yyyy format"
        helper_mode: "persistent"
        
       
    MDIconButton:
        icon: "refresh"
        ripple_scale: .5
        pos_hint: {"center_y": .5}
        pos: numEntry.width - self.width + dp(8), 0
        on_release: app.primaryScreen.searchScreen.addPXScreen.autoGenID()
        
Screen:
    name: "adduser"
    BoxLayout:
        orientation:"vertical"
        padding:40
        spacing:10
        MDLabel: 
            halign: "center"
            text:"To add a patient, fill out the details below and click add patient"
            font_style:"Subtitle1"
            size_hint_y: None
            height: 100
        GridLayout:
            cols: 4
            rows: 2
            spacing: [50,0]
            padding: 10
            MDTextField:
                id: fNameEntry
                hint_text: "First Name"
                mode: "rectangle"
                
            MDTextField:
                id: lNameEntry
                hint_text: "Last Name"
                mode: "rectangle"
                
            MDTextField:
                id: emailEntry
                hint_text: "email"
                mode: "rectangle"
                
            MDTextField:
                id: phoneEntry
                hint_text: "Phone Number"
                mode: "rectangle"
               
            MDTextField:
                id: addy1Entry
                hint_text: "Address Line"
                mode: "rectangle"
                
            MDTextField:
                id: postcodeEntry
                hint_text: "Postcode"
                mode: "rectangle"
                
            IDSelector:
                id:orgIDEntry
            
            DateSelector:
                id:dateEntry
                
        MDBoxLayout:
            spacing : 15
                
            MDRaisedButton:
                text: "Add Patient"
                halign:"center"
                valign:"center"
                on_release: app.primaryScreen.searchScreen.addPXScreen.addPX()
                
            MDSpinner:
                size_hint:None,None
                size: dp(40), dp(40)
                active: False
                id: spinner
                
            MDLabel:
                id: infoLabel
                text:""
                size_hint_y: None
                height:10
                font_style:"Caption"
                    
        MDLabel: 
            halign: "center"
            font_style:"Subtitle1"
            size_hint_y: None
            height: 160

        MDFloatingActionButton:
            icon: "backspace"
            on_release: app.primaryScreen.searchScreen.screenManager.current = "searchmain"
            md_bg_color: app.theme_cls.primary_color
    
'''

viewPXHelper = '''
<DateSelector@RelativeLayout>:
    size_hint_y: None
    height: dateEntry.height

    MDTextField:
        id: dateEntry
        hint_text: "Date"
        text: ""
        mode: "rectangle"
        color_active: app.theme_cls.primary_light
        helper_text: "Enter date in dd/mm/yyyy format"
        helper_mode: "persistent"
        
       
    MDIconButton:
        icon: "calendar"
        ripple_scale: .5
        pos_hint: {"center_y": .5}
        pos: dateEntry.width - self.width + dp(8), 0
        on_release: app.primaryScreen.searchScreen.viewPXScreen.selectCalendar()
        
<IDSelector@RelativeLayout>:
    size_hint_y: None
    height: numEntry.height

    MDTextField:
        id: numEntry
        hint_text: "ID"
        text: ""
        mode: "rectangle"
        color_active: app.theme_cls.primary_light
        helper_text: "Enter date in dd/mm/yyyy format"
        helper_mode: "persistent"
        
       
    MDIconButton:
        icon: "refresh"
        ripple_scale: .5
        pos_hint: {"center_y": .5}
        pos: numEntry.width - self.width + dp(8), 0
        on_release: app.primaryScreen.searchScreen.viewPXScreen.autoGenID()
        
Screen:
    BoxLayout:
        orientation:"vertical"
        padding:40
        spacing:10
        MDLabel:
            text: "Patient Details"
            font_style: "H5"
            
        MDSeparator:
        GridLayout:
            cols: 4
            rows: 2
            spacing: [50,0]
            padding: 10
            MDTextField:
                id: fNameEntry
                hint_text: "First Name"
                mode: "rectangle"
                
            MDTextField:
                id: lNameEntry
                hint_text: "Last Name"
                mode: "rectangle"
                
            MDTextField:
                id: emailEntry
                hint_text: "email"
                mode: "rectangle"
                
            MDTextField:
                id: phoneEntry
                hint_text: "Phone Number"
                mode: "rectangle"
               
            MDTextField:
                id: addy1Entry
                hint_text: "Address Line"
                mode: "rectangle"
                
            MDTextField:
                id: postcodeEntry
                hint_text: "Postcode"
                mode: "rectangle"
                
            IDSelector:
                id:orgIDEntry
            
            DateSelector:
                id:dateEntry
                
        MDBoxLayout:
            spacing : 15
                
            MDRaisedButton:
                id:updatePX
                text: "Update Patient Details"
                halign:"center"
                valign:"center"
                on_release: app.primaryScreen.searchScreen.viewPXScreen.updateUserDetails()
                
            MDSpinner:
                size_hint:None,None
                size: dp(40), dp(40)
                active: False
                id: spinner
                
            MDLabel:
                id: infoLabel
                text:""
                size_hint_y: None
                height:15
                font_style:"Caption"
                
        MDLabel:
            text: "Scan History"
            font_style: "H5"
        
        MDSeparator:
            
        ScrollView:
            do_scroll_y: False
            do_scroll_x: True
            BoxLayout:
                orientation: "horizontal"
                spacing: 15
                id: listview
                
        MDFloatingActionButton:
            icon: "backspace"
            on_release: app.primaryScreen.searchScreen.screenManager.current = "searchmain"
            md_bg_color: app.theme_cls.primary_color
            halign: "right"
'''
viewScansHelper = '''
<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48)
    on_release: app.primaryScreen.viewScansScreen.loadScans()
    
<DLabel@MDLabel>:
    size_hint_x: None
    width:60

Screen:
    name: "listview"
    MDBoxLayout:
        orientation: "vertical"
        padding:40
        spacing:20
        MDBoxLayout:
            spacing:15
            size_hint_y: None
            height: 50
            
            MDLabel:
                text: "Recent Scans"
                font_style: "H5"
                
            DLabel:
                text: "Today"
                
            
            Check:
                active: True
                id: day
                
            DLabel:
                text: "Last Week"
            
            Check:
                id: week
                
            DLabel:
                text: "Last Month"
                
            Check:
                id: month
                
        MDSeparator:
            
        ScrollView:
            MDList:
                id:listview
        
'''

viewScanHelper = '''
Screen:

    BoxLayout:
        padding:60
        spacing:5
        orientation: "horizontal"
        
        BoxLayout:
            orientation: "vertical"
            spacing:14
            
            MDLabel:
                text: "Scan Details"
                font_style: "H4"
                size_hint_y: None
                height: 20
            MDLabel:
                id: results
            
                
            MDTextField:
                id: field
                hint_text: "Diagnosis"
            MDTextField:
                id: orgid
                hint_text: "Patient ID"
            
            MDFlatButton:
                id: updateButt
                text: "Update"
                md_bg_color: app.theme_cls.primary_color
                
            MDFlatButton:
                id: deleteButt
                text: "Delete Scan"
                md_bg_color: app.theme_cls.primary_color
                
                
        
        BoxLayout:
            orientation: "vertical"
            spacing:20
            MDLabel:
                text: "Scan"
                font_style: "H4"
                size_hint_y: None
                height: 20
                
            AsyncImage:
                id: image
                
        MDFloatingActionButton:
            id: back
            icon: "backspace"
            on_release: 
            md_bg_color: app.theme_cls.primary_color
                            
'''

introScreenHelper = '''
Screen:
    name: "INTRO"
    MDBoxLayout:
        padding: 250,0,0,250
        spacing:50
        orientation:"vertical"
        valign: "center"
        halign:"center"
        
        MDLabel:
            font_style: "H2"
            text: "Hello!"
            size_hint_y:None
            height: 30
            
        MDLabel:
            font_style: "Subtitle1"
            text: "How would you like to setup this app?"
            size_hint_y:None
            height: 15
        
        MDBoxLayout:
            orientation:"horizontal"
            spacing:20
            size_hint_y:None
            height: 15
            
            MDRaisedButton:
                elevation:20
                text: "Setup Existing Practice"
                on_release: app.setup.sm.current = "EXISTINGPRAC"
                size_hint_y:None
                height: 30
                md_bg_color: app.theme_cls.primary_color
                
            MDRaisedButton:
                elevation:20
                text: "Setup New Practice"
                on_release: app.setup.sm.current = "NEWPRAC"
                size_hint_y:None
                height: 30
                md_bg_color: app.theme_cls.primary_color
'''

setupExistingHelper = '''
Screen:
    name: "EXISTINGPRAC"
    MDBoxLayout:
        orientation:"vertical"
        padding: 50
        spacing:20
        
        MDLabel:
            font_style: "H3"
            text: "Enter your practice code"

        
        MDTextField:
            hint_text: "Code"
            id: codeField
            
        MDRaisedButton:
            text:"Next"
            on_release: app.setup.verifyPracCode(codeField.text)
            md_bg_color: app.theme_cls.primary_color
            
        Widget:
            size_hint_y: None
            height:50
            
        MDFloatingActionButton:
            id: back
            icon: "backspace"
            on_release: app.setup.sm.current = "INTRO"
            md_bg_color: app.theme_cls.primary_color
            
    
'''

setupNewHelper = '''
Screen:
    name: "NEWPRAC"
    MDBoxLayout:
        orientation:"vertical"
        padding: 50
        spacing:20
        
        MDLabel:
            font_style: "H3"
            text: "Enter your organisation code"

        
        MDTextField:
            hint_text: "Code"
            id: codeField
            
        MDRaisedButton:
            text:"Next"
            on_release: app.setup.verifyOrgCode(codeField.text)
            md_bg_color: app.theme_cls.primary_color
            
        Widget:
            size_hint_y: None
            height:50
            
        MDFloatingActionButton:
            id: back
            icon: "backspace"
            on_release: app.setup.sm.current = "INTRO"
            md_bg_color: app.theme_cls.primary_color
    
'''

setupPracticeHelper = '''
        
Screen:
    name: "SETUPPRACTICE"
    MDBoxLayout:
        orientation: "vertical"
        padding: 50
        spacing:30
        MDLabel:
            text: "Make your practice"
            font_style: "H3"
            size_hint_y: None
            height:40
            
        MDLabel:
            text: "Enter your practice details below"
            font_style: "Subtitle2"
            size_hint_y: None
            height:20
            
        GridLayout:
            cols: 3
            rows: 2
            spacing: [50,0]
            padding: 10
            MDTextField:
                id: pracNameEntry
                hint_text: "Practice Name"
                mode: "rectangle"
                
            MDTextField:
                id: adminNameEntry
                hint_text: "System Admin Name"
                mode: "rectangle"
                
            MDTextField:
                id: emailEntry
                hint_text: "Practice Contact Email"
                mode: "rectangle"
                
            MDTextField:
                id: phoneEntry
                hint_text: "Pracitce Contact Number"
                mode: "rectangle"
               
            MDTextField:
                id: addy1Entry
                hint_text: "Practice Address Line"
                mode: "rectangle"
                
            MDTextField:
                id: postcodeEntry
                hint_text: "Practice Postcode"
                mode: "rectangle"
                
        MDBoxLayout:
            orientation: "horizontal"
            spacing:15
            MDRaisedButton:
                text: "Create"
                md_bg_color: app.theme_cls.primary_color
                on_release: app.setup.createPractice()
            
            MDSpinner:
                size_hint:None,None
                size: dp(40), dp(40)
                active: False
                id: spinner
            
                 
'''

setupAdminAccHelper = '''
Screen:
    name: "SETUPADMIN"
    MDBoxLayout:
        orientation:"vertical"
        padding:50
        spacing:30
        MDLabel:
            text: "Make your first account!"
            font_style: "H3"
            size_hint_y: None
            height:40
        MDLabel:
            text: "This will be your practice admin account for OpthaBot"
            font_style: "Subtitle2"
            size_hint_y: None
            height:20
            
        GridLayout:
            cols: 3
            rows: 2
            spacing: [50,0]
            padding: 10
            MDTextField:
                id: fnameEntry
                hint_text: "First Name"
                mode: "rectangle"
                
            MDTextField:
                id: lnameEntry
                hint_text: "Last Name"
                mode: "rectangle"
                
            MDTextField:
                id: emailEntry
                hint_text: "Email"
                mode: "rectangle"
                
            MDTextField:
                id: usernameEntry
                hint_text: "Username"
                mode: "rectangle"
               
            MDTextField:
                id: passwordEntry
                hint_text: "Password"
                mode: "rectangle"
                

                
            Widget:
                
        MDBoxLayout:
            orientation: "horizontal"
            spacing:15
            MDRaisedButton:
                text: "Finish"
                md_bg_color: app.theme_cls.primary_color
                on_release: app.setup.createAdmin()
            
            MDSpinner:
                size_hint:None,None
                size: dp(40), dp(40)
                active: False
                id: spinner
'''

viewAllUsersHelper = '''
Screen:
    name: "VIEWALL"
    MDBoxLayout:
        orientation: "vertical"
        padding:40
        spacing:25
        
        MDLabel:
            text: "Users"
            font_style:"H3"
            size_hint_y:None
            height: 30
            
        MDSeparator:
            
        ScrollView:
            MDList:
                id: listview
                
        MDFloatingActionButton:
            id: back
            icon: "plus"
            on_release: app.primaryScreen.viewUsers.sm.current = "ADDUSER"
            md_bg_color: app.theme_cls.primary_color
'''

addUserHelper = '''
Screen:
    name:"ADDUSER"
    MDBoxLayout:
        padding:40
        spacing:20
        orientation: "vertical"
        
        MDLabel:
            text: "Add User"
            font_style: "H3"
            size_hint_y:None
            height: 30
            
        MDSeparator:
        
        GridLayout:
            cols: 3
            rows: 2
            spacing: [50,0]
            padding: 10
            MDTextField:
                id: fnameEntry
                hint_text: "First Name"
                mode: "rectangle"
                
            MDTextField:
                id: lnameEntry
                hint_text: "Last Name"
                mode: "rectangle"
                
            MDTextField:
                id: emailEntry
                hint_text: "Email"
                mode: "rectangle"
                
            MDTextField:
                id: usernameEntry
                hint_text: "Username"
                mode: "rectangle"
               
            MDTextField:
                id: passwordEntry
                hint_text: "Password"
                mode: "rectangle"
            
                
            MDRaisedButton:
                text:"Select Access Level"
                id:setacc
                on_release:app.primaryScreen.viewUsers.setAccessLevel("ADDUSER")
        MDBoxLayout:
            orientation: "horizontal"
            spacing:15
            MDRaisedButton:
                text: "Create"
                md_bg_color: app.theme_cls.primary_color
                on_release: app.primaryScreen.viewUsers.addUser()
            
            MDSpinner:
                size_hint:None,None
                size: dp(40), dp(40)
                active: False
                id: spinner
        Widget:
                
        MDFloatingActionButton:
            id: back
            icon: "backspace"
            on_release: app.primaryScreen.viewUsers.sm.current = "VIEWALL"
            md_bg_color: app.theme_cls.primary_color
        
'''

viewUserHelper = '''
Screen:
    name: "VIEWUSER" 
    MDBoxLayout:
        padding:40
        spacing:20
        orientation: "vertical"
        
        MDLabel:
            text: "View User"
            font_style: "H3"
            size_hint_y:None
            height: 30
            
        MDSeparator:
        
        GridLayout:
            cols: 3
            rows: 2
            spacing: [50,0]
            padding: 10
            MDTextField:
                id: fnameEntry
                hint_text: "First Name"
                mode: "rectangle"
                
            MDTextField:
                id: lnameEntry
                hint_text: "Last Name"
                mode: "rectangle"
                
            MDTextField:
                id: emailEntry
                hint_text: "Email"
                mode: "rectangle"
            MDTextField:
                id: usernameEntry
                hint_text: "Username"
                mode: "rectangle"
                
            Widget:
            Widget:
               
        MDBoxLayout:
            orientation: "horizontal"
            spacing:15
            
            MDRaisedButton:
                text: "Change Password"
                on_release: app.primaryScreen.viewUsers.changePass()
                
                
            MDRaisedButton:
                text:"Select Access Level"
                id:setacc
                on_release:app.primaryScreen.viewUsers.setAccessLevel("VIEWUSER")
                
            
            MDRaisedButton:
                text: "Update"
                md_bg_color: app.theme_cls.primary_color
                on_release: app.primaryScreen.viewUsers.updateUser()
                
            
            MDSpinner:
                size_hint:None,None
                size: dp(40), dp(40)
                active: False
                id: spinner
        Widget:
        MDFloatingActionButton:
            id: back
            icon: "backspace"
            on_release: app.primaryScreen.viewUsers.sm.current = "VIEWALL"
            md_bg_color: app.theme_cls.primary_color
'''
