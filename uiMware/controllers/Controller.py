from flet import View, Page
from uiMware.views.moreInformationView import ConfigProfileUser
from uiMware.views.indexView import IndexView
from uiMware.views.vncServerView import VncServerView
from uiMware.views.exampleView import ExampleView
from uiMware.views.smsView import SMSView
from uiMware.views.appView import AppsView


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