#BUCLE FOR - #EJERCICIO 18

print("\n--------- BIENVENIDO ----------")
"""
Triángulo numérico centrado
Solicita al usuario un número y dibuja un triángulo utilizando números.

Por ejemplo, si el usuario ingresa 5:
    1
   123
  12345
 1234567
123456789

Pista: En cada fila tendrás que controlar la cantidad de espacios y la cantidad de números. Observa que los números de cada fila aumentan de 2 en 2.
"""

print("\n-- Triángulo numérico centrado --")
numero = int(input("Ingrese un número: "))

for contador in range(1, numero+1):
    
    espacios = " " * (numero - contador)
    secuencia = contador * 2-1
    print(espacios, end="")

    for contador1 in range(1, secuencia+1):
        print(contador1, end="")
    
    print()

# Explicación de Lógica
"""
- Se solicita al usuario un número entero y se almacena en la variable numero.
- El primer for controla la cantidad de filas del triángulo.
- Si numero vale 5, contador toma los valores del 1 al 5.

- En cada fila se calculan dos elementos:
  1. Los espacios que se colocarán al inicio.
  2. La cantidad de números que tendrá la fila.

- La expresión " " * (numero - contador) genera los espacios necesarios para centrar cada fila.
- Conforme contador aumenta, la cantidad de espacios disminuye.

- La variable secuencia calcula cuántos números tendrá cada fila:
  contador * 2 - 1
- Esto genera cantidades impares:
  1, 3, 5, 7 y 9.

- El segundo for se encarga de imprimir los números desde 1 hasta la cantidad indicada por secuencia.
- Por ejemplo, si secuencia vale 5, el for interno imprime:
  12345

- print(espacios, end="") imprime los espacios sin saltar de línea.
- print(contador1, end="") imprime cada número en la misma línea.
- Finalmente, print() hace un salto de línea cuando termina cada fila.

- El for externo controla las filas y el for interno controla los números que aparecen dentro de cada fila.

- Por eso, si numero vale 5, el resultado es:

    1
   123
  12345
 1234567
123456789
"""

