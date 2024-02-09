import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def EncodeBase64(password: str)-> str:
    return base64.b64encode(password.encode('utf-8')).decode('utf-8')

def decrypt_message(ciphertext, key):
    # Decodificar la clave base64 y crear un objeto AES
    key = base64.b64decode(key)
    cipher = AES.new(key, AES.MODE_CBC, IV=key[:16])
    # Decodificar el texto cifrado base64 y descifrarlo
    ciphertext = base64.b64decode(ciphertext)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    # Decodificar el texto cifrado desencriptado como UTF-8 con manejo de errores
    try:
        return plaintext.decode('utf-8')
    except UnicodeDecodeError:
        return plaintext.decode('utf-8', errors='ignore')
