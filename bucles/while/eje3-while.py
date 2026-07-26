#BUCLE WHILE - #EJERCICIO 3

print("\n--------- BIENVENIDO ----------")

"""
Imprimir números del 10 al 1. 
Utiliza un bucle while para mostrar en pantalla los números del 10 al 1 en orden descendente.
"""
print("\n- Números del 10 hasta 1, en orden Descendente:")
inicializador = 10;

while inicializador > 0:
    print(inicializador)
    inicializador = inicializador - 1;

#--------------------------------------------------------
print("\n- Números del 1 hasta 10, en orden Ascendente:")
inicializador = 0;

while inicializador <= 10:
    print(inicializador)
    inicializador = inicializador + 1;

#Explicación de Lógica
"""
- Crea una variable de control (inicializador).
- El while se ejecuta mientras la condición sea verdadera.
- En cada iteración imprime el valor actual.
- Luego modifica la variable para acercarse al fin del ciclo, restando 1 para ir de 10 a 1.
"""
