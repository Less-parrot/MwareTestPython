import subprocess


def GetRouteImage():
    try:
        # MOSTRAMOS UN DIALOGO DE SELECCIÓN DE ARCHIVOS
        resultado = subprocess.run(
            [
                'zenity',
                '--file-selection',
                '--title=Selecciona una Imagen',#TITULO DE LA PÁGINA
                '--file-filter=Icon Profile(png,jpeg, jpg) | *.png *.jpeg *jpg',#IDENTIFICAMOS POR CUALES EXTENCIONES FILTRAR
                '--file-filter=All files | *'
            ],
            capture_output=True, text=True)#OBTENEMOS LA RUTA DE LA IMAGEN QUE SELECCIONÓ
        if resultado.returncode == 0:
            # LA RUTA SELECCIONADA ESTÁ EN UNA SALIDA ESTANDAR
            ruta_seleccionada = resultado.stdout.strip()
            #print("Ruta absoluta del archivo seleccionado:", ruta_seleccionada) #TEST
            return ruta_seleccionada#RETORNAMOS EL VALOR DE LA RUTA
        
        else:
            return("LogoPerfilHombre3.jpeg")
    
    except FileNotFoundError:
        return("Zenity no está instalado(sudo apt install zenity)")