#FUNCIONES - VALORES DE PARÁMETROS PREDETERMINADOS

print("\n-- Valores predeterminados de parámetros --")

def exponente(base, exponente=2):
    resultado = base ** exponente
    print(resultado)

#Llamada a la función sin expecificar el exponente
exponente(3)
"""
El numero 3 es elevado al valor por defecto que tengo en la variable exponente
"""

exponente(3, 3)
"""
El numero 3 es elevado al valor 3 que mandé como argumento.
"""
#Esto quire decir:
"""
La función está preparada para recibir el valor del exponente si así se desea, de lo contrario toma el valor que se estableció en la variable.
"""

