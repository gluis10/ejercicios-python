#BUCLE FOR - #EJERCICIO 30

print("\n--------- BIENVENIDO ----------")
"""
Contar números pares e impares.

Crea una lista de números.
Utiliza un for para recorrerla y utiliza if para determinar cuáles son pares y cuáles impares.

Al finalizar, muestra:
    - Cantidad de números pares: X
    - Cantidad de números impares: Y
""" 

print("\n- Contar números pares e impares --")

print("Mi lista: ")
numeros = [1,2,5,10,13,15,16,20,23,30,32,34,35,40,45,48,49,50,58,60,70,100]
print(numeros)

contador_pares = 0;
contador_impares = 0;

for contador in numeros:
    if contador % 2 == 0:
        contador_pares = contador_pares + 1;
    else:
        contador_impares = contador_impares + 1;

print("\n- Cantidad de números pares encontrado: ", contador_pares)
print("- Cantidad de números impares encontrado: ", contador_impares)

# Explicación de Lógica
"""
- Se crean dos contadores: uno para números pares y otro para números impares.
- El for recorre cada número de la lista.
- El if verifica si el número es par utilizando % 2 == 0.
- Si es par, se incrementa contador_pares en 1.
- Si no es par, se incrementa contador_impares en 1.
- Al finalizar el recorrido, se muestra la cantidad de números pares e impares encontrados.
"""

#----------- espaciado final ---------------
print("\n")