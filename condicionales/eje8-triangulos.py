#Clasificación de triángulo → Ingresa tres lados y determina si el triángulo es equilátero, isósceles o escaleno.
# Equilátero → los 3 lados son iguales.
# Isósceles → exactamente 2 lados son iguales.
# Escaleno → los 3 lados son diferentes.

print("BIENVENIDO")
lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))

#Condición para que los lados formen un triángulo
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1): 
    if (lado1 == lado2 and lado2 == lado3):
        print("El triángulo es equilátero")
    elif (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")
else:
    print("Los lados ingresados no forman un triángulo")

#print(f"El numero mayor es: {num2}")           

