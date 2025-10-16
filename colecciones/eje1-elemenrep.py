#Escriba un programa donde tenga una lista y que, a continuación, elimine elementos repetidos, por último mostrar lista.

print("\n--------- BIENVENIDO ----------")
#Creación de lista
lista = ["CR7", "Vini", "Bellingam", "Mbappe", "Arda", "CR7", "Arda", "CR7", "Vini"]
print(lista)

#Recordemos que en los conjuntos no pueden haber elementos repetidos 
#Entonces podemos convertir la "lista" a "conjunto"

print("\n--------Convertir a conjunto eliminando repetidas---------")
conjunto = set(lista)
print(conjunto)

#Como ya eliminamos elementos repetidos, podemos convertirla nuevamente a una "lista"
print("\n--------Convertir el conjunto nuevamente a una lista---------")
listanueva = list(conjunto)
print(listanueva)


print("\n--------- RESOLUCIÓN A NIVEL SENIOR ----------")
lista = ["CR7", "Vini", "Bellingam", "Mbappe", "Arda", "CR7", "Arda", "CR7", "Vini"]
lista = list(set(lista))
print(lista)

#Sobrescribir la lista y le digo que se trasforme en un "conjunto" ("set(lista)") para eliminar los elementos repetidos, luego a este "conjunto" lo trasformo nuevamente a una "lista" ( "list(set(lista))" ), de esa manera los transformo en lista ya con elementos únicos, eliminando los elementos repetidos.


