#BUCLE WHILE - #EJERCICIO 6

print("\n--------- BIENVENIDO ----------")

"""
Tabla de multiplicar de un número.
Solicita al usuario un número y muestra su tabla de multiplicar del 1 al 10 utilizando un bucle while.
"""

contador = 1;
numero = int(input("\nDigite un número: "))

while contador <= 10:
    resultados = numero * contador;
    print(numero, "x", contador, "=", resultados)
    contador = contador + 1;

"""
- numero nunca cambia.
- contador va de 1 a 10.
- resultado se recalcula en cada iteración.
"""

# Explicación de Lógica
"""
- Se solicita al usuario un número para generar su tabla de multiplicar.
- Se crea un contador que inicia en 1.
- El while se ejecuta mientras el contador sea menor o igual a 10.
- En cada iteración se multiplica el número ingresado por el contador.
- Se muestra la operación y su resultado.
- El contador aumenta en 1 hasta llegar a 10.
"""