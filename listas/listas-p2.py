#Listas

lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", 40, 5.67, [1,2,3], True]

print(lista)

#Podemos determinar cuántos elementos tiene la lista con la función len
print(len(lista))

print("--------------------------------------------------")
lista1 = [1,2,3,4,5]
#Podemos agregar un nuevo elemento a lista con la funcion .append()
#Agrega el elemento según le indicas al final de la lista
lista1.append(6)
lista1.append("Genry")
print(lista1)

print("----------------agregar un elemento---------------")
lista2 = [1,2,4,5]
#Agregar un elemento un una posición específica con la función .insert()
#Se le pasa 2 parámetros, el índice donde quiero que vaya el valor y luego el elemento
lista2.insert(2,3)
print(lista2)
#Agregar varios elementos a la vez con la funcion .extend()
lista2.extend([6,7,8])
print(lista2)

print("--------------------------------------------------")
#Podemos sumar dos listas por ejemplo
lista3 = [1,2,3,4,5]
lista4 = [6,7,8, 9]
lista5 = lista3 + lista4
print(lista5)

print("--------------------------------------------------")
#Determinar si un elemento en específico está dentro de la lista
lista6 = [1,2,3,4,5, "Genry"]
#En este caso, evualuamos si 3 está en la lista
print(3 in lista6)
print("Genry" in lista6)
print(10 in lista6)

#Saber en qué índice pertenece un elemento
print(lista6.index(5))
print(lista6.index(3))
print(lista6.index("Genry"))
#Si pongo un valor que no existe en la lista me va a tirar error

print("--------------------------------------------------")
lista7 = [1,2,3,4,5, "Genry", 1, 3, 2, "Genry", 1, 6, 2]
#Ver cuántas veces aparece un elemento en una lista
print(lista7.count(2))
print(lista7.count("Genry"))

print("-----------Eliminar un elemento-------------------")
#Eliminar un elemento de la lista
lista8 = [1,2,3,4,5, "Genry"]
#Eliminar el último elemento si mandar el parámetro (vacía)
lista8.pop()
print(lista8)
#Eliminar un elemento mando el índice del elemento
lista8.pop(2)
print(lista8)

#Eliminar un elemento pasando el nombre de elemento a eliminar
lista8.remove(5)
print(lista8)
lista8.remove(2)
print(lista8)
#Eliminar toda la lista, dejarla vacía
lista8.clear()
print(lista8)


print("-----------Poner modo reverso-------------------")
#poner una lista en reverso
lista9 = [1,2,3,4,5, "Genry"]
lista9.reverse()
print(lista9)

#Copiar los elementos de la lista 2 o 3 veces
lista9 = [1,2,3,4,5, "Genry"]*2
print(lista9)

print("-----------Ordenar elementos----------------------")
#Ordenar los elementos de la lista con el sort
lista10 = [5,4,-5,-1,3,2]
lista10.sort()
print(lista10)
#Ordenar los elementos de mayor a menor (descendente)
lista10.sort(reverse=True)
print(lista10)

