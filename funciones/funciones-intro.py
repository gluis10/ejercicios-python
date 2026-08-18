#FUNCIONES EN PYTHON

#¿Qué es una función en Python?

"""
Una función es un bloque de código que podemos crear una vez y reutilizar varias veces cuando lo necesitemos.
"""
print("---------- Ejemplo 1 función saludar ----------")
#Se define utilizando def:   
def saludar():
    print("Hola, ¿cómo estás?")

#Y para ejecutarla:
saludar()

#La idea principal es:
"""
- Definir una función = decirle a Python qué debe hacer.
- Llamar a la función = pedirle que lo haga.

Por ejemplo, si necesitas realizar una suma muchas veces, en lugar de escribir el mismo código repetidamente, puedes crear una función:
"""
print("\n---------- Ejemplo2 - función suma ----------")

def sumar():
    numero1 = 10
    numero2 = 5
    print(numero1 + numero2)

#Y después simplemente:
sumar()
sumar()
sumar()

"""
Más adelante aprenderás a enviar datos a las funciones mediante parámetros y a obtener un resultado mediante return. Pero inicialmente vamos a ir paso a paso.
"""



