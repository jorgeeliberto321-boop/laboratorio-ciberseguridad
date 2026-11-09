from datetime import datetime

def detectar_intentos():
    intentos = {}

    try:
        with open("eventos.log", "r", encoding="utf-8") as archivo:
            for linea in archivo:

                if "Inicio de sesión fallido:" not in linea:
                    continue

                try:
                    fecha_texto = linea[:19]
                    fecha = datetime.strptime(
                        fecha_texto, "%Y-%m-%d %H:%M:%S"
                    )
                except ValueError:
                    continue

                usuario = linea.split(":")[-1].strip()

                if usuario not in intentos:
                    intentos[usuario] = []

                intentos[usuario].append(fecha)

        for usuario, fechas in intentos.items():
            if len(fechas) >= 3:
                deteccion = datetime.now()
                mttd = (deteccion - fechas[0]).total_seconds()

                print(f"ALERTA: {usuario}")
                print(f"MTTD: {mttd:.2f} segundos")

    except FileNotFoundError:
        print("No se encontró eventos.log")


if __name__ == "__main__":
    detectar_intentos()