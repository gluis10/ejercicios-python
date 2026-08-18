#BUCLE FOR - #EJERCICIO 34

print("\n--------- BIENVENIDO ----------")

"""
Encontrar el número mayor.

Crea una lista de números.
Utiliza un for para recorrerla y determina cuál es el número mayor sin utilizar max().

Al finalizar, muestra el número mayor encontrado.
"""

print("\n-- Encontrar el número mayor --")

print("Mi lista: ")
numeros = [1, 2, 5, 10, 13, 15, 16, 20, 23, 30, 32, 34, 35, 40, 45, 48, 49, 50, 58, 60, 70, 85]
print(numeros)

mayor = numeros[0]

for indice, valor in enumerate(numeros):
    if valor < mayor:
        continue
    mayor = valor

print("El número mayor es:", mayor)


# Explicación de Lógica
"""
- Se crea una lista de números.
- mayor = numeros[0] toma el primer número de la lista como referencia inicial para comenzar la comparación.
- enumerate() recorre la lista proporcionando la posición y el valor de cada elemento.
- El if verifica si el valor actual es menor que mayor.
- Si es menor, continue lo ignora y pasa al siguiente número.
- Si el valor es mayor o igual, mayor = valor actualiza la variable mayor con ese nuevo número.
- Al finalizar el recorrido, mayor contiene el número más grande de toda la lista y se muestra en pantalla.
"""

#----------- espaciado final ---------------
print("\n")