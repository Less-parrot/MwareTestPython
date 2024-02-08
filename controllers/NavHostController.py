import flet as ft
from views.loginView import Login_users
from controllers.Controller import ControllerViews


def main(page: ft.Page):
    #page.views.clear()
    page.title = "M Ware Test"
    page.window_maximizable=False
    def route_change(route):
        page.views.append(
            Login_users(page)
        )
        

        if page.route == "example":
            page.views.append(
                ControllerViews.ViewExample(page)
                
            )
            
               
        elif page.route == "/index":
            page.views.clear()
            page.views.append(
                ControllerViews.ViewIndex(page)
            )
            
        elif page.route == "/index/ExtraInfoDevice":
            page.views.append(
                ControllerViews.ViewProfile(page)
            )
        

        elif page.route == "/index/ExtraInfoDevice/vnc_server":
            page.views.append(
                ControllerViews.ViewVncServer(page)  
            )
            
        elif page.route == "/index/viewSMS":
            page.views.append(
                ControllerViews.ViewSms(page)
            )

        elif page.route == "/index/viewApps":
            page.views.append(
                ControllerViews.ViewApps(page)
            )            
            
        page.update()
        
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


