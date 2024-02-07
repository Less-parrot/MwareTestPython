import socket
import ssl

# Configuración del servidor y del puerto
host = '192.168.100.242'
port = 8081  # El mismo puerto que utilizas en tu aplicación Kotlin

# Crea un contexto SSL
context = ssl.create_default_context()

# Establece la verificación del certificado. Si estás utilizando un certificado autofirmado,
# podrías querer desactivar la verificación (verify_mode=ssl.CERT_NONE), pero ten en cuenta
# que esto puede ser inseguro en entornos de producción.
context.check_hostname = True
context.verify_mode = ssl.CERT_REQUIRED

# Establece la conexión SSL
with socket.create_connection((host, port)) as sock:
    with context.wrap_socket(sock, server_hostname=host) as ssock:
        # Envía el mensaje al servidor
        ssock.sendall(b'getip')

        # Recibe la respuesta del servidor
        response = ssock.recv(4096)

        # Imprime la respuesta del servidor
        print("Respuesta del servidor:", response.decode())
