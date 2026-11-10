from pasajero import Pasajero


class MiPila:
    """Pila LIFO: entra y sale por el tope."""
    # Sin métodos integrados de listas, len, búsquedas con in,
    # slicing ni comprensiones.

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("  ⚠ La pila está llena")
            return False
        if self.buscar(pasajero.numero) != -1:
            print("  Ya existe un pasajero con ese número")
            return False
        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):
        if self.cantidad == 0:
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ---------------------------------------------------------------------
    def desapilar(self):
        if self.esta_vacia():
            return None
        self.cantidad = self.cantidad - 1
        pasajero = self.datos[self.cantidad]
        self.datos[self.cantidad] = None
        return pasajero

    def ver_tope(self):
        if self.esta_vacia():
            return None
        return self.datos[self.cantidad - 1]

    def buscar(self, numero):
        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i].numero == numero:
                return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)
        if posicion == -1:
            return False
        self.datos[posicion].destino = nuevo_destino
        self.datos[posicion].asiento = nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        auxiliar = MiPila(self.capacidad)
        encontrado = False
        while not self.esta_vacia():
            pasajero = self.desapilar()
            if pasajero.numero == numero:
                encontrado = True
                break
            auxiliar.apilar(pasajero)

        while not auxiliar.esta_vacia():
            self.apilar(auxiliar.desapilar())
        return encontrado

    def copiar(self):
        # Se copia del fondo al tope para conservar el orden.
        nueva = MiPila(self.capacidad)
        for i in range(self.cantidad):
            nueva.apilar(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0
