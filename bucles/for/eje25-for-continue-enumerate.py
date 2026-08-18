#BUCLE FOR - CONTINUE Y ENUMERATE - #EJERCICIO 25

print("\n--------- BIENVENIDO ----------")
"""
Mostrar únicamente las letras que no sean vocales.
Solicita al usuario una palabra y utiliza enumerate() para recorrer
cada carácter junto con su posición.

Utiliza continue para ignorar las vocales.

Para cada consonante, muestra su posición y la letra.

Ejemplo:
Ingrese una palabra: Python

Resultado:
Posición 0: P
Posición 2: t
Posición 3: h
Posición 5: n
"""

print("\n-- Mostrar letras que no sean vocales --")
palabra = str(input("\nIngrese una palabra: "))

for posicion, letra in enumerate(palabra):

    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        continue;
    print("Posición", posicion, ":", letra)


# Explicación de Lógica
"""
- Se solicita una palabra al usuario y se almacena en palabra.
- enumerate() recorre cada letra y proporciona dos valores:
  la posición y la letra.
- El if verifica si la letra es una vocal.
- Si es una vocal, continue omite esa iteración y pasa a la siguiente letra.
- Si no es una vocal, se muestra su posición y la letra correspondiente.
"""

#----------- espaciado final ---------------
print("\n")