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
NavigationLayout:
    ScreenManager:
        Screen:
            BoxLayout:
                orientation: "vertical" 
                MDToolbar:
                    title: "OpthaBot"
                    elevation: 10
                    left_action_items: [["menu", lambda x: navDraw.toggle_nav_drawer()]]
                    
                    
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
                OneLineIconListItem:
                    text: "Home"
                    on_release: 
                        app.primaryScreen.content.ids.primaryScreenManager.current = "HOME"
                        navDraw.toggle_nav_drawer()
                    IconLeftWidget:
                        icon: "home"
                OneLineIconListItem:
                    text: "Search"
                    on_release: 
                        app.primaryScreen.content.ids.primaryScreenManager.current = "SEARCH"
                        navDraw.toggle_nav_drawer()
                    IconLeftWidget:
                        icon: "magnify"
                        
                OneLineIconListItem:
                    text: "Scans"
                    on_release: 
                        app.primaryScreen.content.ids.primaryScreenManager.current = "LISTSCAN"
                        navDraw.toggle_nav_drawer()
                    IconLeftWidget:
                        icon: "selection-search"
                        
                OneLineIconListItem:
                    text: "Settings"
                    on_release: 
                        app.primaryScreen.content.ids.primaryScreenManager.current = "SETTINGS"
                        navDraw.toggle_nav_drawer()           
                    IconLeftWidget:
                        icon: "cogs"
                        
                OneLineIconListItem:
                    text: "About"
                    on_release: 
                        app.primaryScreen.content.ids.primaryScreenManager.current = "ABOUT"
                        navDraw.toggle_nav_drawer()
                    IconLeftWidget:
                        icon: "account-question"
                
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
        id: spinner
        size_hint: None, None
        size: dp(32),dp(32)
        pos_hint: {"center_x":0.5,"center_y":0.2}
        active: False
        
        
'''

searchScreenHelper = '''

<ClickableTextFieldRound>:
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
            
            ClickableTextFieldRound:
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
        ScrollView:
            id: detailsView
            MDLabel:
                text: "Software Details"
                font_style: "H4"
                
                
'''

addUserHelper = '''
<ClickableTextFieldRound>:
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
        on_release: app.primaryScreen.searchScreen.addUserScreen.selectCalendar()
        
<ClickableTextFieldRound2>:
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
        on_release: app.primaryScreen.searchScreen.addUserScreen.autoGenID()
        
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
                
            ClickableTextFieldRound2:
                id:orgIDEntry
            
            ClickableTextFieldRound:
                id:dateEntry
                
        MDBoxLayout:
            spacing : 15
                
            MDRaisedButton:
                text: "Add Patient"
                halign:"center"
                valign:"center"
                on_release: app.primaryScreen.searchScreen.addUserScreen.addUser()
                
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
            halign: "center"
            font_style:"Subtitle1"
            size_hint_y: None
            height: 160

        MDFloatingActionButton:
            icon: "backspace"
            on_release: app.primaryScreen.searchScreen.screenManager.current = "searchmain"
            md_bg_color: app.theme_cls.primary_color
    
'''

viewUserHelper = '''
<ClickableTextFieldRound>:
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
        on_release: app.primaryScreen.searchScreen.viewUserScreen.selectCalendar()
        
<ClickableTextFieldRound2>:
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
        on_release: app.primaryScreen.searchScreen.viewUserScreen.autoGenID()
        
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
                
            ClickableTextFieldRound2:
                id:orgIDEntry
            
            ClickableTextFieldRound:
                id:dateEntry
                
        MDBoxLayout:
            spacing : 15
                
            MDRaisedButton:
                id:updatePX
                text: "Update Patient Details"
                halign:"center"
                valign:"center"
                on_release: app.primaryScreen.searchScreen.viewUserScreen.updateUserDetails()
                
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
                on_focus: if self.focus: app.primaryScreen.viewSingleScanScreen.menu.open()
                
            MDTextField:
                id: orgid
                hint_text: "Patient ID"
                text:
            
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

