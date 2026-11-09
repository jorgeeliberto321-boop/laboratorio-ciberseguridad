from datetime import datetime

def registrar_respuesta(usuario, intentos, inicio):
    respuesta = datetime.now()
    mttr = (respuesta - inicio).total_seconds()

    mensaje = (
        f"{respuesta.strftime('%Y-%m-%d %H:%M:%S')} - "
        f"ALERTA ATENDIDA: {usuario}, "
        f"MTTR: {mttr:.2f} segundos"
    )

    with open("respuesta.log", "a", encoding="utf-8") as archivo:
        archivo.write(mensaje + "\n")

    print(mensaje)


if __name__ == "__main__":
    inicio = datetime.now()
    registrar_respuesta("prueba03", 3, inicio)