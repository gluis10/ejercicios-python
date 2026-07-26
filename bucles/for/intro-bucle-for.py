#BUCLE FOR - #INTRODUCCIÓN
"""
¿Qué es el bucle for en Python?

El for es un bucle que se utiliza cuando sabemos de antemano cuántas veces queremos repetir algo o cuando queremos recorrer una colección de elementos (listas, textos, etc.).

Por ejemplo:
-Imprimir los números del 1 al 10.
-Mostrar los caracteres de una palabra.
-Recorrer una lista de nombres.
"""

print("\n--------- Ejemplo 1.1 ----------")
for i in [1,2,3,4,5]:
    print("Hola mundo")

"""
El iterador i esta recorriendo la colección elemento por elemento, y como hay 5 elementos dentro de la colección entonces está repitiendo 5 veces el bucle ("Hola Mundo").
"""
"""
El bucle for recorre la colección elemento por elemento, y cuánto elementos haya será la cantidad de veces que va a repetirse el bucle
"""

print("\n--------- Ejemplo 1.2 ----------")

for i in [2,10,8,3,4,"Alejandra"]:
    print("Hola, como estas?")
#Imprime 5 veces el mensaje


print("\n--------- Ejemplo 1.3 ----------")
print("Mostrar el valor que tiene cada elemento")

for iterador in [2,10,8,3,4,"Alejandra"]:
    print("Elemento: ", iterador)


print("\n--------- Ejemplo 1.4 ----------")
print("Guardar la colección dentro de una variable")

coleccion = ["Harry",10,8,3,7,"Potter"]

for iterador in coleccion:
    print("Elemento: ", iterador)


"""
Esto se puede trabajar con listas, tuplas, conjuntos.
"""

print("\n--------- Ejemplo 1.5 -Diccionario---------")
print("Recorrer un diccionario")

coleccion = {"Harry":22, "Potter":24, "Maria": 28, "Jose":20, "Luis":35}

for iterador in coleccion:
    print("Elemento: ", iterador)


print("\n--------- Ejemplo 1.6 -Diccionario---------")
print("Imprimir las claves y valores de los elementos")

coleccion = {"Harry":22, "Potter":24, "Maria": 28, "Jose":20, "Luis":35}

for iterador in coleccion:
    print(iterador,":", coleccion[iterador])


print("\n--------- Ejemplo 1.7 -Diccionario----------")
print("Imprimir las claves y valores de los elementos de forma profesional")

coleccion = {"Harry":22, "Potter":24, "Maria": 28, "Jose":20, "Luis":35}

for clave, valor in coleccion.items():
    print(clave, "->", valor)

""""""

print("\n--------- Ejemplo 1.8 -Cadena---------")
print("Recorrer una cadena")

coleccion = "HarryP"

for iterador in coleccion:
    print("Hola!")

#Imprime cuantas veces según la cantidad de carácteres!


print("\n--------- Ejemplo 1.9 -Cadena---------")
print("Imprimir carácter por carácter")

coleccion = "HarryP"

for iterador in coleccion:
    print("Elemento: ", iterador)


print("\n--------- Ejemplo 1.10 -Cadena---------")
print("Imprimir carácter por carácter de forma horizontal")

coleccion = "Harry Potter"

for iterador in coleccion:
    print(iterador, end=" ")

#Imprimir carácter por carácter de forma horizontal con espacion por caracter, usando el end=" ".
