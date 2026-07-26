#BUCLE WHILE - #EJERCICIO 4

print("\n--------- BIENVENIDO ----------")

"""
Mostrar números pares del 2 a 20. 
Crea un programa que imprima únicamente los números pares comprendidos entre 2 y 20 utilizando un bucle while.
"""

print("\n- Números pares del 2 al 20:")

inicializador = 2;

while inicializador <= 20:
    print(inicializador);
    inicializador = inicializador + 2;

#Explicación de Lógica
"""
- El while se ejecuta mientras el valor sea menor o igual a 20.
- Imprime el valor actual.
- Aumenta de 2 en 2, por lo que siempre obtiene números pares y evita tener que verificar si un número es par o impar.
"""
