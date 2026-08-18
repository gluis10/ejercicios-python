#BUCLE FOR - #EJERCICIO 28

print("\n--------- BIENVENIDO ----------")
"""
Mostrar las vocales utilizando enumerate()

Solicita al usuario una caracter o frase.
Utiliza enumerate() para recorrerla y mostrar cada vocal encontrada junto con su posición.

Por ejemplo, para: Hola
Deberías obtener algo similar a:
    Posición 0: o
    Posición 1: a
Recuerda que las posiciones comienzan desde 0.
""" 

print("\n-- Mostrar las vocales utilizando enumerate() --")

frase = str(input("Ingrese un caracter o frase: "))
for posicion, caracter in enumerate(frase):

     if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u" or caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U":
             print("Posición", posicion, ":", caracter)

# Explicación de Lógica
"""
- Se solicita una palabra o frase al usuario y se almacena en frase.
- enumerate() recorre cada carácter y proporciona dos valores:
  la posición y la letra.
- posicion almacena el índice y palabra almacena el carácter actual.
- El if verifica si el carácter corresponde a una vocal.
- Si es una vocal, se muestra su posición y la vocal encontrada.
"""

#----------- espaciado final ---------------
print("\n")