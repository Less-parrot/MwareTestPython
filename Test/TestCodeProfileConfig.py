import flet as ft 
import subprocess
import math

def ConfigProfileUser(page: ft.Page):
    
    def TituloPagina():
        
        titulo = "INFORMACIÓN DE DISPOSITIVO"
        centrar_titulo = ft.Container(
            alignment=ft.alignment.center,
            content=
            ft.Column(
                controls=[
                    ft.Text(titulo, 
                            weight=ft.FontWeight.BOLD,
                            size=16, 
                            font_family="Consolas",
                            italic=True
                            
                        )
                ]
            )

        )
        return (centrar_titulo)
    
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
        
        
    def InfoDevice():
        
        
        def DefineCardsInfoDevice(
                icono: ft.Icon,
                titleCard: str = "Desconocido",
                *descriptionCard: str
                
                
                ):
            descriptions = "\t\n".join(descriptionCard)
            infoSimCard = ft.Card(
            
            
            content=ft.Container(
                #bgcolor=colorCard,
                border_radius=ft.border_radius.all(10),
                gradient=ft.SweepGradient(
                center=ft.alignment.center,
                start_angle=0.0,
                end_angle=math.pi * 2,
                colors=[
                    "0x8b0000",
                    "0xFF34A853",
                    "0x0F130C",
                    "0xFFEA4335",
                    "0x8b0000",
                ],
                stops=[0.0, 0.25, 0.5, 0.75, 1.0],
            ),
                
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
                
                width=700,
                padding=18,
            )
        )
            
            #infoSimCard.content.content.controls.append(ft.Text("Hola"))
            
            return ft.Container(
                #bgcolor=ft.colors.RED,
                alignment=ft.alignment.top_center,
                content=ft.Column(
                    controls=[
                        infoSimCard
                    ]
                )
            )
            
        
        contenedorCards = ft.Container(
            
            content=ft.Column(
                scroll=ft.ScrollMode.ALWAYS,
                controls=[
            DefineCardsInfoDevice(
            ft.Icon(ft.icons.PHONE_ANDROID),
            
            "SIM CARD",
            "Operador: Claro Colombia",
            "Célular: 3224527435",
            "Identificador: 7700121"
            ),
        
        DefineCardsInfoDevice(
            ft.Icon(ft.icons.LOCATION_ON),
                    #color = ft.colors.GREEN_900),
            
            "UBICACIÓN",
            "País: Paipa-Boyacá/Colombia",
            "Cod Postal: 7000120",
            "Corrdenadas: 66º 50' y 84º 46'",
            "Dirección: Cra 33 #17 A",
            ),
        
        
        DefineCardsInfoDevice(
            ft.Icon(ft.icons.APPS_SHARP),
            "APLICACIONES",
            "desplegar apliaciones..."   
        ),
        
        DefineCardsInfoDevice(
            ft.Icon(ft.icons.SMS_OUTLINED),
            "MENSAJES DE TEXTO",
            "despegar mensajes de texto..."
        ),
        
        DefineCardsInfoDevice(
            ft.Icon(ft.icons.ELECTRIC_BOLT_SHARP),
            "GENERAL",
            "Hora: 11:41am",
            "Temperatúra: 32ºC"
        ),
                ]
            )
        )
        
        lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        lv.controls.append(contenedorCards)
        
        return (
            contenedorCards
        )
        
        
    def ActionButtonVncServer(e):
        page.route("index/config/vnc_server")
        
        
    def ViewVNCServerProfile():
        
        imagen = ft.Image(
            src="playVNC.jpeg",
            border_radius=ft.border_radius.all(20),
            )
        contenedor = ft.Container(
            alignment=ft.alignment.top_right,
            width=170,
            height=170,
            #bgcolor=ft.colors.GREEN,
            content=imagen
        )
        
        boton = ft.IconButton(
            content=contenedor,
            on_click=ActionButtonVncServer
                         
            )

        return (boton)
    
         
    def BackToPagePrevious():
        
        iconoVolver = ft.IconButton(
            
            icon=ft.icons.ARROW_BACK,
            tooltip="Volver a la página anterior"
        )
        
        contenedor = ft.Container(
            alignment=ft.alignment.bottom_left,
            
            content=iconoVolver
        )
        return contenedor
    
    
    info = InfoDevice()
    
    lv1 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
    lv1.controls.append(info)
    
    vista = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ProfileUser(),
                lv1,
                ViewVNCServerProfile()
            ]
        )
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
    lv.controls.append(vista)
    
    
    
    
    
    page.add(

        TituloPagina(),
        lv,   
        BackToPagePrevious()

    )
   
   
ft.app(target = ConfigProfileUser,assets_dir="assets")#Llamamos a la vista Test