#BUCLE FOR - #EJERCICIO 13

print("\n--------- BIENVENIDO ----------")
"""
Triángulo de números.
Solicita al usuario un número y dibuja un triángulo utilizando números.

Por ejemplo, si el usuario ingresa 5:
1
12
123
1234
12345
Cada fila debe comenzar nuevamente desde el número 1 y aumentar la cantidad de números mostrados.
"""

print("\n-- Triángulo de números --")
numero = int(input("Ingrese un número: "))

for contador in range(1, numero+1):
    for contador2 in range(1, contador+1):
        print(contador2, end=" ")
    print()

"""
La idea importante es que el for externo controla las filas y el for interno controla los números que aparecen dentro de cada fila.
"""

# Explicación de Lógica
"""
- Se solicita al usuario un número entero y se almacena en la variable numero.
- El número ingresado determina cuántas filas tendrá el triángulo.

- Se utiliza un primer for, llamado for externo.
- El for externo utiliza range(1, numero + 1) para recorrer los números desde 1 hasta el número ingresado.
- Cada repetición del for externo representa una fila diferente del triángulo.

- Dentro del for externo existe un segundo for, llamado for interno.
- El for interno utiliza range(1, contador + 1).
- Este segundo for se encarga de generar los números que aparecerán dentro de cada fila.
- El valor de contador determina hasta qué número debe llegar el for interno.

- En cada repetición del for interno, se imprime el valor de contador2.
- Se utiliza end=" " para evitar que cada número se muestre en una línea diferente. Es decir que se imprime en horizontal (Eje: 123 sin salto de línea)
- Esto permite que los números de una misma fila aparezcan juntos.

- Cuando el for interno termina, significa que ya se imprimieron todos los números correspondientes a esa fila.
- Entonces se ejecuta print() fuera del for interno.
- Este print() realiza un salto de línea para comenzar una nueva fila.

- El proceso continúa hasta que el for externo completa todas las filas.
- De esta manera se forma el siguiente patrón:
  1
  1 2
  1 2 3
  1 2 3 4
  1 2 3 4 5
"""

# Podemos pensar que tienes dos trabajadores:

# Primer for: controla las filas
"""
    for contador in range(1, numero + 1):

Su función es decir: "¿En qué fila del triángulo estamos?"

Si numero = 5, el primer for genera:
    contador = 1
    contador = 2
    contador = 3
    contador = 4
    contador = 5
Por lo tanto, tenemos 5 filas.
"""

# Segundo for: controla los números de cada fila
"""
    for contador2 in range(1, contador + 1):
    
Este for depende del valor que tenga contador.
Su función es decir: "¿Qué números tengo que imprimir en esta fila?"

Por ejemplo:
contador = 1 → imprime 1
contador = 2 → imprime 1 2
contador = 3 → imprime 1 2 3
contador = 4 → imprime 1 2 3 4
contador = 5 → imprime 1 2 3 4 5

Por eso el segundo for necesita estar dentro del primero.
"""

# ¿Cómo trabajan juntos?
"""
Supongamos que el usuario ingresa:
    numero = 5

El programa comienza:
    for contador in range(1, 6):

El primer for empieza con:
    contador = 1

Ahora Python entra al segundo for:
    for contador2 in range(1, 2):

El segundo for solo tiene una vuelta:
    contador2 = 1

Se ejecuta:
    print(contador2, end=" ")

    Resultado: 1

Luego: print()
Hace el salto de línea.

Ahora el primer for pasa a:
    contador = 2

El segundo for ahora es:
    range(1, 3)

Por lo tanto:
    contador2 = 1
    contador2 = 2

Se imprimen en la misma línea: 1 2
    Ahora: contador = 3

    El segundo for genera: 
    1
    2
    3

Como usamos: end=" "
se imprimen así: 1 2 3
Y nuevamente print() hace el salto de línea.
"""

# Finalmente, el proceso completo sería:
"""
    FOR EXTERNO
    contador = 1
        └── FOR INTERNO → 1
                            ↓
                        print()

    contador = 2
        └── FOR INTERNO → 1 2
                            ↓
                        print()

    contador = 3
        └── FOR INTERNO → 1 2 3
                            ↓
                        print()

    contador = 4
        └── FOR INTERNO → 1 2 3 4
                            ↓
                        print()

    contador = 5
        └── FOR INTERNO → 1 2 3 4 5
                            ↓
                        print()

Resultado:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# La idea fundamental
"""
La clave para entender un for anidado es esta:
    Por cada vuelta del for externo, el for interno se ejecuta completamente.

Es decir:
    FOR EXTERNO
        ↓
        FOR INTERNO → se ejecuta completo
        ↓
    FOR EXTERNO
        ↓
        FOR INTERNO → se ejecuta completo
        ↓
    FOR EXTERNO
        ↓
        FOR INTERNO → se ejecuta completo
"""

"""
En tu ejercicio:

🟦 for contador → decide cuántas filas existen.
🟩 for contador2 → decide qué números aparecen en cada fila.
end=" " → mantiene los números en la misma línea.
print() → cuando termina una fila, hace un salto de línea.

Y aquí hay algo muy importante: el segundo for utiliza el valor del primero:
    range(1, contador + 1)

Por eso, cuando contador aumenta, también aumenta la cantidad de números que imprime el segundo for. Esa es precisamente la razón por la que se forma el patrón:

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

¡Este ejercicio es muy bueno porque acabas de aprender uno de los conceptos fundamentales de programación: los bucles anidados!
"""

