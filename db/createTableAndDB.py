from db.script import createTable



try:
    createTable(
        "db/dataDevices.db",
        "info_devices", 
        """
        
        CREATE TABLE "info_devices" (
            	"idDevice"	INTEGER,
            	"device"	TEXT,
            	"ip_publica"	TEXT,
            	"ip_privada"	TEXT,
            	PRIMARY KEY("idDevice" AUTOINCREMENT)
            );
        
        """
    )
    
    
    #---------------------BASE DE DATOS SMSDEVICE-----------------------
    createTable(
        "db/smsDevices.db",
        "id_sms_device", 
        
        """
        CREATE TABLE "id_sms_device" (
        	    "id_sms"	INTEGER,
        	    "name_device"	TEXT,
        	    "id_device"	INTEGER,
        	    PRIMARY KEY("id_sms" AUTOINCREMENT)
            );
        """
                
    )
    
    createTable(
        "db/smsDevices.db",
        "sms_device", 
        
        """
        CREATE TABLE "sms_device" (
        	    "id_sms"	INTEGER,
        	    "sms"	TEXT,
        	    PRIMARY KEY("id_sms" AUTOINCREMENT)
            );
        """
                
    )
    #--------------------------------------------------------------------

    #---------------------BASE DE DATOS APPSDEVICE-----------------------
    createTable(
        "db/appsDevices.db",
        "id_apps_devices", 
        
        """
        CREATE TABLE "id_apps_devices" (
        	    "id_apps"	INTEGER,
        	    "name_device"	TEXT,
        	    "id_device"	INTEGER,
        	    PRIMARY KEY("id_apps" AUTOINCREMENT)
            );
        """
                
    )
    
    
    createTable(
        "db/appsDevices.db",
        "apps_device", 
        
        """
        CREATE TABLE "apps_device" (
        	    "id_apps"	INTEGER,
        	    "app"	TEXT,
        	    PRIMARY KEY("id_apps" AUTOINCREMENT)
            );
        """
                
    )
    #--------------------------------------------------------------------
    
except Exception as e:
    print("¡Ups, ah ocurrido un error en la creación de tablas")