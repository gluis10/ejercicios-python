#BUCLE FOR - #EJERCICIO 16

print("\n--------- BIENVENIDO ----------")
"""
Triángulo invertido centrado.
Solicita al usuario un número y dibuja un triángulo invertido utilizando asteriscos.

Por ejemplo, si el usuario ingresa 5:
*********
 *******
  *****
   ***
    *

Pista: En cada fila tendrás que controlar dos cosas: la cantidad de espacios aumenta y la cantidad de asteriscos disminuye de 2 en 2.
"""

print("\n-- Triángulo invertido centrado --")
numero = int(input("Ingrese un número: "))

for contador in range(numero, 0, -1):

    espacios = " " * (numero - contador)
    asteriscos = "*" * ((contador * 2) - 1)

    print(espacios + asteriscos)
