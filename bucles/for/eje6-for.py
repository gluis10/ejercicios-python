#BUCLE FOR - #EJERCICIO 6

print("\n--------- BIENVENIDO ----------")
"""
Mostrar la tabla de multiplicar de un número.
Solicita al usuario un número y muestra su tabla de multiplicar del 1 al 10 utilizando un for.

Ejemplo para el número 5:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
"""

print("\n-- Mostrar la tabla de multiplicar de un número --")
numero = int(input("Ingrese un número: "))

for contador in range(1, 11):
    resultado = numero * contador
    print(numero, "x", contador, "=", resultado)

# Explicación de Lógica
"""
- Se solicita al usuario un número y se almacena en la variable numero.
- Se utiliza un bucle for para recorrer los números del 1 al 10.
- La función range(1, 11) genera una secuencia desde el 1 hasta el 10.
- Se utiliza 11 como límite superior porque el segundo parámetro de range() no se incluye.
- En cada iteración, el valor actual se almacena en la variable contador.
- La operación numero * contador calcula el resultado correspondiente de la tabla de multiplicar.
- El resultado se almacena en la variable resultado.
- La instrucción print() muestra la operación completa en formato:
  numero x contador = resultado
- El proceso se repite automáticamente hasta completar las diez multiplicaciones de la tabla.
"""

