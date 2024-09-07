from funciones_menu import *

opcion=""
while opcion != "6":
    print("Bienvenidos al Sistema de Gestión de Inventario")
    print("------------------------------------------------")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Mostrar inventario")
    print("6. Salir del programa")
    print("-------------------------------------------------")
    
    opcion = (input("\n Seleccione una opción escribiendo sólo el número: "))

    if opcion == "1":
        agregar_producto()
        
    elif opcion == "2":
        buscar_producto()
    elif opcion=="3":
        modificar_stock()
    else:
        pass

