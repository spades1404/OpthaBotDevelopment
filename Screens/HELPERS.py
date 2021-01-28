homeContentHelper = '''
Screen:
    BoxLayout:
        orientation: "horizontal"
        padding: 10

        BoxLayout:
            orientation: "vertical"
            padding: 15

            MDLabel:
                text: "Current Image"
                font_style: "Subtitle2"
                size_hint_y: None
                height: 20

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
            MDLabel:
                text: "Recent Results"
                font_style: "Subtitle2"
                size_hint_y: None
                height: 20
            
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
        padding: "8dp"
        spacing: "8dp"
    
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
                        icon: "database-search"
                        
                OneLineIconListItem:
                    text: "Settings"
                    on_release: 
                        app.primaryScreen.content.ids.primaryScreenManager.current = "SETTINGS"
                        navDraw.toggle_nav_drawer()           
                    IconLeftWidget:
                        icon: "content-save-settings"
                        
                OneLineIconListItem:
                    text: "About"
                    on_release: 
                        app.primaryScreen.content.ids.primaryScreenManager.current = "ABOUT"
                        navDraw.toggle_nav_drawer()
                    IconLeftWidget:
                        icon: "account-question"
                        
    
        
'''

primaryScreenHelperVersion2 = '''
MDBoxLayout:
    orientation: "vertical"
    MDToolbar:
        title: "OpthaBot"
        elevation: 10
        
    MDBoxLayout:
        
        orientation: "horizontal"
        MDNavigationRail:
            id: rail
            use_resizeable: True
            visible: "persistent"
            
            MDNavigationRailItem:
                icon: "home"
                text: "Home"
                on_open: app.primaryScreen.content.ids.primaryScreenManager.current = "HOME"
                
            MDNavigationRailItem:
                icon: "database-search"
                text: "Search"
                on_open: app.primaryScreen.content.ids.primaryScreenManager.current = "SEARCH"

            MDNavigationRailItem:
                icon: "content-save-settings"
                text: "Settings"
                on_open: app.primaryScreen.content.ids.primaryScreenManager.current = "SETTINGS"

            MDNavigationRailItem:
                icon: "account-question"
                text: "About"
                on_open: app.primaryScreen.content.ids.primaryScreenManager.current = "ABOUT"
                
        ScreenManager:    
            id: primaryScreenManager
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
Screen:
    MDBoxLayout:
        orientation: "vertical"
        spacing:20
        padding:40
        MDLabel:
            text: "Search"
            font_style: "H4"
            size_hint_y: None
            height: 15

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
            
            MDBoxLayout:
                padding:5
                spacing : 10
                MDRaisedButton:
                    text: "Search"
                    halign:"center"
                    valign:"center"
                    on_release: app.primaryScreen.searchScreen.search()
                MDSpinner:
                    size_hint:None,None
                    size: dp(20), dp(20)
                    active:False
                    id: spinner
                    
                
            
                        
                
        MDLabel:
            text: "Results"
            font_style: "H4"
        ScrollView:
            
            MDList:
                id: resultListView
            
    
        MDFloatingActionButton:
            icon: "plus"
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
    BoxLayout:
        orientation: "vertical"
        BoxLayout:
            orientation: "horizontal"
            ScrollView:
                id: flipSwitchView
                MDLabel:
                    text: "Settings"
            ScrollView:
                id: detailsView
                MDLabel:
                    text: "Software Details"
                
        MDFlatButton:
            text: "Save"
            size_hint_y: None
            height: 15 
                
'''


