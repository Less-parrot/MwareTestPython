from flet import View, Page
from views.profileConfig import ConfigProfileUser
from views.indexView import IndexView
from views.vncServerView import VncServerView
from views.exampleView import ExampleView
from views.viewSMS import SMSView
from views.viewApps import AppsView


class ControllerViews:
    
    def ViewExample(page: Page):
        return View(
            "example",
            ExampleView(page)
        )
    
    def ViewIndex(page: Page):
        return View(
            "/index",
            IndexView(page)
        )
    
    
    def ViewProfile(page: Page):
        return View(
            "/index/ExtraInfoDevice",
            ConfigProfileUser(page)
        )
        
    def ViewVncServer(page: Page):
        return View(
            "/index/ExtraInfoDevice/vnc_server",
            VncServerView(page)
        )
        
    def ViewSms(page: Page):
        return View(
            "/index/viewSMS",
            SMSView(page)
        )
        
        
    def ViewApps(page: Page):
        return View(
            "/index/viewApps",
            AppsView(page)
        )