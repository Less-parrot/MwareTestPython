import flet as ft
from uiMware.scriptsDB.script import ReadTableDb
from uiMware.views.libs.DefineCards import DefineCardsInfoDevice
from uiMware.views.indexView import listaIDAPP


def AppsView(page: ft.Page):
    

    containerExampleText = ft.Container(
        alignment=ft.alignment.top_center,
        content=ft.Text("Mostrar APPS")
    )
    
    print(f"id aplicaciones: {listaIDAPP}")
    
    

    
    def OcupeMessagesAndId():
        
        idMessages = []
        Messages = []
        
        
        id_app = listaIDAPP
        readApps = ReadTableDb(
        "db/appsDevices.db",
        f"""
        SELECT * FROM apps_device_{id_app[0]}
        
        """    
        )
        for i,b in readApps:
            idMessages.append(i)
            Messages.append(b)
        
        gradient = gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[ft.colors.WHITE70,ft.colors.BLACK26, "#000000"]      
                        )
        
        containerMessages = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column(
                controls=[],
                scroll=ft.ScrollMode.ALWAYS
            )
        ) 
        

        for idMessages, Messages  in  zip(idMessages, Messages):            
            agg = DefineCardsInfoDevice(            
                            gradient,
                            420,
                            2,
                            ft.Icon(ft.icons.APP_SHORTCUT),
                            f"{idMessages}",
                            f"{Messages}"
                            
                            
                )
            containerMessages.content.controls.append(agg)
            

        scrollColumn = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        scrollColumn.controls.append(containerMessages)
        
        return (    
            scrollColumn
        )
        
        
    
    def NavigationToBackPage(e):
        page.go("/index")
    
    def ButtonBackPage():
        
        containerButtonBackPage = ft.Container(
            alignment=ft.alignment.bottom_left,
            content=
            ft.IconButton(
                icon = ft.icons.ARROW_BACK,
                on_click=NavigationToBackPage
            )
        )
        
        return (
            containerButtonBackPage
        )
        
        
    viewApps = [
        containerExampleText,
        OcupeMessagesAndId(),
        ButtonBackPage()
    ]
    
    
    return (
        
        viewApps
        
    )
    