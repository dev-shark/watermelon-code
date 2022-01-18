def nombre_veces(nombre,cantidad):
    for i in range(cantidad):
        print(f"{i+1} - {nombre}")

nombre = input("ingrese un nombre: ")
cantidad = int(input("Ingrese cantidad: " ))
nombre_veces(nombre, cantidad)
