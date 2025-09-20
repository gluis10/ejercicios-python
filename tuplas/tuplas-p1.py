#Una tupla en Python es una colección ordenada e inmutable de elementos, lo que significa que los valores se almacenan en un orden fijo y no se pueden modificar, agregar o eliminar después de su creación; se definen con paréntesis () y pueden contener distintos tipos de datos, incluso otras colecciones, siendo útiles cuando se quiere manejar información que no debe cambiar, como coordenadas, fechas o configuraciones fijas.

#TUPLAS
tupla = (4, "Hola", 6.78, [1,2,3],4)
print(tupla)

#lo que se puede con la tupla es buscar
print(tupla[1])
print(tupla[1:])
#verificar si un elemento se encuentra en la tupla
print(4 in tupla)
#Saber en qué índice pertenece un elemento
print(tupla.index("Hola"))
#Ver cuántas veces aparece un elemento en mi tupla
print(tupla.count(4))
#Nos indica cuantos elementos tiene la tupla
print(len(tupla))

print("-----------Transformar tuplas en listas-------------------")
tupla1 = (4, "Hola", 6.78, [1,2,3],4)
lista = list(tupla)
print(lista)

print("-----------Transformar listas en tuplas-------------------")
lista2 = [4, "Hola", 6.78, [1,2,3],4]
tupla2 = tuple(lista2)
print(tupla2)
