#BUCLE FOR - #EJERCICIO 17

print("\n--------- BIENVENIDO ----------")
"""
Rombo de asteriscos
Solicita al usuario un número y dibuja un rombo utilizando asteriscos.

Por ejemplo, si el usuario ingresa 5:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

Pista: Puedes dividir el problema en dos partes: primero construye una pirámide que aumente y después una pirámide invertida que disminuya.
"""

print("\n-- Rombo de asteriscos --")
numero = int(input("Ingrese un número: "))

# Parte superior del rombo
for contadoraum in range(1, numero+1):

    espacios = " " * (numero - contadoraum)
    asteriscos = "*" * ((contadoraum * 2) - 1)
    print(espacios + asteriscos)

# Parte inferior del rombo
for contadordism in range(numero -1, 0, -1):

    espacios = " " * (numero - contadordism)
    asteriscos = "*" * ((contadordism * 2) - 1)
    print(espacios + asteriscos)


# Explicación de Lógica
"""
- Se solicita al usuario un número entero y se almacena en la variable numero.
- El rombo se divide en dos partes: una superior que aumenta y otra inferior que disminuye.

- El primer for construye la parte superior:
  range(1, numero + 1)
- contadoraum controla las filas y aumenta desde 1 hasta numero.
- En cada fila, los espacios disminuyen y los asteriscos aumentan de 2 en 2.
- La expresión (numero - contadoraum) calcula los espacios.
- La expresión (contadoraum * 2) - 1 calcula los asteriscos.

- El segundo for construye la parte inferior:
  range(numero - 1, 0, -1)
- contadordism comienza en numero - 1 y disminuye hasta 1.
- Se utiliza numero - 1 para evitar repetir la fila más grande, que ya fue creada por el primer for.
- En esta parte, los espacios aumentan y los asteriscos disminuyen.

- Los dos for están uno después del otro, por lo que al terminar el primero, comienza automáticamente el segundo.
- De esta manera, la combinación de ambas partes forma el rombo completo.

- Si numero vale 5, el primer for genera:

    *
   ***
  *****
 *******
*********

- Y el segundo for genera:

 *******
  *****
   ***
    *

- Al ejecutarse ambos for consecutivamente, se obtiene el rombo completo.

- En resumen:
  - El primer for construye la mitad superior del rombo.
  - El segundo for construye la mitad inferior.
  - Los espacios permiten centrar los asteriscos.
  - Los asteriscos aumentan en la primera parte y disminuyen en la segunda.
  - range(numero - 1, 0, -1) evita repetir la fila más grande.
"""
