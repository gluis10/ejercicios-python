#BUCLE FOR - ENUMERATE - #EJERCICIO 23

print("\n--------- BIENVENIDO ----------")
"""
Mostrar la posición de cada letra.
Solicita al usuario una palabra y utiliza enumerate() para recorrer
cada carácter mostrando su posición.

Ejemplo:
Ingrese una palabra: Python
Resultado esperado:
Posición 0: P
Posición 1: y
Posición 2: t
Posición 3: h
Posición 4: o
Posición 5: n
"""
print("\n-- Mostrar la posición de cada letra usando enumerate --")
palabra = str(input("\n- Ingrese una palabra: "))

for posicion, caracter in enumerate(palabra):
    print("Posición", posicion, ":", caracter)

# Explicación de Lógica
"""
- Se solicita una palabra al usuario y se almacena en palabra.
- enumerate() recorre cada carácter de la palabra y proporciona dos valores:
  la posición y el carácter.
- posicion almacena el índice y caracter almacena la letra actual.
- El for recorre toda la palabra y print() muestra ambos valores.
"""

"""
Lo importante que acabas de aprender es que enumerate() te evita tener que crear y manejar manualmente un contador para conocer la posición de cada elemento.
"""