inventario = {
    "arroz":("abarrote", 5, 1690),
    "pipeño":("alcohol", 100, 4990),
    "granadina":("coctelería", 100, 5390),
    "helado de piña":("helados", 200, 4990),
}

def agregar_producto():
    print("A continuación, agrega el producto ingresando los datos solicitados:\n\n")
    nombre_producto = input("Ingresa el nombre del producto: \n")
    precio = int(input("Ingrese el precio del producto: \n"))
    categoria = input("Ingrese la categoría del producto: \n")
    stock = int(input("Ingrese el stock del producto: \n"))

    inventario[nombre_producto] = (categoria,stock,precio)

def buscar_producto():
    while True:
        print("Opciones de búsqueda\n")
        print("1. Buscar por nombre")
        print("2. Buscar por categoría")
        print("3. Devolverse al menú principal")

        tipo_busqueda = input("Ingresa el número de la opción de búsqueda: \n")

        if tipo_busqueda == "1":
            nombre = input("Ingresa el nombre de producto que deseas buscar: ")

            if nombre in inventario:
                categoria = inventario[nombre][0]
                stock = inventario[nombre][1]
                precio = inventario[nombre][2]

                print(f"El producto {nombre} es de la categoría {categoria}, su stock es {stock} y su valor es {precio}")
            else:
                print("El producto no se encuentra")
        
        elif tipo_busqueda == "2":
            categoria = input("Escribe la categoría que quieres buscar:\n")

            for clave, valor in inventario.items():
                
                if categoria in valor:
                    nombre_producto = clave
                    stock = valor[1]
                    precio = valor[2]
                    print(f"El producto {nombre_producto} pertenece a la categoría {categoria}, su stock es {stock} y su precio es {precio}")
        elif tipo_busqueda=="3":
            break
        else:
            print("Ingrese opción válida.")

def modificar_stock():
    nombre_producto=input("Ingrese el nombre del producto a modificar su stock: ")
    if nombre_producto in inventario:
        categoria = inventario[nombre_producto][0]
        stock = inventario[nombre_producto][1]
        precio = inventario[nombre_producto][2]

        print(f"El producto {nombre_producto} tiene un stock de {stock}.")

        print("Modificar stock")
        print("1. Agregar Stock")
        print("2. Quitar stock")

        deltastock=input("Ingrese opción")
        if deltastock=="1":
            delta=int(input("Ingrese unidades a sumar: "))
            delta=delta+stock
            del inventario[nombre_producto]
            inventario[nombre_producto]=(categoria,delta,precio)
            print(f"Stock actualizado. El producto {nombre_producto} tiene un stock de {stock}.")

        elif deltastock=="2":
            delta=int(input("Ingrese unidades a restar: "))
            delta=stock-delta
            del inventario[nombre_producto]
            inventario[nombre_producto]=(categoria,add,precio)
            print(f"Stock actualizado. El producto {nombre_producto} tiene un stock de {stock}.")

        else:
            print("Error in layer 8. Please check yourself.")



    else:
        print("El producto no se encuentra")

def borrar_producto():
    print("Ingrese el nombre del producto que desea borrar del stock")
    nombre_producto=input("Nombre del producto: ")
    if borrar in inventario:
        del inventario[nombre_producto]
        print(f"El producto {nombre_producto} ha sido borrado.")
    else:
        print("Producto no encontrado".)





