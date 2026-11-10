from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

pila = MiPila(10)
cola = MiCola(10)


# ------------------------- funciones de apoyo -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")


# ------------------------- menú de pila -------------------------
def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if pila.apilar(pasajero):
                print("  ✓ Apilado: ahora es el tope")
        elif op == "2":
            pila.listar()
        elif op == "C":
            for p in datos_prueba():
                pila.apilar(p)
            print("  ✓ Datos de prueba apilados")

        elif op == "3":
            pasajero = pila.desapilar()
            if pasajero is None:
                print("  La pila está vacía")
            else:
                print(f"  Salió: {pasajero}")
                tope = pila.ver_tope()
                if tope is None:
                    print("  La pila está vacía")
                else:
                    print(f"  Nuevo tope: {tope}")

        elif op == "4":
            pasajero = pila.ver_tope()
            if pasajero is None:
                print("  La pila está vacía")
            else:
                print(f"  Tope: {pasajero}")

        elif op == "5":
            numero = leer_entero("  Número de pasajero: ")
            posicion = pila.buscar(numero)
            if posicion == -1:
                print("  No existe")
            else:
                print(f"  Encontrado en [{posicion}]: {pila.datos[posicion]}")

        elif op == "6":
            numero = leer_entero("  Número de pasajero: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()
            if pila.modificar(numero, destino, asiento):
                print("  Pasajero modificado")
            else:
                print("  No existe")

        elif op == "7":
            numero = leer_entero("  Número de pasajero: ")
            if pila.eliminar_por_numero(numero):
                print("  Pasajero eliminado")
            else:
                print("  No existe")

        elif op == "8":
            copia = pila.copiar()
            print("--- COPIA ---")
            copia.listar()
            print("--- ORIGINAL ---")
            pila.listar()

        elif op == "9":
            print(f"  Longitud: {pila.longitud()}")
            if pila.esta_vacia():
                print("  La pila está vacía")
            else:
                print("  La pila no está vacía")

        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ------------------------- menú de cola -------------------------
def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if cola.encolar(pasajero):
                print("  ✓ Encolado: está al final")
        elif op == "2":
            cola.listar()
        elif op == "C":
            for p in datos_prueba():
                cola.encolar(p)
            print("  ✓ Datos de prueba encolados")

        elif op == "3":
            pasajero = cola.desencolar()
            if pasajero is None:
                print("  La cola está vacía")
            else:
                print(f"  Salió: {pasajero}")
                frente = cola.ver_frente()
                if frente is None:
                    print("  La cola está vacía")
                else:
                    print(f"  Nuevo frente: {frente}")

        elif op == "4":
            pasajero = cola.ver_frente()
            if pasajero is None:
                print("  La cola está vacía")
            else:
                print(f"  Frente: {pasajero}")

        elif op == "5":
            numero = leer_entero("  Número de pasajero: ")
            posicion = cola.buscar(numero)
            if posicion == -1:
                print("  No existe")
            else:
                print(f"  Encontrado en [{posicion}]: {cola.datos[posicion]}")

        elif op == "6":
            numero = leer_entero("  Número de pasajero: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()
            if cola.modificar(numero, destino, asiento):
                print("  Pasajero modificado")
            else:
                print("  No existe")

        elif op == "7":
            numero = leer_entero("  Número de pasajero: ")
            if cola.eliminar_por_numero(numero):
                print("  Pasajero eliminado")
            else:
                print("  No existe")

        elif op == "8":
            copia = cola.copiar()
            print("--- COPIA ---")
            copia.listar()
            print("--- ORIGINAL ---")
            cola.listar()

        elif op == "9":
            print(f"  Longitud: {cola.longitud()}")
            if cola.esta_vacia():
                print("  La cola está vacía")
            else:
                print("  La cola no está vacía")

        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ------------------------- menú principal -------------------------
def main():
    while True:
        print("\n===== TAREA PILAS Y COLAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
