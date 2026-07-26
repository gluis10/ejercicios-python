#BUCLE FOR - #EJERCICIO 11

print("\n--------- BIENVENIDO ----------")
"""
Triángulo invertido.
Solicita al usuario un número y dibuja un triángulo de asteriscos invertido.

Por ejemplo, si el usuario ingresa 5:
*****
****
***
**
*
"""

print("\n-- Triángulo de asteriscos invertido --")
numero = int(input("Ingrese un número: "))

for contador in range(numero, 0, -1):
    resultado = "*" * contador;
    print(resultado)


# Explicación de Lógica
"""
- Se solicita al usuario un número entero y se almacena en la variable numero.
- El número ingresado determina la cantidad de asteriscos de la primera línea y también la cantidad de filas del triángulo.
- Se utiliza un bucle for con range(numero, 0, -1) para recorrer los números en orden descendente.
- El contador comienza con el número ingresado y disminuye de uno en uno hasta llegar al 1.
- En cada iteración, se utiliza "*" * contador para repetir el asterisco según el valor actual del contador.
- El resultado se imprime en cada vuelta del for, formando una nueva línea.
- Como el contador disminuye en cada iteración, la cantidad de asteriscos también disminuye.
- Al finalizar el ciclo, se obtiene un triángulo invertido.
"""

"""
La idea principal es:
El for recorre los números de forma descendente y el valor de contador determina cuántos asteriscos se imprimen en cada fila.
"""
