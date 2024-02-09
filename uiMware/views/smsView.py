import flet as ft
from uiMware.scriptsDB.script import ReadTableDb
from uiMware.views.libs.DefineCards import DefineCardsInfoDevice
from uiMware.views.indexView import listaIDSMS


def SMSView(page: ft.Page):
    
    containerExampleText = ft.Container(
        alignment=ft.alignment.top_center,
        content=ft.Text("Mostrar Mensajes de texto")
    )
    

    
    def OcupeMessagesAndId():
        
        idMessages = []
        Messages = []
        
        id_sms = listaIDSMS
        print(id_sms)
        readMessages =  ReadTableDb(
        "db/smsDevices.db",
        f"""
        SELECT * FROM sms_device_{id_sms[0]}
        
        """    
    )
        for i,b in readMessages:
            idMessages.append(i)
            Messages.append(b)
        
        gradient = gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=["#000000", ft.colors.RED_900]      
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
                            900,
                            2,
                            ft.Icon(ft.icons.SMS),
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
        
        
    viewSMS = [
        containerExampleText,
        OcupeMessagesAndId(),
        ButtonBackPage()
    ]
    
    
    return (
        
        viewSMS
        
    )
    