#BUCLE FOR - #EJERCICIO 31

print("\n--------- BIENVENIDO ----------")
"""
Saltar determinados números.

- Utiliza range() para recorrer los números del 1 al 30.
- Utiliza continue para evitar imprimir los números que sean múltiplos de 3.

El resultado debe mostrar todos los números excepto: 3, 6, 9, 12, 15...
""" 

print("\n-- Saltar determinados números --")

for contador in range(1, 31):

    if contador % 3 == 0:
        continue;
    print(contador)

# Explicación de Lógica
"""
- El for recorre los números del 1 al 30.
- El if verifica si el número es múltiplo de 3 utilizando % 3 == 0.
- Si es múltiplo de 3, continue omite esa iteración y pasa al siguiente número.
- Si no es múltiplo de 3, se ejecuta print() y se muestra el número.
"""

#----------- espaciado final ---------------
print("\n")

"""
Regla importante: la indentación define qué instrucciones pertenecen al for. Si una línea queda sin la indentación del bucle, se ejecutará después de que el bucle haya terminado.
"""