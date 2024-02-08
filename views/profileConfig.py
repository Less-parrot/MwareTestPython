import math
from views.libs.GetRouteFile import GetRouteImage
from views.libs.DefineCards import DefineCardsInfoDevice, DefineCardsAPPS_SMS_Device

from flet import (
    Page,
    Container,
    alignment,
    Column,
    Text, 
    FontWeight,
    Image,
    border_radius,
    icons,
    IconButton,
    CrossAxisAlignment,
    SweepGradient,
    ScrollMode,
    Icon,
    Row,
    MainAxisAlignment,
    ListView,
    TextButton,
    colors, 
    Padding
    
)

from os import system
from views.indexView import listaIDDevice, listIPDevice, listIPDevice1, listNameDevice
from views.libs.LocalitationDevice import IPinfo
from db.script import ReadTableDb
from json import loads, load
from jsonData.script import InsertUserInJson
from views.libs.GetRouteFile import GetRouteImage


def ConfigProfileUser(page: Page):

    def TitlePageInformationDevice():
        
        titulo = "INFORMACIÓN DE DISPOSITIVO"
        containerTitileInformationDevice = Container(
            alignment= alignment.center,
            
            content=
            Column(
                controls=[
                    
                    Text(
                        titulo, 
                        weight= FontWeight.BOLD,
                        size=16, 
                        font_family="Consolas",#USAMOS LA FUENTE CONSOLAS, (TEST)
                        italic=True#ACTIVAMOS LA LETRA ITALIC 
                    )
                    
                ]
            )

        )
        
        return (
            
            containerTitileInformationDevice
        
        )
        
    def RouteImage():
        ruta_archivo = "jsonData/config.json"

        with open(ruta_archivo, 'r') as archivo:
            datos_json = load(archivo)

        dataImage = datos_json[f"{listaIDDevice[0]}"]
        routeImage = dataImage['imagen_perfil']
        return routeImage
    
    def RouteImage1():
        ruta_archivo = "jsonData/config.json"

        with open(ruta_archivo, 'r') as archivo:
            datos_json = load(archivo)

        dataImage = datos_json[f"{listaIDDevice[0]}"]
        routeImage = dataImage['imageVnc']
        return routeImage
    
    def ProfileUser():

        routeImage = RouteImage()
        imageUser = Image(
            src=routeImage,#Ponemos una imagen por defecto, hasta que el usuario seleccione una
            width=120,
            height=120, 
            border_radius=border_radius.all(15)
        )
        
        def ChangeImageUser(e):
            InsertUserInJson(nameUser=listNameDevice[0], id_user=listaIDDevice[0], nueva_imageVnc=GetRouteImage(), nueva_imagen=RouteImage1())
            imageUser.src = RouteImage()
            page.update()
            
        iconEditImageUser = IconButton(
            icon = icons.EDIT,
            tooltip="Editar Imágen",
            on_click=ChangeImageUser
            )  

        
        nameUserProfile = Text(listNameDevice[0])
        
        containerProfileDevice = Container(
            bgcolor=colors.GREEN_200,
    
            width=150,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    imageUser,
                    iconEditImageUser,
                    nameUserProfile
                ]
            )
            
        )
        
        return (
            
            containerProfileDevice #RETORNAMOS EL CONTENEDOR DE LA IMAGEN DE USUARIO EN UNA COLUMNA
        
        )


    def AccessBackPage(e):
        view_pop = []
        lista_filtrada = [vista for vista in page.views if not ('route=\'/\'') in str(vista)]        
        for i in lista_filtrada:
            if str(i) == "view {'route': '/', 'verticalalignment': 'center', 'horizontalalignment': 'center'}":
                pass
            else:
                view_pop.append(i)
        
        
        page.go(view_pop[-2].route)
        

    def ButtonAccessBackPage():
        IconBackPage = IconButton(
            
            icon=icons.ARROW_BACK,
            tooltip="Volver a la página anterior"#TEXTO QUE APARECERÁ ENCIMA DE EL BOTÓN AL PASAR EL RATÓN POR ENCIMA
        
        )
        
        containerBackPage = Container(
            
            alignment= alignment.bottom_left,
            padding= Padding(10,400,10,10),
            content=IconBackPage,
            on_click=AccessBackPage
        
        )
        
        return (
            containerBackPage
        )
    
    containerProfileUserAndButtonBack = Container(
        
        padding= Padding(10,10,10,10),
        content= Column(
            
            controls=[
                ProfileUser(),
                ButtonAccessBackPage()
            ]
            
        )
        
    )
        
        
    def InfoDevice():
        IPDevice = listIPDevice[0]
        ipinfo = IPinfo(IPDevice)
        localitation = ipinfo.start()
        data_dict = loads(localitation)

        # Acceder a los valores del diccionario
        pais = data_dict["country"]
        ciudad = data_dict["city"]
        proveedorInternet = data_dict["isp"]
        Maps = data_dict["maps"]
        bandera = data_dict["flag"]
        
        readMessages =  ReadTableDb(
        "db/smsDevices.db",
        f"""
        SELECT * FROM sms_device_{listaIDDevice[0]}
        
        """    
        )
        
        readApps = ReadTableDb(
        "db/appsDevices.db",
        f"""
        SELECT * FROM apps_device_{listaIDDevice[0]}
        
        """    
        )
        
        
        gradient= SweepGradient( #DEGRADADO EN ESTRELLA
                center= alignment.center,
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
            )
        width, padding = 1005, 10
        
        containerInfoExtraDevice = Container(
            expand=True, 
            content= Column(
                expand=True,
                scroll= ScrollMode.ALWAYS,
                controls=[
                    
                    DefineCardsInfoDevice(
                        gradient,
                        width,
                        padding,
                        Icon(icons.PHONE_ANDROID),
                        "SIM CARD",
                        "Operador: Claro Colombia",
                        "Célular: 3149127812",
                        "Identificador: 8912112"
                    ),
        
                    DefineCardsInfoDevice(
                        gradient,
                        width,
                        padding,
                        Icon(icons.LOCATION_ON),
                        "UBICACIÓN",
                        f"País: {pais} {bandera}",
                        f"Ciudad: {ciudad}"
                        #f"Cod Postal: 1247412",
                        f"Coordenadas: {Maps}",
                        f"Proveedor de internet: {proveedorInternet}",
                    ),
        
        
                    DefineCardsAPPS_SMS_Device(
                        gradient,
                        width,
                        padding,
                        Icon(icons.APPS_SHARP),
                        "MENSAJES DE TEXTO",
                        "sms",
                        readMessages
                    ),
                    
                    
                    DefineCardsAPPS_SMS_Device(
                        gradient,
                        width,
                        padding,
                        Icon(icons.APPS_SHARP),
                        "APLICACIONES",
                        "apps",
                        readApps
                    ),
        
                    DefineCardsInfoDevice(
                        gradient,
                        width,
                        padding,
                        Icon(icons.ELECTRIC_BOLT_SHARP),
                        "GENERAL",
                        "Hora: 11:41am",
                        "Temperatúra Célular: 32ºC"
                    ),
                    
                ]
            )
        )
        
        return (
            
            
            ListView(expand=True,spacing=10,padding=20,auto_scroll=False,
                     controls=[
                         containerInfoExtraDevice,
                            ]
                    )
        
        )
        
    
    def NavigateToIndex(e):
        page.go("/index")#NAVEGAMOS HACIA LA VISTA /INDEX
        
        
    def BackToPagePrevious():
        
        iconBackPage = IconButton(
                
            icon= icons.ARROW_BACK,
            tooltip= "Volver a la página anterior",
            on_click= NavigateToIndex
        
        )
        
        containerBackPage = Container(
            
            alignment= alignment.bottom_left,
            content= iconBackPage
        
        )
        
        return (
            containerBackPage
        )
    
    


    
    
    viewExtraInfoDevice = [
        Row(
            spacing=40,
            expand = True,
            controls=[
                containerProfileUserAndButtonBack,
                InfoDevice()
            ]
        )
    ]
    
    return (
        
        viewExtraInfoDevice
    
    )
    
    
    
    
