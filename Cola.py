
import re
from Clientes import Cliente


class SistemaAtencion:
    def __init__(self):
        #Colas de clientes atendidos y en espera
        self.cola_clientes = []
        self.clientes_atendidos = []
        self.numero_actual_pólizas = 1
        self.numero_actual_siniestros = 1
    

    def llegada_cliente(self):
    #ingreso de clientes
        nombre = input("Ingrese el nombre del cliente: ")
        while not re.match("^[a-zA-Z\s]*$", nombre):
                print("El nombre no puede contener números ni caracteres especiales. Inténtelo de nuevo.")
                nombre = input("Ingrese el nombre del cliente: ")

        comida= input("ingrese el nombre de la comida q desea : ")
        cantidad= int(input("ingrese el la cantidad de la comida q desea : "))
        precio= float(input("ingrese el precio de la comida q desea : "))
        total = (cantidad * precio)
        cliente = Cliente(nombre,cantidad,comida,precio,total)
        self.cola_clientes.append(cliente)
        """
        eliooo esto es por si necesitamos esto despues
        
        
        
        while comida not in ["1", "2"]:
            print("El servicio debe ser '1' para pólizas o '2' para siniestros. Inténtelo de nuevo.")
            comida = input("Ingrese el servicio (1 para pólizas, 2 para siniestros): ")
        #opciones de servicio 
        if servicio == "1":
            cliente = Cliente(nombre, f"A{self.numero_actual_pólizas}", "pólizas")
            self.numero_actual_pólizas += 1
        elif servicio == "2":
            cliente = Cliente(nombre, f"R{self.numero_actual_siniestros}", "siniestros")
            self.numero_actual_siniestros += 1

        """
        
        

    def atender_cliente(self):
        #Se atiende a un cliente y se manda a la cola de clientes atendidos
        if self.cola_clientes:
            cliente = self.cola_clientes.pop(0)
            cliente.atendido = "Atendido"
            self.clientes_atendidos.append(cliente)
            print(f"Atendiendo al cliente {cliente.nombre}-comida : {cliente.comida}-total a pagar :{cliente.total}")
        else:
            print("No hay clientes en espera.")

    def mostrar_secuencia(self):
        
        if self.clientes_atendidos:
            print("Secuencia de atención de clientes en el día:")
            for cliente in self.clientes_atendidos:
                print(f" {cliente.cantidad} - {cliente.nombre} - {cliente.total} - Estado: {cliente.comida}")
        else:
            print("No hay clientes atendidos.")

    def mostrar_clientes_en_espera(self):
        #Se muestran los clientes en espera
        if self.cola_clientes:
            print("Clientes en espera:")
            for cliente in self.cola_clientes:
                print(f"cliente-{cliente.nombre} -Cantidad de comida={cliente.cantidad} -{cliente.comida} -{cliente.total}  --Estado: {cliente.atendido}")
                print(f"Cliente: {cliente.nombre} - Comida: {cliente.comida} - Cantidad de comida: {cliente.cantidad}  - Total: {cliente.total} - Estado: {cliente.atendido}")
        else:
            print("No hay clientes en espera.")
