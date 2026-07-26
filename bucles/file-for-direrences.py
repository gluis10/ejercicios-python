#BUCLE WHILE AND FOR - #DIFERENCIAS

#Diferencia principal entre while y for

#WHILE
"""
Se usa cuando no sabemos exactamente cuántas veces se repetirá el ciclo.

- Necesita una condición (while numero <= 10).
- Normalmente debes modificar manualmente el contador (numero += 1).

Por ejemplo, con while hacías algo así:

    contador = 1
    while contador <= 5:
        print(contador)
        contador += 1
"""

#FOR
"""
Se usa cuando sí sabemos cuántas veces se repetirá el ciclo.

- Generalmente utiliza range() para indicar el rango de repeticiones.
- El contador avanza automáticamente.

Con for, Python se encarga del incremento:

    for contador in range(1, 6):
        print(contador)
"""
"""
¿Qué es range()?
Es una función muy utilizada con for y sirve para generar secuencias de números.
- range(inicio, fin)
- Ejemplo: range(1, 6) imprime: 1, 2, 3, 4, 5
- El número final no se incluye.
"""
"""
Cómo leer un for

    for numero in range(1, 6):
        print(numero)

Se puede leer como:
"Para cada número dentro del rango del 1 al 5, imprime el número."
"""
"""
Ventajas del for
- Menos código.
- Menos posibilidades de olvidar incrementar el contador.
- Más legible cuando el número de repeticiones es conocido.
"""

#UNA REGLA RÁPIDA PARA RECORDAR
"""
Si piensas:
"Repetir hasta que ocurra algo"
normalmente usarás while.

Si piensas:
"Repetir exactamente X veces"
normalmente usarás for.
"""
