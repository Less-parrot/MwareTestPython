import flet as ft
from uiMware.views.libs.clientSocket import ClientSocketConnection
from uiMware.views.libs.OnClickButtons import OnClickButtons

def DialogUser(page: ft.Page):
    page.title = "AlertDialog examples"

    def ActionDismissedDialog(e):
        print("Dialogo cerrado")
    
    def on_click(e):
        global ipServer
        ipServer = e.data
        
    def PostIp(e):
        print(ipServer)
        texto = ClientSocketConnection(ipServer, "getsms")

        if texto == 0:
            dlg.content.content.controls.append(
                ft.Text(f"Servidor {ipServer}:8080 inativo")
            )
        else:
            containerButton = [
                        ft.OutlinedButton(text="getip",width=700-20,
                                          on_click=lambda e: OnClickButtons.ActionnGetIp(e, ipServer)
                                          ),
                        ft.OutlinedButton(text="getuser",width=700-20,
                                          on_click=lambda e: OnClickButtons.ActionnGetUser(e, ipServer)
                                          ),
                        ft.OutlinedButton(text="getsms",width=700-20, 
                                          on_click=lambda e: OnClickButtons.ActionnGetSms(e, ipServer)
                                          ),
                        ft.OutlinedButton(text="getapp",width=700-20,
                                          on_click=lambda e: OnClickButtons.ActionnGetApp(e, ipServer)
                                          ),
                        ft.OutlinedButton(text="pushuser",width=700-20,
                                          on_click=lambda e: OnClickButtons.ActionnPushUser(e, ipServer)
                                          ),
                        ft.OutlinedButton(text="pushsms",width=700-20,
                                          on_click=lambda e: OnClickButtons.ActionnPushSms(e, ipServer)
                                          ),
                        ft.OutlinedButton(text="pushapp",width=700-20,
                                          on_click=lambda e: OnClickButtons.ActionnPushApp(e, ipServer)
                                          ),
            
                    ]
            for i in containerButton:
                dlg.content.content.controls.append(i)
            #dlg.content.content.controls.append(
            #    containerButton
            #)
        
        scroll = ft.ListView(expand=True,spacing=10,padding=20,auto_scroll=False,
          controls=[
                ft.Container(
                    content=ft.Text(texto)
                
                    )
                ]
            )
       
       
        #dlg.content.content.controls.append(
        #        scroll
        #    )
        
        
        page.update()
        dlg.content.content.controls.pop()
        
   
    ipDevice = ft.TextField(
        label="IP SERVER", 
        on_change=on_click,                            
        )
        
    
    buttonOkey = ft.ElevatedButton("Enviar", on_click=PostIp)
    
    dlg = ft.AlertDialog(
        title=ft.Text(
            "Seleccione la IP del dispositivo a conectar"),
            on_dismiss=ActionDismissedDialog,
        content=ft.Container(
            alignment=ft.alignment.top_center,
            width=700,
            
            content=(
                ft.Column(
                    controls=[
                        ipDevice,
                        buttonOkey
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        )
    )
    
    
    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()


    addDevice = ft.IconButton(
            icon=ft.icons.ADD,
            on_click=open_dlg, #Abrir dialogo AlerDialog
            icon_color="red900",
            icon_size="30",
            tooltip="Agregar dispositivo"
            )
    
    return(
        #ft.ElevatedButton("Open dialog", on_click=open_dlg),
        addDevice
    )
    
