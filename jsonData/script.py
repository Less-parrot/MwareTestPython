import json
from views.libs.GetRouteFile import GetRouteImage
from os.path import exists


def cargar_configuracion():
    if exists('jsonData/config.json'):
        try:
            with open('jsonData/config.json', 'r') as archivo:
                configuracion = json.load(archivo)
                # Convertir las claves a enteros
                configuracion = {int(k): v for k, v in configuracion.items()}
            return configuracion
        except FileNotFoundError:
            print("El archivo config.json no se puede leer.")
            return {}
    else:
        print("El archivo config.json no existe. Creando uno nuevo.")
        with open('jsonData/config.json', 'w') as archivo:
            json.dump({}, archivo)
        return {}


# Función para guardar la configuración en un archivo JSON
def guardar_configuracion(configuracion):
    with open('jsonData/config.json', 'w') as archivo:
        json.dump(configuracion, archivo)

# Función para cambiar la imagen de perfil de un usuario específico
def cambiar_imagen_perfil(configuracion, usuario_id, nueva_imagen):
    if usuario_id in configuracion:
        configuracion[usuario_id]['imagen_perfil'] = nueva_imagen
        guardar_configuracion(configuracion)
        print(f"Imagen de perfil del usuario {usuario_id} cambiada con éxito.")
    else:
        print("Usuario no encontrado.")

# Ejemplo de uso
configuracion = cargar_configuracion()

# Mostrar la configuración actual de todos los usuarios
#print("Configuración actual:")
#for usuario_id, usuario_config in configuracion.items():
#    print(f"ID: {usuario_id}, Nombre: {usuario_config.get('nombre_usuario', 'No especificado')}, Imagen: {usuario_config.get('imagen_perfil', 'No especificada')}")



def InsertUserInJson(nameUser: str, id_user: int, nueva_imagen: str, nueva_imageVnc: str="LogoPerfilHombre3.jpeg"):
    nuevo_usuario = nameUser
    # Verificar si el usuario ya existe en la configuración
    usuario_existente = None
    for usuario_id, usuario_config in configuracion.items():
        if usuario_config.get('nombre_usuario') == nuevo_usuario:
            usuario_existente = usuario_id
            break
        
    if usuario_existente is not None:
        # Si el usuario ya existe, actualizar la imagen de perfil y la imagen VNC
        cambiar_imagen_perfil(configuracion, usuario_existente, nueva_imagen)
        configuracion[usuario_existente]['imageVnc'] = nueva_imageVnc
        guardar_configuracion(configuracion)
        print(f"Imagen de perfil e imagen VNC del usuario '{nuevo_usuario}' actualizadas con éxito.")
    else:
        # Si el usuario no existe, agregarlo a la configuración con imagen de perfil e imagen VNC
        nuevo_usuario_id = id_user
        configuracion[nuevo_usuario_id] = {'nombre_usuario': nuevo_usuario, 'imagen_perfil': nueva_imagen, 'imageVnc': nueva_imageVnc}
        guardar_configuracion(configuracion)
        print(f"Usuario '{nuevo_usuario}' agregado con éxito con ID {nuevo_usuario_id} y con imagen de perfil e imagen VNC.")




#
#
#import json
#
## Función para cargar la configuración desde un archivo JSON
#def cargar_configuracion1():
#    try:
#        with open('config.json', 'r') as archivo:
#            configuracion = json.load(archivo)
#        return configuracion
#    except FileNotFoundError:
#        print("El archivo config.json no se encuentra.")
#        return {}
#
## Función para eliminar un usuario por su ID
#def eliminar_usuario(configuracion, usuario_id):
#    if usuario_id in configuracion:
#        del configuracion[usuario_id]
#        guardar_configuracion(configuracion)
#        print(f"Usuario con ID {usuario_id} eliminado con éxito.")
#    else:
#        print("Usuario no encontrado.")
#
## Cargar la configuración desde el archivo JSON
#configuracion = cargar_configuracion1()
#
## Ejemplo de uso
## Eliminar un usuario por su ID
#id_a_eliminar = input("Ingrese el ID del usuario que desea eliminar: ")
#eliminar_usuario(configuracion, id_a_eliminar)
#