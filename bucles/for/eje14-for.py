#BUCLE FOR - #EJERCICIO 14

print("\n--------- BIENVENIDO ----------")
"""
Triángulo de números repetidos.
Solicita al usuario un número y dibuja un triángulo donde cada fila repita el mismo número.

Por ejemplo, si el usuario ingresa 5:
1
22
333
4444
55555
Observa que el número de la fila determina qué número se debe imprimir y la cantidad de veces que aparece.
"""

print("\n-- Triángulo de números repetidos --")
numero = int(input("Ingrese un número: "))


for contador1 in range(1, numero + 1):
    for contador2 in range(1, contador1 + 1):
        print(contador1, end=" ")
    print()

# Explicación de Lógica
"""
- Se solicita al usuario un número entero y se almacena en la variable numero.
- El número ingresado determina la cantidad de filas que tendrá el triángulo.

- Se utiliza un primer bucle for con range(1, numero + 1) para controlar las filas del triángulo.
- La variable contador1 representa el número de la fila actual.
- Si el usuario ingresa 5, contador1 tomará los valores 1, 2, 3, 4 y 5.

- Dentro del primer for se utiliza un segundo bucle for.
- El segundo for utiliza range(1, contador1 + 1) para determinar cuántas veces se repetirá el número de la fila.
- La variable contador2 controla las repeticiones del segundo for.

- En cada repetición del segundo for se imprime el valor de contador1.
- Se imprime contador1 y no contador2 porque queremos repetir el mismo número en cada fila.
- Por ejemplo, cuando contador1 vale 3, el segundo for se repite 3 veces y se imprime el número 3 en cada repetición.
- Esto produce: 333.

- Se utiliza end=" " para evitar que cada número se muestre en una línea diferente.
- Esto permite que los números repetidos de una misma fila aparezcan juntos.
- Cuando el segundo for termina, se ejecuta print() para realizar un salto de línea y comenzar una nueva fila.

- El proceso continúa hasta que el primer for llega al número ingresado por el usuario.

- Por ejemplo, si el usuario ingresa 5, el resultado será:
  1
  2 2
  3 3 3
  4 4 4 4
  5 5 5 5 5

- De esta manera, el primer for controla qué número se está trabajando y el segundo for controla cuántas veces se repite ese número.
"""

#Y la idea principal que debes recordar de este ejercicio es:
"""
El for externo (contador1) determina el número que se imprime, mientras que el for interno (contador2) determina cuántas veces se repite ese número.
"""