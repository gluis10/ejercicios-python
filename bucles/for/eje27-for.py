#BUCLE FOR - #EJERCICIO 27

print("\n--------- BIENVENIDO ----------")
"""
Mostrar solamente números positivos.
Crea una lista que contenga números positivos y negativos.

Utiliza un for para recorrerla y muestra únicamente los números positivos.
Utiliza continue para ignorar los números negativos.
"""
print("Mi lista: ")
numeros = [-1,1,-2,2,3,-4,-5,-6,7,-9,10,11,-12,12,15]
print(numeros)

print("\n-- Mostrar solamente números positivos --")

for iterador in numeros:
    if iterador < 0:
        continue;
    print(iterador)

# Explicación de Lógica
"""
- Se crea una lista con números positivos y negativos.
- El for recorre cada número de la lista.
- El if verifica si el número es negativo.
- Si es negativo, continue omite esa iteración y pasa al siguiente número.
- Si el número es positivo, se muestra en pantalla.
"""

#----------- espaciado final ---------------
print("\n")