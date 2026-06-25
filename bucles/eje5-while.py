#BUCLE WHILE - #EJERCICIO 5

print("\n--------- BIENVENIDO ----------")

"""
Calcular la suma de los primeros 10 números. 
Utiliza un bucle while para sumar los números del 1 al 10 y mostrar el resultado final.

Eg: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
"""

inicializador = 1;
suma = 0;

while inicializador <= 10:
    print(inicializador)
    suma = suma + inicializador;
    inicializador = inicializador + 1;
print("La suma total del número 1 hasta 10 es: ", suma)

# Explicación de Lógica
"""
- Se inicializa la variable suma en 0 para almacenar el resultado acumulado.
- El while se ejecuta mientras el valor de inicializador sea menor o igual a 10.
- En cada iteración, se agrega el valor actual de inicializador a la variable suma.
- Luego se incrementa inicializador en 1 para pasar al siguiente número.
- Cuando el ciclo termina, la variable suma contiene la suma total de los números del 1 al 10.
"""
