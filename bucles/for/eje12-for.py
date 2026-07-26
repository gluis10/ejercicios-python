#BUCLE FOR - #EJERCICIO 12

print("\n--------- BIENVENIDO ----------")
"""
Cuadrado de asteriscos.
Solicita al usuario un número y utiliza un bucle for para dibujar un cuadrado de asteriscos.

Por ejemplo, si el usuario ingresa 5:
*****
*****
*****
*****
*****
La cantidad ingresada por el usuario debe determinar tanto el número de filas como la cantidad de asteriscos por fila.
"""

print("\n-- Cuadrado de asteriscos --")
numero = int(input("Ingrese un número: "))

for contador in range(numero):
    resultado = "*" * numero
    print(resultado)

# Explicación de Lógica
"""
- Se solicita al usuario un número entero y se almacena en la variable numero.
- El número ingresado determina tanto la cantidad de filas como la cantidad de asteriscos que tendrá cada fila.

- Se utiliza un bucle for con range(numero) para repetir el proceso tantas veces como indique numero.
- La variable contador controla cuántas veces se repite el for.
- Si el usuario ingresa 5, range(5) genera 5 repeticiones.
- En cada repetición se crea la variable resultado.
- "*" * numero significa repetir el carácter "*" tantas veces como indique el valor de numero.
- Si numero vale 5, "*" * 5 produce "*****".
- El print(resultado) muestra los 5 asteriscos en una línea.
- Como el for se repite 5 veces, se imprimen 5 líneas iguales.
- El resultado final es un cuadrado de 5 filas y 5 columnas de asteriscos.
"""

"""
¿Y qué hace el for?
for contador in range(numero):
Si numero = 5, tenemos: range(5)

Esto hace que el for se repita 5 veces.
Entonces ocurre:
Vuelta 1 → "*" * 5 → *****
Vuelta 2 → "*" * 5 → *****
Vuelta 3 → "*" * 5 → *****
Vuelta 4 → "*" * 5 → *****
Vuelta 5 → "*" * 5 → *****
El resultado es:
    *****
    *****
    *****
    *****
    *****
"""

"""
En resumen:
numero controla el tamaño del cuadrado (filas y columnas), mientras que contador solamente permite que el for repita la impresión el número de veces necesario.
"""