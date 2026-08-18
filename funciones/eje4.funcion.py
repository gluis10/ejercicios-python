#FUNCIONES - #EJERCICIO 4

print("\n--------- BIENVENIDO ----------")

"""
Función para calcular una suma

- Crea una función llamada sumar_numeros() que realice la suma de los números del 1 al 100 utilizando un for.
- Al finalizar, la función debe mostrar el resultado.
- Importante: intenta que la variable que almacena la suma exista dentro de la función.
"""

print("\n-- Función para calcular una suma --")

def sumar_numeros():

    acumulador = 0

    for suma in range(1,101):
        acumulador = acumulador + suma
    print("La suma de 1 al 100 es:", acumulador)

sumar_numeros()

# Explicación de Lógica
"""
- Se define la función sumar_numeros() utilizando def.
- Dentro de la función se crea acumulador con valor inicial 0.
- El for recorre los números del 1 al 100.
- En cada repetición, el número actual se suma al acumulador.
- Al terminar el recorrido, acumulador contiene la suma total.
- print() muestra el resultado dentro de la función.
- Al llamar a sumar_numeros(), se ejecuta todo el proceso.
"""

