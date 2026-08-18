#FUNCIONES - #EJERCICIO 3

print("\n--------- BIENVENIDO ----------")

"""
Función para mostrar números pares

Crea una función llamada numeros_pares() que utilice un for para mostrar todos los números pares del 2 al 20.
Cuando termines, llama a la función desde el programa principal.
"""

print("\n-- Función para mostrar números pares --")

def numeros_pares():
    for numeros in range(2,21,2):
        print(numeros)

numeros_pares()

# Explicación de Lógica
"""
- Se define la función numeros_pares() utilizando def.
- Dentro de la función se utiliza un for para recorrer los números pares.
- range(2, 21, 2) comienza en 2, llega hasta 20 y aumenta de 2 en 2.
- print() muestra cada número par durante el recorrido.
- Al llamar a numeros_pares(), se ejecuta la función y se muestran los números.
"""

