#Número múltiplo → Pide un número e imprime si es múltiplo de 3 y de 5 al mismo tiempo, si solo es múltiplo de uno de ellos, o si no es múltiplo de ninguno.

print("BIENVENIDO")
print("Validar si el número es múltiplo de 3 y 5 o solo uno de ellos o ninguna.")
numero = float(input("Ingrese un número: "))

if (numero % 3 == 0 and numero % 5 == 0):
    print("- El número es múltiplo de 3 y 5.")
elif (numero % 3 == 0) or (numero % 5 == 0):
    print("- El número solo es múltiplo de uno de ellos.")
else:
    print ("- El número no es múltiplo de ninguno de ellos.")
    
"""
- 15 y 30 es múltiplo de uno de ellos.
- 12, 18 o 20 es múltiplo de uno de ellos.
- 8, 11 o 19 o es múltiplo de ninguno de ellos.
"""
