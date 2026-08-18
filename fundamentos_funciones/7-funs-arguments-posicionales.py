#FUNCIONES - ARGUMENTOS POSICIONALES O ARBITRARIOS

print("\n-- Argumentos posicionales arbitrarios --")

def suma_numeros(*numeros):
    resultado = sum(numeros)
    print(resultado)

suma_numeros(1, 2, 3, 4, 5)

#Entonces:
"""
Cuando coloco un asterisco antes del nombre del parámetro, le estoy indicando a python que acepte cualquier número de argumentos posicionales y los empaqueta en una tupla.
Por eso no tira error al mandarle muchos argumentos teniendo un solo parámetro.
"""

#Argumentos posicionales arbitrarios = args
