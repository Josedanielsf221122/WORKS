
from Cola import SistemaAtencion

# Ejemplo de uso
sistema = SistemaAtencion()
username = input("Ingresa tu nombre de usuario: ")
password = input("Ingresa tu contraseña: ")
while True:
# Determinar el acceso al menú
    
    try:
            
        if username == "cajero" and password == "cajero123":
            print("\nMenú Cajero/Atención al Cliente:")
            while True:
                print("\n1. Llegada de cliente")
                print("2. Atender cliente")
                print("3. Mostrar secuencia de atención")
                print("4. Mostrar clientes en espera")
                print("5. Salir")
                try:
                    opcion = int(input("Elige una opción: "))
                    if opcion == 1:
                        #Opcion de agregar un cliente a la cola de clientes en espera
                        sistema.llegada_cliente()
                    elif opcion == 2:
                        #Opcion de atender a un cliente de la cola de espera
                        sistema.atender_cliente()
                    elif opcion == 3:
                        #opcion de mostrar clientes atendidos
                        sistema.mostrar_secuencia()
                    elif opcion == 4:
                        #opcion de mostrar clientes en espera
                        sistema.mostrar_clientes_en_espera()
                    elif opcion == 5:
                        break
                except ValueError:
                    print("Por favor, ingrese un número para elegir una opción.")
            break



            
            
        elif username == "gerente" and password == "gerente123":
            print("\nMenú Gerente:")
            while True:
                print("\n1. Llegada de cliente")
                print("2. Atender cliente")
                print("3. Mostrar secuencia de atención")
                print("4. Mostrar clientes en espera")
                print("5. Salir")
                try:
                    opcion = int(input("Elige una opción: "))
                    if opcion == 1:
                        #Opcion de agregar un cliente a la cola de clientes en espera
                        sistema.llegada_cliente()
                    elif opcion == 2:
                        #Opcion de atender a un cliente de la cola de espera
                        sistema.atender_cliente()
                    elif opcion == 3:
                        #opcion de mostrar clientes atendidos
                        sistema.mostrar_secuencia()
                    elif opcion == 4:
                        #opcion de mostrar clientes en espera
                        sistema.mostrar_clientes_en_espera()
                    elif opcion == 5:
                        break
                except ValueError:
                    print("Por favor, ingrese un número para elegir una opción.")
            break  
    except NameError:
            print("Nombre de usuario o contraseña incorrectos. Acceso denegado.")

            

def cargar_menu(nombre_archivo):
    menu = {}
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            platillo, descripcion, precio = linea.strip().split(",")
            menu[platillo] = {"descripcion": descripcion, "precio": precio}
    return menu

# Solicitar al cajero que ingrese el pedido
pedido = input("Ingrese el nombre del platillo: ")

# Cargar el menú desde el archivo "menu.txt"
menu = cargar_menu("menu.txt")

# Verificar si el pedido está en el menú
if pedido in menu:
    print(f"Pedido: **{pedido}**")
    print(f"Descripción: {menu[pedido]['descripcion']}")
    print(f"Precio: **${menu[pedido]['precio']:.2f}**")
else:
    print("Comida no localizada en el menú.")
