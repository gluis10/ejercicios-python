#FUNCIONES - ARGUMENTOS CON PALABRAS CLAVES

print("\n-- Argumentos con palabras claves --")

"""
Cuando utilizamos argumentos con palabras claves, el orden no importa.
"""

def saludar(nombre, saludo):
    mensaje = print(f"\n{saludo} {nombre}!")
    print(mensaje)

saludar(saludo="Hola", nombre="Harry Potter")

"""
Entonces puedo colocar los argumentos en cualquier orden, siempre y cuando yo establezca la palabra clave y así colocar cada valor en el lugar correcto.
"""
