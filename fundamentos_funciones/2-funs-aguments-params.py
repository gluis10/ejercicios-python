#FUNCIONES - ARGUMENTOS Y PARÁMETROS

#Parámetros
"""
Los parámetros son variables utilizadas por una función para recibir información necesaria para realizar una tarea en específico.
"""

#Argumentos
"""
Cuando se llama a una función, los valores que se le pasan a dicha función, se le llaman argumentos.
"""
print("\n-- Funciones como parámetro y argumento --")

def saludar(nombre):
    mensaje = print(f"\nHola {nombre}, bievenido al curso de funciones!")
    print(mensaje)

saludar("Harry Potter")

#Qué pasa si "saludar()" final lo dejo vacío?
"""
Si "saludar()" lo dejo vacío, da error, eso se debe porque no le estoy mandando la información que esperar recibir la función (saludar(nombre)). Es decir, el parámetro "nombre" significa que la función está esperando algo.
"""

#Entonces:
"""
    - nombre: Es el parámetro
    - Harry: Es el argumento
"""

"""
    - Cuando una función recibe un valor, se le conoce como parámetro.
    - Cuando hacemos llamado a una función y le enviamos información, se le conoce como argumento.
"""