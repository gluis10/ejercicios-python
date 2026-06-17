#EJERCICIO 2 -COLECCIONES

#Escriba un programa que tenga dos listas y que, a continuación, cree las siguientes listas (en las que no puede haber repeticiones):

#1 - Lista de elementos que aparecen en las dos listas.
#2 - Lista de elementos que aparecen en la primera lista, pero no en la segunda.
#3 - Lista de elementos que aparecen en la segunda lista, pero no en la primera.
#4 - Lista de elementos que aparecen en ambas listas.

print("\n--------- BIENVENIDO ----------")
print("\n-- LISTAS GENERALES --")
lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]
print(lista1)
print(lista2)

print("\n--Eliminar elementos repetidos de ambas listas--")
a = set(lista1)
b = set(lista2)
print(a)
print(b)

print("\n#1 - Lista de elementos que aparecen en las dos listas.")
#Es decir, unir las dos listas
union = a | b
print(union)

print("\n--Convetirla nuevamente a lista: ")
union = list(a | b)
print("\n", union)

print("\n#2 - Lista de elementos que aparecen en la primera lista, pero no en la segunda.")
#Es decir, solo los elementos que aparecen en la primera lista y que no estan en la segunda lista, basándonos en las listas generales.
soloA = list(a - b)
print(soloA)

print("\n#3 - Lista de elementos que aparecen en la segunda lista, pero no en la primera.")
#Es decir, solo los elementos que aparecen en la segunda lista y que no estan en la primera lista, basándonos en las listas generales.
soloB = list(b - a)
print(soloB)

print("\n#4 - Lista de elementos que aparecen en ambas listas.")
#Es decir, solo los ementos que están en ambas
interseccion = list(a & b)
print(interseccion)



