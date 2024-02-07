import flet as ft
import subprocess

def VncServerView(page: ft.Page):

    def obtener_ruta_seleccionada():
        try:
            # Ejecutar el diálogo de selección de archivos utilizando zenity
            resultado = subprocess.run(['zenity',
                                        '--file-selection',
                                        '--title=Selecciona una Imagen',
                                        '--file-filter=Icon Profile(png,jpeg, jpg) | *.png *.jpeg *jpg',
                                        '--file-filter=All files | *'],
                                       capture_output=True, text=True)

            if resultado.returncode == 0:
                # La ruta seleccionada está en la salida estándar
                ruta_seleccionada = resultado.stdout.strip()
                #print("Ruta absoluta del archivo seleccionado:", ruta_seleccionada)
                return ruta_seleccionada
            else:
                return("No se seleccionó ningún archivo.")
        except FileNotFoundError:
            return("Zenity no está instalado. Instálalo para utilizar esta funcionalidad.")
    
    def ProfileUser(routeImage: str = "LogoPerfilHombre3.jpeg"):

        imageUser = ft.Image(
            src=routeImage,
            width=120,
            height=120, 
            border_radius=ft.border_radius.all(15)
        )
        
        def changeImageUser(e):
            imageUser.src = str(obtener_ruta_seleccionada())
            page.update()
            
        iconoUser = ft.IconButton(
            icon = ft.icons.EDIT,
            tooltip="Editar Imágen",
            on_click=changeImageUser
            )  

        
        nombreUsuario = ft.Text("Juan Carlos")
        
        contenedorPerfil = ft.Container(
            
            width=150,
            #bgcolor=ft.colors.RED,
            #alignment=ft.alignment.top_left,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    imageUser,
                    iconoUser,
                    nombreUsuario
                ]
            )
        )
        

        
        return (contenedorPerfil)


    def BackToPagePrevious():
        
        iconoVolver = ft.IconButton(
            
            icon=ft.icons.ARROW_BACK,
            tooltip="Volver a la página anterior"
        )
        
        contenedor = ft.Container(
            alignment=ft.alignment.bottom_left,
            padding=ft.Padding(10,400,10,10),
            content=iconoVolver
        )
        return contenedor
    

    
    contenedorTodo = ft.Container(
        padding=ft.Padding(10,10,10,10),
        content=ft.Column(
            controls=[
                ProfileUser(),
                BackToPagePrevious()
                
            ]
        )

    )
    
    
    
    def ViewScreenVncServer():
        contenedor = ft.Container(
            border_radius=ft.border_radius.all(12),
            width=400,
            height=600,
            bgcolor=ft.colors.WHITE70,
            
        )
        
        return (contenedor)
    
    
    contenedorVNC = ft.Container(
        content=ViewScreenVncServer()
    )
    
    def DescriptionDevice():
        titulo = "CLIENTE VNC"
        
        def DefineCardsInfoDevice(
                icono: ft.Icon,
                titleCard: str = "Desconocido",
                *descriptionCard: str
                
                
                ):
            descriptions = "\t\n".join(descriptionCard)
            infoSimCard = ft.Card(
            
            
            content=ft.Container(
            gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.colors.BLACK87,ft.colors.BLACK54, ft.colors.BLUE_800, ft.colors.CYAN_700],    
                
            ),
            border_radius=ft.border_radius.all(15),
                
                content=ft.Column(
                    scroll=ft.ScrollMode.ALWAYS,
                    controls=
                    [
                        ft.ListTile(
                            leading=icono,
                            title=ft.Text(titleCard),
                            subtitle=ft.Column(
                                controls=[
                                    ft.Text(
                                        descriptions
                                    )
                                ]
                            )
                            
                        ),
                    ]
                    
                ),
                
                width=290,
                padding=1,
            )
        )
            
            return infoSimCard
        
        arguments = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(titulo,
                        color=ft.colors.WHITE,
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        italic=True,
                        ),
                DefineCardsInfoDevice(            
                    ft.Icon(ft.icons.PERSON),
                    "IP PÚBLICA",
                    "188.127.102.102",
                ),
                DefineCardsInfoDevice(            
                    ft.Icon(ft.icons.PERSON),
                    "IP PRIVADA",
                    "192.168.100.152",
                ),
                DefineCardsInfoDevice(            
                    ft.Icon(ft.icons.AIRPLANEMODE_ON),
                    "PAIS",
                    "Colombia ",
                ),

            ]
        )
        
        contenedor = ft.Container(
            border_radius=ft.border_radius.all(12),
            bgcolor=ft.colors.WHITE10,
            width=300,
            height=600,
            content=arguments
        )
        return (contenedor)
    
    
    
    
    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                contenedorTodo,
                contenedorVNC,
                DescriptionDevice()
                
            ]
        )
        
    )


ft.app(target = VncServerView)