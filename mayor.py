#Pide dos números e imprime cuál es el mayor. Si son iguales, indícalo.

print("BIENVENIDO")
num1 = int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero: "))

if (num1>num2):
    print("El número mayor es: ", num1)
elif (num1<num2):
    print(f"El numero mayor es: {num2}") 
else:
    print("Los números son iguales.")
