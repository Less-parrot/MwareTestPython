from os import system, getlogin

usuario = getlogin()
def execute_vnc_viewer(ipServer):
    try:
        puerto_server = "5300"  # Reemplaza con el puerto de tu servidor VNC
        system(f"./bins/vncviewer -geometry 405x610+412+140 {ipServer}:{puerto_server}")

    except Exception as e:
        print("Ocurrió un error al intentar visualizar el dispositivo. Por favor, inténtalo más tarde.", e)
