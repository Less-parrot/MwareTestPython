import sqlite3
import json
import os


def TestCreateFileJson():
    def readBD():
        conn = sqlite3.connect("db/dataDevices.db")
        insert = f"SELECT * FROM sqlite_sequence"
        cursor = conn.cursor()
        cursor.execute(insert)
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
        return(datos)
    
    info, messages, apps = readBD()
    
    def readTableDB(nameTable: str):
        conn = sqlite3.connect("db/dataDevices.db")
        insert = f"SELECT * FROM {nameTable}"
        cursor = conn.cursor()
        cursor.execute(insert)
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
        return(datos)
        
    
    informationDevice = readTableDB(info[0])
    messagesDevice = readTableDB(messages[0])
    appsDevice = readTableDB(apps[0])

    idDevice, nameDevice, ipPublicDevice, ipPrivateDevice, idSMSDevice, idAPPSDevice = informationDevice[0]


    listaMensajes = []
    for i in messagesDevice:
        idMessage, Message = i
        mensaje = {
            "mensaje_id": idMessage,
            "contenido": Message
        }
        listaMensajes.append(mensaje)


    listaAplicaciones = []
    for i in appsDevice:
        idAplication, Aplication = i
        mensaje = {
            "aplication_id": idAplication,
            "app": Aplication
        }
        listaAplicaciones.append(mensaje)
    
# Ejemplo de un nuevo dispositivo
    newDevice = {
        "id": idDevice,
        "NOMBRE": nameDevice,
        "IP_PUBLICA": ipPublicDevice,
        "IP_PRIVADA": ipPrivateDevice,
        "MENSAJES": listaMensajes,
        "APLICACIONES": listaAplicaciones
    }
    
    
    AggDevice('views/TestCode/data.json', newDevice)

    # Agregar el nuevo dispositivo al archivo JSON
    #def JsonTest():
    #    agregar_dispositivo('views/TestCode/data.json', nuevo_dispositivo)




def AggDevice(json_file, nuevo_dispositivo):
    # Si el archivo JSON existe, cargarlo
    if os.path.exists(json_file):
        with open(json_file, 'r') as f:
            data = json.load(f)
    else:
        data = {"dispositivos": []}

    # Agregar el nuevo dispositivo
    data["dispositivos"].append(nuevo_dispositivo)

    # Escribir los datos en el archivo JSON
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)


