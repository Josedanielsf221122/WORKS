"""
    Jose Daniel Sanchez Fonseca 31093026 T1T3 Seccion B 
    Leonardo Gutierrez 31190245 T1T3 Seccion B

"""
from cola import ColaDeBanco

cola = ColaDeBanco()

while True:
    print("1. Ingresar nuevo cliente")
    print("2. Atender al próximo cliente")
    print("3. Eliminar al primer cliente")
    print("4. Atender a todos los clientes")
    print("5. Mostrar clientes")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        cola.nuevo_cliente()
    elif opcion == '2':
        print("El próximo cliente a atender es: ", cola.atender_cliente())
    elif opcion == '3':
        persona_eliminada = cola.eliminar_persona()
        if persona_eliminada is not None:
            print(f"El primer cliente {persona_eliminada} ha sido eliminado.")
        else:
            print("No se pudo eliminar al cliente.")
    elif opcion == '4':
        orden_atencion = cola.atender_todos()
        print("Orden de atención: ", orden_atencion)
    elif opcion == '5':
        print("Clientes con prioridad:",cola.mostrar_clientes_mayor_de_edad())
        print("Clientes Simples :", cola.mostrar_clientes_general())
        print("Clientes en espera: ", cola.mostrar_clientes_generales())
    elif opcion == '6':
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
