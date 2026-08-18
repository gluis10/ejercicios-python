#FUNCIONES - RETURN MULTIPLES DECLARACIONES

print("\n-- Verificar si un número es negativo, positivo o cero --")

def funcion_condicional(valor):

    if valor > 0:
        return "Positivo"
    elif valor < 0:
        return "Negativo"
    else:
        return "Cero"

#Podemos llamarla múltiples veces
resultado = funcion_condicional(-7)
print(resultado)

resultado = funcion_condicional(5)
print(resultado)

resultado = funcion_condicional(0)
print(resultado)


