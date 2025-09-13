#Validar número positivo → Pide un número y valida que no sea negativo. Si es negativo muestra un error, si no, confirma que es válido.

#USANDO EL IF NOT

print("BIENVENIDO")
numero = float(input("Ingrese un número: "))

if not (numero >= 0):
    print("- El número es negativo!")
else:
    print("El número es positivo")