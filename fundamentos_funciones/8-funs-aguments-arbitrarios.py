#FUNCIONES - ARGUMENTOS ARBITRARIOS

print("\n-- Argumentos arbitrarios --")

def imprimir_info(**info):

    for clave, valor in info.items():
        print(f"{clave} : {valor}")

imprimir_info(nombre="Juan", edad=25, ciudad="Guate")

#Entonces
"""
Cuando coloco tres asteriscos antes del parámetros (**info), le estoy indicando a python que acepte cualquier número de argumentos de palabra clave y los enpaquete en un diccionario.
"""

#Argumentos arbitrarios = kwargs
