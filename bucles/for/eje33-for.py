#BUCLE FOR - #EJERCICIO 33

print("\n--------- BIENVENIDO ----------")
"""
Suma de números positivos

Crea una lista que contenga números positivos, negativos y ceros.
Utiliza un for para recorrerla y calcula únicamente la suma de los números positivos.

Los números negativos deben ignorarse utilizando continue.
""" 

print("\n-- Suma de números positivos --")

print("Mi lista: ")
numeros = [-1,1,-2,0,2,3,-4,-5,0,-6,7,-9,10,11,-12,0,12,15]
print(numeros)
suma_positivos = 0

print("\n-- Aplicando la lógica --")
for contador in numeros:
    if contador < 0:
        continue;
    suma_positivos = suma_positivos + contador;
print("La suma total de los positivos es:", suma_positivos)

# Explicación de Lógica
"""
- Se crea una variable suma_positivos con valor inicial 0 para almacenar la suma acumulada.
- El for recorre cada número de la lista.
- El if verifica si el número es negativo.
- Si es negativo, continue lo ignora y pasa al siguiente número.
- Si el número no es negativo, se suma al acumulador suma_positivos.
- Al finalizar el recorrido, se muestra la suma total de los números positivos.
"""

#----------- espaciado final ---------------
print("\n")