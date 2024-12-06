import re
from collections import deque

class ColaDeBanco:
    def __init__(self):
        self.cola_tercera_edad = deque()
        self.cola_general = deque()

    def nuevo_cliente(self):
        while True:
            nombre = input("Ingrese el nombre del cliente: ")
            if not re.match("^[a-zA-Z\s]*$", nombre):
                print("El nombre no puede contener números ni caracteres especiales. Inténtelo de nuevo.")
                continue
            while True:
                try:
                    edad = int(input("Ingrese la edad del cliente: "))
                    if not (0 <= edad <= 116):
                        print("La edad debe estar entre 0 y 116 años. Inténtelo de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Por favor, ingrese un número para la edad. Inténtelo de nuevo.")
            break

        if edad >= 60:
            self.cola_tercera_edad.append(nombre)
        else:
            self.cola_general.append(nombre)

    def atender_cliente(self):
        if self.cola_tercera_edad:
            return self.cola_tercera_edad.popleft()
        elif self.cola_general:
            return self.cola_general.popleft()
        else:
            return "No hay clientes en espera"

    def eliminar_persona(self):
        total_personas = len(self.cola_tercera_edad) + len(self.cola_general)
        if total_personas == 0:
            print("No hay clientes en la cola.")
            return None

        if len(self.cola_tercera_edad) > 0:
            persona_eliminada = self.cola_tercera_edad.popleft()
        else:
            persona_eliminada = self.cola_general.popleft()

        return persona_eliminada

    def atender_todos(self):
        orden_atencion = []
        while self.cola_tercera_edad or self.cola_general:
            cliente_atendido = self.atender_cliente()
            orden_atencion.append(cliente_atendido)
            print(f"El cliente {cliente_atendido} ha sido atendido.")
        return orden_atencion

    def mostrar_clientes_mayor_de_edad(self):
        return list(self.cola_tercera_edad)

    def mostrar_clientes_general(self):
        return list(self.cola_general)

    def mostrar_clientes_generales(self):
        return list(self.cola_tercera_edad) + list(self.cola_general)
