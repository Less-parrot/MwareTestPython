hecho con: FLET

## Descripción:
ESTE PROYECTO VA EN CONJUNTO CON EL PROYECTO DE [MwareTestAndroid](https://github.com/Less-parrot/MwareTestAndroid),
AQUÍ REPRESENTAMOS GRÁFICAMENTE LOS DATOS DE LOS DISPOSITIVOS A LOS CUALES SE TENGA ACCESO,
MEDIANTE UNAS BASES DE DATOS.


## CÓDIGO REALIZADO: 
    1. Por el momento se han realizado 4 vistas, con conexión a una base de datos en una de ellas.
    2. Se realizo el script clientSocet para obtener una shell para obtener la información de los dispositivos en una cli.
    3. Se realizo una refactorización de código, para que se vea más legible y escalable, junto con bibliotecas.


## ESTRUCTURA DEL PROYECTO:
    1. El proyecyo empieza con la ejecución de el archivo main.py en la raiz del mismo.
    2. main.py va a llamar a el archivo NavHostController, el cual llamara a Controller,
        el cual contendrá todas las vistas del proyecto, incluido un ejemplo de vista y
        cómo implementarla para mostrarla.
    
    3. VISTAS:
        _____________________________________________________________
        |           NOMBRE VISTA              |         VISTA       |
        | ------------------------------------|---------------------|
        | -login:                             |            Vista 0  |
        | -index:                             |            Vista 1  |
        | -index/profile:                     |            Vista 2  |
        | -index/profile/vnc_server:          |            Vista 3  |
        | -index/viewSMS                      |            Vista 4  |
        | -index/viewAPP                      |            Vista 5  |
        |                                     |                     |
        -------------------------------------------------------------

    4. Manejamos el proyecto con el framework frontend flet

    5. Tenemos el el directorio "bins" el ejecutable de el cliente VNC "vncviewer" que lo utilizamos para visualizar la pantalla del dispositivo en cuention

    6. Para compilar el proyecto en un ejecutable usamos: flet pack main.py --add-data "assets:assets" --icon icon.png --name MwareTest

    7. En el directorio "dist" encontraremos el banario final

    8. En el directorio views encontraremos el "clientSocket.py" el cuál será fundamental para la recepción de datos de los dispositivos android
        
        COMANDOS:
            -getip      --> Imprime la ip pública y privada del dispositivo
            -getuser    --> Imprime el nombre del dispositivo
            -getsms     --> Imprime en una lista compacta los mensajes de texto del dispositivo
            -getapp     --> Imprime en una lista compacta las aplicaciones tanto del sistema como instaladas del dispositivo
            -pushuser   --> Sube datos del dispositivo como ip(pública/privada), nombre a la base de datos ubicada en "db/dataDevices.db"
            -pushsms    --> Sube a la base de datos "db/smsDevices.db" los mensajes de el dispositvo en una tabla nueva
            -pushapp    --> Sube a la base de datos "db/appsDevices.db" las aplicaciones de el dispositvo en una tabla nueva
    
    9. En el directorio jsonData vamos a encontrar un script, el cual creará un archivo config.json, el cuál contendrá las configuraciones personalizadas del usuario(Pendiente poner para poder modificar nombres de dispositivos)

    10. En el directorio viws/TestCode podemos hacer testeo de código, como vistas y lógica


## POR HACER:
~~1. Segunda conexión a una segunda tabla de la base de datos.~~

~~2. Cuando se acceda a la vista Profile enviar consigo los datos del usuario al cual se quiere acceder, aunque sea un id para que se pueda acceder a los datos del mismo con el id.~~

~~3. Hacer una tabla en la base de datos que guarde los datos editados por el usuario, como imágenes de usuarios, alias, etc...~~

~~4. Conexión de varias bases de datos.~~

    5. Hacer plantillas(GUI) en el apk ware hecho con jetpack compose.

    6. Hacer que cada vista de la UI sea responsive, actualmente solo corre si la UI se deja al 90% - 100% de la pantalla

    7. Mejorar en clientSocket para que sea más usable.

    8. Terminar la ui de MwareTestPython.

    9. Rellenar los las tablas id_sms e id_apps de las bases de datos con los datos del usuario.

    10. Hacer archivo requiriments.txt(IMPORTANTE).

    11. Vista para cámara frontal y trasera del dispositivo-

    12. Vista para enviar mensajes anónimos al dispositivo.

    13. Arreglar comandos push

    14. Lógica para recibir inforamción general sobre el dispositivo, como simcard, temperatura, etc...


## BUGS
    1. Error del ícono en la ui MwareTestPython
    
    2. AL pushear la información del dispositivo si o si tiene que primero pushear el usuario o dará error.

    4. Error al no pushear apps o sms

    
## CÓMO EJECUTAR? 🔨
    1. Primero instale las dependencias del proyecto (pip install -r requirements.txt)
    
    2. Ahora teniendo lo necesario hay dos opciones, ejecutar el proyecto compilado con (./dist/MwareTest) o ejecutar el proyecto con python (python3 main.py)
    
En el [README.md](https://github.com/Less-parrot/MwareTestAndroid/blob/main/README.md) de el proyecto [MwareTestAndroid](https://github.com/Less-parrot/MwareTestAndroid) pondré las instrucciones para usar los dos proyectos en conjunto.

## VERSIÓN   -  FECHA DE LANZAMIENTO
    1.0.0   ~->     04/02/2024: 10:49pm

## by: [Less](https://github.com/Less-parrot/Less-parrot)