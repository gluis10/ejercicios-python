#FUNCIONES - #EJERCICIO 2

print("\n--------- BIENVENIDO ----------")

"""
Función para mostrar números

Crea una función llamada mostrar_numeros() que utilice un for para mostrar los números del 1 al 10.
La función debe encargarse de todo el recorrido.
"""

print("\n-- Función para mostrar números --")

def mostrar_numeros():

    for numeros in range(1, 11):
        print(numeros)

mostrar_numeros()

# Explicación de Lógica
"""
- Se define la función mostrar_numeros() utilizando def.
- Dentro de la función se coloca un for que recorre los números del 1 al 10.
- range(1, 11) genera los valores del 1 al 10.
- print() muestra cada número durante el recorrido.
- Al escribir mostrar_numeros() se llama a la función y se ejecuta todo el for.
"""
