#Tuplas
"""
Una tupla en Python es una colección ordenada e inmutable de elementos, lo que significa que los valores se almacenan en un orden fijo y no se pueden modificar, agregar o eliminar después de su creación; se definen con paréntesis () y pueden contener distintos tipos de datos, incluso otras colecciones, siendo útiles cuando se quiere manejar información que no debe cambiar, como coordenadas, fechas o configuraciones fijas.
"""

tupla = (4, "Hola", 6.78, [1,2,3],4)
print(tupla)

print("\t")
print("------- buscar elementos según la posición -------")
print(tupla[1]) #Imprime el elemento "Hola"
print(tupla[1:]) #Imprime a partir de elemento "Hola" en adelante.

print("\t")
print("------- verificar si un elemento se encuentra en la tupla -------")
print(4 in tupla)

print("\t")
print("------- ubicar el índice del un elemento -------")
print(tupla.index("Hola"))

print("\t")
print("------- contar la veces de un elemento en mi tupla -------")
print(tupla.count(4))

print("\t")
print("------- ver cuantos elementos tiene la tupla -------")
print(len(tupla))

print("\t")
print("-----------Transformar una tupla en lista-------------------")
tupla1 = (4, "Hola", 6.78, [1,2,3],4)
lista = list(tupla1)
print(lista)

print("\t")
print("-----------Transformar una lista en tupla-------------------")
lista2 = [4, "Hola", 6.78, [1,2,3],4]
tupla2 = tuple(lista2)
print(tupla2)



