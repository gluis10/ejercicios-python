#FUNCIONES - ARGS y KWARGS

print("\n-- Parámetros en tipo args y wargs --")

def funcion_combinada(*args, **kwargs):
    print("Argumentos posicionales: ", args)
    print("Argumentos de palabra clave: ", kwargs)

funcion_combinada(1, 2, 3, nombre="Harry", edad=25)

"""
Estos son las alternativas que tenemos para poder enviar una cantidad variable de argumentos aunque no hayamos establicido una cantidad de parámetros, que es lo que vamos a recibir. Por eso, nos lo empaqueta en estructura de datos, tupla o diccionario.
"""

"""
args = formato de tupla
kwargs = formato de diccionario
"""


