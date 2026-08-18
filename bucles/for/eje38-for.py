#BUCLE FOR - #EJERCICIO 38

print("\n--------- BIENVENIDO ----------")

"""
Buscar un producto con límite de búsquedas.
z
Crea una lista de productos, por ejemplo:
["Laptop", "Mouse", "Teclado", "Monitor", "Impresora"]

El usuario tendrá 3 oportunidades para buscar un producto.

En cada intento:
- Solicita el nombre del producto.
- Utiliza un for para recorrer la lista y comprobar si existe.
- Si el producto existe, muestra un mensaje indicando que fue encontrado y utiliza break.
- Si no existe, permite realizar otro intento.
- Si el usuario agota los 3 intentos sin encontrar el producto, muestra un mensaje indicando que se agotaron las búsquedas.

Importante: en este ejercicio intenta utilizar una variable booleana, por ejemplo encontrado = False, para determinar si el producto fue encontrado.
"""

print("\n-- Buscar un producto con límite de búsquedas --")

productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Impresora", "Router"]
print(productos)

for intentos in range(3):
    product_buscado = str(input("\nIngrese el producto que desea buscar: "))

    product_encontrado = False

    for lista_productos in productos:
        if product_buscado == lista_productos:
            product_encontrado = True
            break
    if product_encontrado:
        print("El producto", product_buscado, "fué encontrado!")
        break
    else:
        print("Producto no encontrado. Intente nuevamente.")
else:
    print("Intentos de búsqueda agotados!!")

# Explicación de Lógica
"""
- Se crea una lista con los productos disponibles.
- El primer for controla los 3 intentos que tiene el usuario para buscar un producto.
- En cada intento se solicita el nombre del producto.
- product_encontrado = False indica inicialmente que el producto todavía no ha sido encontrado.
- El segundo for recorre uno por uno los productos de la lista.
- El if compara el producto buscado con el producto actual de la lista.
- Si encuentra una coincidencia, product_encontrado cambia a True y el break detiene la búsqueda.
- El if product_encontrado verifica si el producto fue encontrado.
- Si fue encontrado, se muestra el mensaje y el segundo break termina los intentos.
- Si no fue encontrado, se informa al usuario que puede intentar nuevamente.
- Si los 3 intentos terminan sin encontrar el producto, el else del for externo muestra que las búsquedas se agotaron.
"""

"""
Y product_encontrado funciona como una bandera que recuerda si el for interno encontró el producto.
"""

