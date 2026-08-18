#FUNCIONES - SUMA UTULIZANDO EL RETURN

print("\n-- Suma con parámetros y argumentos --")

def suma(a, b, c):  #Parámetros
    resultado = a + b + c
    print(resultado)

suma(5, 3, 2)  #Argumentos

"""
Este función me funciona bien, sumando los tres números.

Sin embargo, pero qué pasaría si y quisiera utilizar este resultado (variable resultado) fuera de la función. Por ejemplo imprimir fuera la función la variable resultado!.

Pues me va a decir que la variable no existe, esto se debe a que la varible solo pertence dentro de la función. 

Entonces para eso existe el return. 
Es importante que una función retorne valores, ejemplo:
"""

print("\n-- Suma con parámetros y argumentos con retorno --")

def suma1(a, b):
    resultado = a + b
    return resultado

resultado_suma = suma1(3, 5)
print(resultado_suma)

"""
La declaración return permite a una función devolver el resultado en el punto de llamada. 
En este ejercicio quiere que cuando yo haga llamado a la función, me va a devolver el resultado de la suma. 
"""

print("\n-- Segunda forma para llamar la función --")

def suma2(a, b):
    resultado = a + b
    return resultado

print(suma2(4, 5))

#Es una forma más directa!

#Además!
"""
La declaración de return, no solo puede devolver un valor, sino también puede finalizar la ejecución inmediatamente.
"""
