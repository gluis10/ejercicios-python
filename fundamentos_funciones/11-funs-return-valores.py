#FUNCIONES - RETURN MULTIPLES

print("\n-- Operaciones básicas --")

def operaciones_basicas(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    return suma, resta, multiplicacion, division

resultado_operaciones = operaciones_basicas(8, 4)
print(resultado_operaciones)

"""
Esto nos retorna el resultado en formato de tupla!
"""



