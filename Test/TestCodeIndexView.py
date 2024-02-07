import flet as ft
from db.script import readRow
from cliTest.clientSocket import ClientSocketConnection


def main(page: ft.Page):
    
    def icono():
        return(
            ft.IconButton(
                icon=ft.icons.SETTINGS,
                icon_color="blue400",
                icon_size=20,
                tooltip="configuración",
            )   
        ) 
        
    def iconoVNC():
        return(
            ft.IconButton(
                icon=ft.icons.PLAY_CIRCLE,
                icon_color="blue400",
                icon_size=20,
                tooltip="ver pantalla",
            )   
        )
    
    def DefineDataColumn(nameColumn: str,
                         color: str,
                         size: int,
                         grosor: ft.FontWeight):
        return(
            ft.Text(nameColumn, 
                width=size,
                color = color,
                weight=grosor,
                text_align= ft.TextAlign.LEFT,
                #bgcolor=ft.colors.GREEN_700,
                )
        )
                
        
        return(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(idDevice)),
                    ft.DataCell(icono()),
                    ft.DataCell(ft.Text(device)),
                    ft.DataCell(ft.Text(ipPublic)),
                    ft.DataCell(ft.Text(ipPrivate)),
                    ft.DataCell(ft.TextButton(viewSms)),
                    ft.DataCell(ft.TextButton(viewApps)),
                    ft.DataCell(iconoVNC()),
                ]
            )
        )
        
        
    def DefineDataRowTest(data_tuple):
        idDevice, device, ipPublic, ipPrivate = data_tuple
        
        return ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(idDevice)),
                ft.DataCell(icono()),
                ft.DataCell(ft.Text(device)),
                ft.DataCell(ft.Text(ipPublic)),
                ft.DataCell(ft.Text(ipPrivate)),
                ft.DataCell(ft.TextButton("view sms")),
                ft.DataCell(ft.TextButton("view apps")),
                ft.DataCell(iconoVNC()),
            ]
        )
        
        
    def DateTableDevices():
        table = ft.DataTable(
                vertical_lines=ft.border.BorderSide(3, "blue"),
                horizontal_lines=ft.border.BorderSide(1, "white"),
                #border=ft.border.all(2, "red"),
                columns=[
                    
                    ft.DataColumn(DefineDataColumn("ID",
                                                   "white", 
                                                   50,
                                                   ft.FontWeight.W_800),
                                  numeric=True),
                    ft.DataColumn(DefineDataColumn("Config",
                                                   "white",
                                                   55,
                                                   ft.FontWeight.W_400
                                                   ),
                                  ),
                     
                    ft.DataColumn(DefineDataColumn("Dispositivos",
                                                   "white",
                                                   100,
                                                   ft.FontWeight.NORMAL
                                                   ),
                                  ),
                    
                    ft.DataColumn(DefineDataColumn("IP(Pública)",
                                                   "white",
                                                   100,
                                                   ft.FontWeight.NORMAL
                                                   ),
                                  ),
                    
                    ft.DataColumn(DefineDataColumn("IP(Privada)",
                                                   "white",
                                                   100,
                                                   ft.FontWeight.NORMAL
                                                   ),
                                  ),
                    
                    
                    ft.DataColumn(DefineDataColumn("Mensajes de Texto",
                                                   "white",
                                                   120,
                                                   ft.FontWeight.NORMAL
                                                   ),
                                  ),
                    
                    ft.DataColumn(DefineDataColumn("Visualizar Alicaciones",
                                                   "white",
                                                   100,
                                                   ft.FontWeight.NORMAL
                                                   ),
                                  ),
                    
                    ft.DataColumn(DefineDataColumn("Visualizar pantalla(VNC)",
                                                   "white",
                                                   100,
                                                   ft.FontWeight.NORMAL),
                                  ),
                    
                ],
                
                
                rows=[],
                
            )
        
        contenedor = ft.Container(
            gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=["#000000", ft.colors.BLUE_900],        
            ),
            content=table
        )
        def AggRows(e):
            dataDB = readRow()
            contenedor.content.rows.clear()
            data_rows = [DefineDataRowTest(data_tuple) for data_tuple in dataDB]
            for i in data_rows:
                print(i)
                contenedor.content.rows.append(i)
            
            #OcupeRow()
            page.update()
        
        
            
        def DeleteRows(e):
            contenedor.content.rows.pop()
            page.update()
                
                
  
        dataDB = readRow()
        data_rows = [DefineDataRowTest(data_tuple) for data_tuple in dataDB]
        for data_tuple, i in zip(dataDB, data_rows):
            #print(f"Tuple: {data_tuple}")
            contenedor.content.rows.append(i)
        
        #boton = ft.IconButton("Agg", on_click=AggRows)
        refresh = ft.IconButton(
            icon=ft.icons.REFRESH_OUTLINED,
            on_click=AggRows, data=0,
            icon_color="blue500",
            icon_size="30",
            tooltip="recargar datos"
            )
        
        boton1 = ft.ElevatedButton("Delete", on_click=DeleteRows)
        todo = ft.Column(
                controls=[
                    refresh,
                    #boton1,
                    contenedor
                    
                ]
            )
        lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        lv.controls.append(todo)


        return (
            lv
                 
        )
        
       
    page.add(
        ft.Container(  
            margin=ft.Padding(top=0, bottom=30, left=0, right=0),
            alignment=ft.alignment.top_center,   
            content= (
                ft.Column(    
                    controls=[
                        ft.Row(
                            controls=[
                                ft.TextButton("Archivo"),
                                ft.TextButton("Editar"),
                                ft.TextButton("Selección"),
                                ft.TextButton("Ver"),
                                ft.TextButton("Ir"),
                                ft.TextButton("Ayuda")
                                
                            ]
                        )
                    ],
                    
                )
            )
        ),
        
        
        DateTableDevices()
        

    )
    
ClientSocketConnection()
ft.app(target=main)



"""
ft.Container(
    #bgcolor="#808080",
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=["#000000", ft.colors.BLUE_900],
    ),
    content=(TablaTest()),
       
)
"""