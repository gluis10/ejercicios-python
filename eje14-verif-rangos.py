#Verificación de rangos dobles → Pide un número e imprime “Está dentro del rango permitido” si el número está entre 1 y 10 o entre 20 y 30 (incluyendo ambos), en caso contrario imprime “Fuera del rango”.

print("BIENVENIDO")
numero = float(input("Ingrese un número: "))

if (numero >= 1 and numero <=10) or (numero >= 20 and numero <= 30):
    print("- Está dentro del rango permitido.")
else:
    print("El número está fuera del rango.")

