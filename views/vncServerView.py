from views.libs.GetRouteFile import GetRouteImage
from views.libs.DefineCards import DefineCardsInfoDevice

from flet import (
    Page,
    Image,
    border_radius,
    IconButton,
    icons,
    Text, 
    Container,
    Column,
    CrossAxisAlignment,
    alignment,
    Padding,
    colors, 
    FontWeight,
    LinearGradient,
    Icon,
    Row,
    MainAxisAlignment,
)

from json import load
from views.indexView import listaIDDevice, listNameDevice
from jsonData.script import InsertUserInJson

def VncServerView(page: Page):    
    
    
    def RouteImage():
        ruta_archivo = "jsonData/config.json"

        with open(ruta_archivo, 'r') as archivo:
            datos_json = load(archivo)

        dataImage = datos_json[f"{listaIDDevice[0]}"]
        routeImage = dataImage['imageVnc']
        return routeImage
    
    def RouteImage1():
        ruta_archivo = "jsonData/config.json"

        with open(ruta_archivo, 'r') as archivo:
            datos_json = load(archivo)

        dataImage = datos_json[f"{listaIDDevice[0]}"]
        routeImage = dataImage['imagen_perfil']
        return routeImage

    print(f"ruta principal: {RouteImage1()}")
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

        
        nameUserProfile = Text("Juan Carlos")
        
        containerProfileDevice = Container(
    
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
    
    
    
    def ViewScreenVncServer():
        containerViewScreenVncServer = Container(
        
            border_radius=border_radius.all(12),
            width=400,
            height=600,
            bgcolor= colors.WHITE70,
            content= Container(
                alignment= alignment.center,
                content= Text("VIEW SCREEN DEVICE", color= colors.BLACK87, size=30,weight= FontWeight.BOLD)
            )
            
        )
        
        return (
            containerViewScreenVncServer
        )
    
    
    containerViewServerVNC = Container(
        
        content=ViewScreenVncServer()
    
    )
    
    def DescriptionDevice():
        titleDescriptionDevice = "CLIENTE VNC"
                
        gradient= LinearGradient(
            begin= alignment.top_center,
            end= alignment.bottom_center,
            colors=[
            
                colors.BLACK87,
                colors.BLACK54,
                colors.BLUE_800,
                colors.CYAN_700
            
            ],    
        )
        
        width, padding = 290, 1
        
        infoDeviceBasic = Column(
            horizontal_alignment= CrossAxisAlignment.CENTER,
            controls=[
                
                Text(titleDescriptionDevice,
                        color= colors.WHITE,
                        size=26,
                        weight= FontWeight.BOLD,
                        italic=True,
                        ),
                
                
                DefineCardsInfoDevice(   
                    gradient, 
                    width,
                    padding,
                    Icon(icons.PERSON),
                    "IP PÚBLICA",
                    "188.127.102.102",
                ),
                
                DefineCardsInfoDevice(       
                    gradient,     
                    width,
                    padding,
                    Icon(icons.PERSON),
                    "IP PRIVADA",
                    "192.168.100.152",
                ),
                
                DefineCardsInfoDevice(            
                    gradient,  
                    width,
                    padding,
                    Icon(icons.AIRPLANEMODE_ON),
                    "PAIS",
                    "Colombia 🇨🇴",
                )
                

            ]
        )
        
        containerInfoDevice = Container(
        
            border_radius= border_radius.all(12),
            bgcolor= colors.WHITE10,
            width= 300,
            height= 600,
            content= infoDeviceBasic
        
        )
        
        return (
            containerInfoDevice
        )
    
    
    
    viewVnc_server = [
        Row(
            alignment= MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                containerProfileUserAndButtonBack,
                containerViewServerVNC,
                DescriptionDevice()
            ]
        )
    ]
    
    
    return (
        
        viewVnc_server
    
    )