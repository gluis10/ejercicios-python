#BUCLE FOR - #EJERCICIO 10

print("\n--------- BIENVENIDO ----------")
"""
Dibujar un triángulo de asteriscos.
Solicita al usuario un número y dibuja un triángulo utilizando *.

Por ejemplo, si el usuario ingresa 5:
*
**
***
****
*****
"""

print("\n-- Dibujar un triángulo de asteriscos. --")
numero = int(input("Ingrese un número: "))

for contador in range(1, numero + 1):
    resultado = "*" * contador
    print(resultado)

# Explicación de Lógica
"""
- Se solicita al usuario que ingrese un número entero y se almacena en la variable numero.
- El número ingresado representa la cantidad de filas que tendrá el triángulo.

- Se utiliza un bucle for para recorrer una secuencia de números desde 1 hasta el número ingresado.
- Se utiliza range(1, numero + 1) porque necesitamos que el contador comience en 1.
- El segundo valor de range() no se incluye, por eso se utiliza numero + 1.
- Por ejemplo, si el usuario ingresa 5, range(1, 5 + 1) genera los valores:
  1, 2, 3, 4 y 5.

- En cada repetición del for, la variable contador contiene el número actual de la secuencia.
- Se crea la variable resultado y se utiliza "*" * contador para repetir el carácter "*" tantas veces como indique contador.
- En la primera iteración, contador vale 1, por lo que se imprime un asterisco.
- En la segunda iteración, contador vale 2, por lo que se imprimen dos asteriscos.
- En la tercera iteración, contador vale 3, por lo que se imprimen tres asteriscos.
- El proceso continúa hasta llegar al número ingresado por el usuario.

- Finalmente, el print() muestra el resultado de cada iteración en una línea diferente.
- De esta manera, la cantidad de asteriscos aumenta en una unidad en cada fila, formando un triángulo.
"""

