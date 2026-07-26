#BUCLE FOR - #EJERCICIO 15.1 - for unidados

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

Pista:
El for externo → controla las filas de la pirámide.
El primer for interno → controla la cantidad de espacios.
El segundo for interno → controla la cantidad de asteriscos.
"""

print("\n-- Pirámide de asteriscos con for anidados --")
numero = int(input("Ingrese un número: "))

for contador1 in range(1, numero + 1): 

    for contador2 in range(numero - contador1): 
        print(" ", end=" ") 

    for contador3 in range(contador1 * 2-1): 
        print("*", end=" ") 
    print()

# Explicación de Lógica
"""
- Se solicita al usuario un número entero y se almacena en la variable numero.
- El número ingresado determina la cantidad de filas que tendrá la pirámide.

- Se utiliza un primer bucle for con range(1, numero + 1) para controlar las filas.
- La variable contador1 representa el número de la fila actual.
- Si el usuario ingresa 5, contador1 tomará los valores 1, 2, 3, 4 y 5.

- Dentro del primer for se utiliza un segundo for para controlar los espacios.
- El segundo for utiliza range(numero - contador1).
- Esta operación hace que la cantidad de espacios disminuya conforme aumenta el número de la fila.
- Si numero vale 5:
  - Fila 1: 5 - 1 = 4 espacios.
  - Fila 2: 5 - 2 = 3 espacios.
  - Fila 3: 5 - 3 = 2 espacios.
  - Fila 4: 5 - 4 = 1 espacio.
  - Fila 5: 5 - 5 = 0 espacios.

- En cada repetición del segundo for se ejecuta print(" ", end=" ").
- Esto imprime un espacio sin realizar un salto de línea.
- De esta manera, los espacios se colocan al inicio de cada fila para centrar los asteriscos.

- Después se utiliza un tercer for para controlar los asteriscos.
- El tercer for utiliza range(contador1 * 2 - 1).
- Esta operación genera una cantidad impar de repeticiones que aumenta de 2 en 2.
- Si contador1 vale 1, se generan 1 asterisco. # 1 x 2 = 2 -> 2 - 1 = 1
- Si contador1 vale 2, se generan 3 asteriscos. # 2 x 2 = 4 -> 4 - 1 = 3
- Si contador1 vale 3, se generan 5 asteriscos. # 3 x 2 = 6 -> 6 - 1 = 5
- Si contador1 vale 4, se generan 7 asteriscos. # 4 x 2 = 8 -> 8 - 1 = 7
- Si contador1 vale 5, se generan 9 asteriscos. # 5 x 2 = 10 -> 10 - 1 = 9

- En cada repetición del tercer for se ejecuta print("*", end=" ").
- Esto imprime un asterisco sin realizar un salto de línea.
- Por esta razón, los asteriscos aparecen uno al lado del otro en la misma fila.

- Cuando terminan los dos for internos, se ejecuta print().
- Este print() realiza un salto de línea y permite comenzar a construir la siguiente fila.

- El proceso se repite hasta que el primer for completa todas las filas.

- Si el usuario ingresa 5, el resultado será una pirámide formada de la siguiente manera:

    *
   ***
  *****
 *******
*********

- En resumen:
  - El primer for (contador1) controla las filas.
  - El segundo for (contador2) controla la cantidad de espacios al inicio de cada fila.
  - El tercer for (contador3) controla la cantidad de asteriscos.
  - end=" " permite imprimir espacios y asteriscos en la misma línea.
  - print() al final de los dos for internos permite pasar a la siguiente fila.

- La idea principal es que en cada fila primero se imprimen los espacios necesarios para centrar la pirámide y después se imprimen los asteriscos necesarios para formar su tamaño.
""" 