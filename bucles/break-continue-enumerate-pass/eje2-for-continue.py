#CONTINUE - #EJERCICIO 2

print("\n--------- BIENVENIDO ----------")
"""
El continue se utiliza para saltar la iteración actual de un bucle y pasar directamente a la siguiente. A diferencia de break, no detiene el bucle completo.
"""

#Ejercicio
"""
Mostrar números omitiendo un valor específico.
Utiliza un bucle for para recorrer los números del 1 al 6.
Cuando el número sea igual a 4, utiliza continue para omitirlo
y continuar con la siguiente iteración.

El resultado debe mostrar:
1
2
3
5
6
"""

print("\n-- Mostrar números omitiendo el 4 --")

for numero in range(1, 7):
    if numero == 4:
        continue; #Omite este y continúa con el resto del bucle
    print("El número es: ", numero)
print("Bucle terminado")

# Explicación de Lógica
"""
- El for recorre los números del 1 al 6.
- Cuando numero vale 4, se ejecuta continue.
- continue omite esa iteración y pasa directamente al siguiente número.
- Por eso, el número 4 no se imprime.
"""