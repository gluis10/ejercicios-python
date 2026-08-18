#BUCLE FOR - #EJERCICIO 20

print("\n--------- BIENVENIDO ----------")
"""
Pirámide de números repetidos
Solicita al usuario un número y dibuja una pirámide donde cada fila repita el mismo número, pero ahora centrada.

Por ejemplo, si el usuario ingresa 5:
    1
   222
  33333
 4444444
555555555

Pista: Este ejercicio combina varias ideas que ya practicaste: controlar las filas, calcular los espacios, determinar cuántas veces se repite cada número y utilizar el número de la fila para saber qué valor imprimir.
"""

print("\n-- Pirámide de números repetidos --")
numero = int(input("Ingrese un número: "))

for filas in range(1, numero+1):

    espacios = " " * (numero - filas)
    secuencia = filas * 2-1;
    print(espacios, end="")

    for contador2 in range(secuencia):
        print(filas, end="")
    print()

# Explicación de Lógica
"""
- Se solicita al usuario un número entero y se almacena en la variable numero.
- El primer for controla la cantidad de filas de la pirámide.
- Si numero vale 5, la variable filas toma los valores:
  1, 2, 3, 4 y 5.

- En cada fila se calculan los espacios para centrar la pirámide.
- La expresión " " * (numero - filas) hace que los espacios disminuyan conforme avanzan las filas.

- La variable secuencia calcula cuántas veces debe repetirse el número de cada fila.
- Se utiliza la fórmula:
  filas * 2 - 1

- Esto genera las cantidades:
  - Fila 1 → 1 * 2 - 1 = 1 repetición.
  - Fila 2 → 2 * 2 - 1 = 3 repeticiones.
  - Fila 3 → 3 * 2 - 1 = 5 repeticiones.
  - Fila 4 → 4 * 2 - 1 = 7 repeticiones.
  - Fila 5 → 5 * 2 - 1 = 9 repeticiones.

- El for interno utiliza range(secuencia).
- Este for no imprime la variable contador2, sino que utiliza su cantidad de repeticiones para saber cuántas veces ejecutar el print().

- Dentro del for interno se imprime filas.
- Como filas representa el número de la fila actual, siempre se imprime el mismo número durante toda esa fila.

- Por ejemplo, cuando filas vale 3:
  - secuencia vale 5.
  - range(5) hace que el for interno se ejecute 5 veces.
  - En cada repetición se ejecuta print(filas, end="").
  - Como filas vale 3, se imprime el número 3 cinco veces:
    33333

- Cuando filas vale 4:
  - secuencia vale 7.
  - El for interno se ejecuta 7 veces.
  - Como filas vale 4, se obtiene:
    4444444

- El print(espacios, end="") coloca los espacios al inicio de cada fila.
- El print(filas, end="") mantiene todos los números de la misma fila juntos.
- El print() que está fuera del for interno realiza el salto de línea para comenzar la siguiente fila.

- En resumen:
  - El for externo controla qué número corresponde a cada fila.
  - espacios controla el centrado.
  - secuencia calcula cuántas repeticiones debe tener cada fila.
  - El for interno repite la impresión la cantidad indicada por secuencia.
  - filas determina qué número se imprime en cada repetición.

- Si numero vale 5, el resultado final es:

    1
   222
  33333
 4444444
555555555
"""

"""
¡Claro! Aquí lo importante es entender que el for interno no decide qué número imprimir, sino cuántas veces debe repetir el número que ya tiene filas.
"""

# La clave para entender el for interno es esta:
"""
for contador2 in range(secuencia):
    print(filas, end="")

contador2 no se utiliza para imprimir. Su función es simplemente hacer que el print() se ejecute varias veces.
Es como decir:
    "Ejecuta print(filas) tantas veces como indique secuencia."

Por eso, cuando:
    filas = 3
    secuencia = 5
el for interno hace conceptualmente esto:
    print(3)
    print(3)
    print(3)
    print(3)
    print(3)

Y gracias a end="", todo queda en la misma línea:
        33333

El for externo decide qué fila estamos construyendo, mientras que el for interno decide cuántas veces repetimos algo dentro de esa fila.
"""