#FUNCIONES - #EJERCICIO 5

print("\n--------- BIENVENIDO ----------")

"""
Función para determinar si un número es par o impar

- Crea una función llamada verificar_numero().
- La función debe solicitar al usuario un número y determinar si es par o impar.
Por ejemplo: 
    - Ingrese un número: 8
    - El número 8 es par.
O:
    - Ingrese un número: 7
    - El número 7 es impar.
"""

print("\n-- Función para determinar si un número es par o impar --")

def verificar_numero():
    numero = int(input("Ingrese un número: "))

    if numero % 2 == 0:
        print("\n- El número", numero, "es par.")
    else:
        print("\n- El número", numero, "es impar.")

verificar_numero()

# Explicación de Lógica
"""
- Se define la función verificar_numero() utilizando def.
- Dentro de la función se solicita al usuario un número y se almacena en numero.
- El if utiliza % 2 para comprobar si el número es divisible entre 2.
- Si el resultado es 0, el número es par.
- Si no es 0, el número es impar y se ejecuta el else.
- Al llamar a verificar_numero(), se ejecuta toda la lógica de la función.
"""

