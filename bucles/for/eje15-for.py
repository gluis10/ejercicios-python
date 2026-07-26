#BUCLE FOR - #EJERCICIO 15

print("\n--------- BIENVENIDO ----------")
"""
Pirámide de asteriscos.
Solicita al usuario un número y dibuja una pirámide utilizando asteriscos.

Por ejemplo, si el usuario ingresa 5:
    *
   ***
  *****
 *******
*********

Pista: Este último ejercicio es un poco más complicado porque tendrás que controlar dos cosas en cada fila: la cantidad de espacios y la cantidad de asteriscos.
"""

print("\n-- Pirámide de asteriscos --")
numero = int(input("Ingrese un número: "))

for contador in range(1, numero + 1):

    espacios = " " * (numero - contador)
    asteriscos = "*" * (contador * 2-1)

    print(espacios + asteriscos)


# Explicación de Lógica
"""
- Se solicita al usuario un número entero y se almacena en la variable numero.
- El número ingresado determina la cantidad de filas que tendrá la pirámide.

- Se utiliza un bucle for con range(1, numero + 1) para recorrer cada una de las filas.
- La variable contador representa el número de la fila actual.
- Si el usuario ingresa 5, contador tomará los valores 1, 2, 3, 4 y 5.

- En cada repetición del for se calculan dos valores diferentes:
  la cantidad de espacios y la cantidad de asteriscos que tendrá la fila actual.

- La variable espacios almacena una cadena formada por espacios en blanco.
- La expresión " " * (numero - contador) repite el espacio tantas veces como indique el resultado de numero - contador.
- La cantidad de espacios disminuye conforme aumenta el número de la fila.

- Si numero = 5 (numero mantiene su valor)(contador empieza en 1 hasta el número)
Entonces:
- numero = 5, contador = 1 entonces 5 - 1 = 4 espacios → "    " 
- numero = 5, contador = 2 entonces 5 - 2 = 3 espacios → "   "
- numero = 5, contador = 3 entonces 5 - 3 = 2 espacios → "  "
- numero = 5, contador = 4 entonces 5 - 4 = 1 espacios → " "
- numero = 5, contador = 5 entonces 5 - 5 = 0 espacios → ""

- La variable asteriscos almacena una cadena formada por asteriscos.
- La expresión "*" * (contador * 2 - 1) determina cuántos asteriscos tendrá cada fila.
- Primero se multiplica contador por 2 y luego se resta 1.
- Esto genera una cantidad impar de asteriscos que aumenta de 2 en 2.
- Si contador vale 1, se generan 1 asterisco. #1x2=2 -> 2-1=1 = *
- Si contador vale 2, se generan 3 asteriscos. #2x2=4 -> 4-1=3 = ***
- Si contador vale 3, se generan 5 asteriscos. #3x2=6 -> 6-1=5 = *****
- Si contador vale 4, se generan 7 asteriscos. #4x2=8 -> 8-1=7 = *******
- Si contador vale 5, se generan 9 asteriscos. #5x2=10 -> 10-1=9 = *********

- Finalmente, print(espacios + asteriscos) une las dos cadenas.
- Primero se colocan los espacios y después los asteriscos.
- Esto permite que los asteriscos queden centrados y formen la figura de una pirámide.

- El proceso se repite hasta completar todas las filas.

- Si el usuario ingresa 5, el resultado final será:

    *
   ***
  *****
 *******
*********

- La lógica principal consiste en que mientras aumentan las filas:
  - Los espacios disminuyen.
  - Los asteriscos aumentan de 2 en 2.

- Gracias a estas dos variables y sus respectivas operaciones matemáticas, se puede construir toda la pirámide utilizando únicamente un for.
"""

#Primero identificas el patrón y después buscas una fórmula que permita automatizar ese patrón.

"""
    *       ← 4 espacios + 1 asterisco
   ***      ← 3 espacios + 3 asteriscos
  *****     ← 2 espacios + 5 asteriscos
 *******    ← 1 espacio  + 7 asteriscos
*********   ← 0 espacios + 9 asteriscos
"""
"""
Si la fila empieza en 1 y el usuario ingresó 5, piensa en estas relaciones:
Fila       Espacios       Asteriscos
  1            4              1
  2            3              3
  3            2              5
  4            1              7
  5            0              9

"""

