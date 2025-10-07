#Diccionarios
"""
Un diccionario en Python es una colección de datos desordenada pero estructurada en pares clave: valor, donde cada clave es única y se usa para acceder rápidamente a su valor; se define con llaves {} y es ideal para representar información con una relación clara, como nombres con edades, productos con precios o usuarios con sus datos.
"""
#Diccionario vacío
diccionario = {}
print(diccionario)

print("-------Ejemplo de diccionario-------")
diccionario1 = {"azul":"blue", "rojo": "red", "verde":"green"}
#clave: azul, valor: blue
print(diccionario1)

print("\n-------Buscar una palabra en específico-------")
#Buscar por su clave
print(diccionario1["azul"])
print(diccionario1["rojo"])

print("------Agregar un nuevo valor al diccionario-----")
diccionario1["amarillo"] = "yellow"
#clave: amarillo, valor: yellow
print(diccionario1)

print("\n-------Modificar un valor al diccionario------")
diccionario1["azul"] = "BLUE"
#clave: azul, nuevo valor: BLUE
print(diccionario1)

print("\n-------Eliminar un valor al diccionario------")
del(diccionario1["verde"])
#eliminar el valor de clave "verde"
print(diccionario1)

print("\n------Dicionarios con otros tipos de datos------")
#Los diccionarios también aceptan diferentes tipos de datos o incluso, lista, tuplas, conjuntos o otros diccionarios

diccionario2 = {"Genry":[22, 1.50], "Jose":[21, 1.75], "Maria":[22, 1.67]}
#clave: Genry, valor: [22, 1.50]
print(diccionario2)

print("\n------Dicionario dentro de un diccionario------")
diccionario3 = {"Genry":{"edad":22, "estatura":1.60}, "Jose":[21, 1.75], "Maria":[22, 1.67]}
print(diccionario3)

print("\n------Imprimir los valores de clave Genry------")
print(diccionario3["Genry"])


print("\n")