#Clasificación de números → Pide un número e imprime si es positivo par, positivo impar, negativo par, negativo impar, o cero.

print("BIENVENIDO")
numero = float(input("Ingrese un número: "))

if (numero > 0 and numero % 2 == 0):
    print("- El número es positivo par.")
elif (numero > 0 and numero % 2 != 0):
    print("- El número es positivo impar.")
elif (numero < 0 and numero % 2 == 0):
    print("- El número es negativo par.")
elif (numero < 0 and numero % 2 != 0):
    print("- El número es negativo impar.")
else: 
    print("- El número es 0.")
