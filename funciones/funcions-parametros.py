#FUNCIONES - PARÁMETROS

#¿Qué es un parámetro?
"""
Un parámetro es una variable que colocamos dentro de los paréntesis de una función para recibir un dato desde fuera.
"""

print("\n-- Ejemplo1 de parámetro - saludar --")

def saludar(nombre):
    print("Hola", nombre)

saludar("Harry Potter")

# Explicación de Lógica
"""
- Se define la función saludar() y se establece el parámetro nombre.
- nombre funciona como una variable que recibirá un valor cuando se llame a la función.
- print() utiliza ese valor para mostrar el saludo.
- Al llamar saludar("Harry Potter"), el texto "Harry Potter" se guarda temporalmente en nombre.
- La función imprime: Hola Harry Potter.
"""
#Idea clave:
"""
- nombre es el parámetro y "Harry Potter" es el argumento que le estamos pasando a la función.

Puedes imaginarlo como:
Parámetro = espacio que la función prepara para recibir un dato.
"""

print("\n-- Ejemplo2 de parámetro - suma --")

def suma(x, y, z):
    resultado = x + y + z
    print(resultado)

suma(5, 6, 8)
suma(4, 6, 5)
suma(3, 8, 2)

# Explicación de Lógica
"""
- Se define la función suma() con tres parámetros: x, y y z.
- La función suma los tres valores y guarda el resultado en resultado.
- print() muestra el resultado de la suma.
- Cada llamada a suma() proporciona tres valores diferentes para realizar una nueva suma.
"""
"""
En cada llamada, los valores reemplazan temporalmente a x, y y z. Por ejemplo, suma(5, 6, 8) significa x = 5, y = 6, z = 8.
"""