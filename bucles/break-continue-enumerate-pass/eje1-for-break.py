#BREAK - #EJERCICIO 1

print("\n--------- BIENVENIDO ----------")
"""
El break se utiliza para detener inmediatamente un bucle (for o while), aunque todavía queden iteraciones por realizar.
"""
#Ejercicio
"""
Crear un programa que recorra los números del 1 al 10 utilizando un bucle for. El programa debe detener el bucle cuando encuentre el número 6 utilizando break. Finalmente, debe mostrar un mensaje indicando que el bucle ha terminado.
"""

print("\n-- Uso del break --")

for numero in range(1, 11):
    if numero == 6:
        break; #Detén el bucle ahora mismo.
    print("El número es: ", numero)
print("Bucle terminado")

# Explicación de Lógica
"""
- El for recorre los números del 1 al 10.
- Cuando numero llega a 6, la condición if se cumple.
- break detiene inmediatamente el bucle.
- Por eso, solo se imprimen los números del 1 al 5.
- Después, el programa continúa ejecutando el código que está fuera del for.
"""

"""
Break te da un uso muy común es cuando estás buscando algo y, al encontrarlo, ya no necesitas seguir recorriendo los elementos.
"""

