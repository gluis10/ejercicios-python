#BUCLE FOR - CONTINUE - #EJERCICIO 21

print("\n--------- BIENVENIDO ----------")
"""
-- Omitir números pares — continue --
Mostrar únicamente números impares.
Utiliza un bucle for para recorrer los números del 1 al 20.
Utiliza continue para evitar imprimir los números pares.

Resultado esperado:
1
3
5
...
19
Aquí practicarás cómo continue salta una iteración y continúa con la siguiente.
"""

print("\n-- Omitir números pares — usando la función continue --")

for contador in range(1, 21):
    if contador % 2 == 0:
        continue;
    print(contador)

# Explicación de Lógica
"""
- El for recorre los números del 1 al 20.
- El if verifica si el número es par utilizando % 2 == 0.
- Si es par, continue salta esa iteración y pasa al siguiente número.
- Si es impar, se ejecuta el print() y se muestra el número.
"""
