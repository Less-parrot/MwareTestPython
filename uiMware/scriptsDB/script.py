import sqlite3

try:

        
    def tableExists(cursor, table_name):
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        return cursor.fetchone() is not None
    
    def createTable(dataBaseConnect: str, table_name: str, createDB: str):
        conn = sqlite3.connect(dataBaseConnect)
        cursor = conn.cursor()
    
        table_name = table_name
        if not tableExists(cursor, table_name):
            
            cursor.execute(createDB)
            conn.commit()
            print(f'Tabla "{table_name}" creada exitosamente')
        else:
            colorRed = "\033[1;31m"
            colorWhite = "\033[0m"
            print(f'{colorRed}ready{colorWhite}')
            pass
    
        conn.close()
            
    #--------------------INSERTAR DATOS  ------------------------#
    
    def InsertDataDevice(dataBaseConnect: str, sqlExecute: str):
        
        conn = sqlite3.connect(dataBaseConnect)
        
        insert = sqlExecute
        
        cursor = conn.cursor()
        cursor.execute(insert)
        conn.commit()
        conn.close()
    #--------------------------------------------------------------#
        
        
    def ExecuteInsertDataDevice():
        InsertDataDevice(
            "db/smsDevices.db",
            """
                INSERT INTO id_sms_device (name_device, id_device) 
	                VALUES ("Sansung A03s", 1)
            """

        )

        InsertDataDevice(
            "db/smsDevices.db",
            """
                INSERT INTO sms_device (sms) 
                	VALUES ("Su código de verificación claro es: 871274")

            """

        )



        InsertDataDevice(
            "db/appsDevices.db",
            """
                INSERT INTO id_apps_devices (name_device, id_device) 
	                VALUES ("Sansung A03s", 1)
            """

        )

        InsertDataDevice(
            "db/appsDevices.db",
            """
                INSERT INTO apps_device (app) 
                	VALUES ("com.whatsapp.co")

            """

        )


    def ReadTableDb(dataBaseConnect: str, sqlExecute: str):
        conn = sqlite3.connect(dataBaseConnect)
        insert = sqlExecute
        cursor = conn.cursor()
        cursor.execute(insert)
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
        return datos
    
        
    
except Exception as e:
    print("¡Ups! Ah ocurridoun error en la ejecución")



