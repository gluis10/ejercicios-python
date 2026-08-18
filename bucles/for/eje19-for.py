#BUCLE FOR - #EJERCICIO 19

print("\n--------- BIENVENIDO ----------")
"""
Cuadrado hueco de asteriscos
Solicita al usuario un número y dibuja un cuadrado de asteriscos vacío por dentro.

Por ejemplo, si el usuario ingresa 5:
*****
*   *
*   *
*   *
*****

Pista: Tendrás que controlar las filas y las columnas. Los asteriscos aparecen en los bordes del cuadrado, mientras que en el interior debes imprimir espacios.
"""

print("\n-- Cuadrado hueco de asteriscos --")
numero = int(input("Ingrese un número: "))
fila = 0

for fila in range(numero):
    for columna in range(numero):
  
        if(fila == 0 or fila == numero-1 or columna == 0 or columna == numero-1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Explicación de Lógica
"""
- Se solicita al usuario un número entero y se almacena en la variable numero.
- Este número determina tanto la cantidad de filas como la cantidad de columnas del cuadrado.

- El primer for utiliza range(numero) y controla las filas del cuadrado.
- Si numero vale 5, la variable fila toma los valores:
  0, 1, 2, 3 y 4.

- Dentro del primer for se encuentra un segundo for.
- El segundo for utiliza range(numero) y controla las columnas de cada fila.
- Si numero vale 5, la variable columna también toma los valores:
  0, 1, 2, 3 y 4.

- El segundo for se ejecuta completamente por cada fila.
- Por ejemplo, cuando fila vale 0, columna recorre 0, 1, 2, 3 y 4.
- Después, fila pasa a 1 y nuevamente columna recorre 0, 1, 2, 3 y 4.
- Este proceso continúa hasta completar todas las filas.

- De esta manera se crea una cuadrícula de 5 filas por 5 columnas.

- La condición if comprueba si la posición actual está en alguno de los bordes del cuadrado.

- Si fila == 0, estamos en la primera fila.
- Si fila == numero - 1, estamos en la última fila.
- Si columna == 0, estamos en la primera columna.
- Si columna == numero - 1, estamos en la última columna.

- Si cualquiera de estas condiciones se cumple, se imprime "*".
- Si ninguna se cumple, significa que estamos dentro del cuadrado, por lo que se imprime un espacio.

- print("*", end="") y print(" ", end="") evitan saltar de línea después de cada columna.
- El print() que está fuera del segundo for realiza el salto de línea cuando termina una fila.

- En resumen:
  - El primer for controla las filas.
  - El segundo for controla las columnas dentro de cada fila.
  - El if determina si la posición actual pertenece al borde.
  - Si está en el borde, imprime "*".
  - Si está en el interior, imprime un espacio.
  - Al combinar filas, columnas y condiciones se obtiene un cuadrado vacío por dentro.

- Si numero vale 5, el resultado final es:

*****
*   *
*   *
*   *
*****
"""

