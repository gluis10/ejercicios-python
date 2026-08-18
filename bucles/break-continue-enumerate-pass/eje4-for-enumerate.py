#ENUMERATE - #EJERCICIO 4

print("\n--------- BIENVENIDO ----------")
"""
El enumerate() es una función que se utiliza para recorrer una colección (lista, tupla, cadena, etc.) obteniendo al mismo tiempo el índice y el valor de cada elemento.
"""

#Ejercicio
"""
dsds
"""

print("\n------- Uso del enumerate -------")

frutas = ['manzana', 'platano', 'uva', 'sandia']
print(frutas)

# ------------ recorrido con for normal ----------------
print("\n-- Recorrer la lista con for --")
for contador in frutas:
    print("- ", contador)

# ------------ uso del enumerate ------------------------
print("\n-- Recorrer la lista con la funcion enumerate --")
frutas = ['manzana', 'platano', 'uva', 'sandia']

for posicion, tipo_fruta in enumerate(frutas):
    print("Posición: ", posicion, "=", tipo_fruta)

# ------------ uso del enumerate y start ------------------------
print("\n-- Recorrer lista con la funcion enumerate usando start --")
frutas1 = ['manzana', 'platano', 'uva', 'sandia']

for posicion, tipo_fruta in enumerate(frutas1, start=101):
    print("Posición: ", posicion, "=", tipo_fruta)


# ------------ Convertir a formato lista  ------------------------
print("\n-- Convertir a formato lista --")
enumarador = list(enumerate(frutas1, start=1))
print(enumarador)

# ------------ Espaciado final  ------------------------
print("\n")
