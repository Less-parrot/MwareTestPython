def autocompletado(texto, estado):
    comandos = ["getip", "getsms", "getapp", "getuser","getscreen", "pushuser", "pushsms", "pushapp", "exit", "clear"]
    opciones = [comando for comando in comandos if comando.startswith(texto)]
    if estado < len(opciones):
        return opciones[estado]
    else:
        return None
