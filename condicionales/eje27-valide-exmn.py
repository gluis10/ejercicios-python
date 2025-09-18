#Validación de examen final: Pide al usuario 4 notas entre 0 y 100 y determina el resultado: si todas son mayores o iguales a 90 debe imprimir “Aprobado con excelencia”, si todas son mayores o iguales a 60 pero al menos una es menor que 90 debe imprimir “Aprobado”, y si alguna es menor que 60 debe imprimir “Reprobado”. Además, valida que las notas estén en el rango de 0 a 100.

print("BIENVENIDO")
nota1 = float(input("Ingrese su primera nota: "))
nota2 = float(input("Ingrese su segunda nota: "))
nota3 = float(input("Ingrese su tercera nota: "))
nota4 = float(input("Ingrese su cuarta nota: "))

if not (0 <= nota1 <= 100 and 0 <= nota2 <= 100 and 0 <= nota3 <= 100 and 0 <= nota4 <= 100):
    print("- Una de las notas ingresadas está fuera del rango (0/100)")
elif (nota1 >= 90 and nota2 >= 90 and nota3 >= 90 and nota4 >= 90):
    print("- Aprobado con excelencia!")
elif (nota1 >= 60 and nota2 >= 60 and nota3 >= 60 and nota4 >= 60):
    print("- Aprobado!")
else:
    print("- Reprobado, estudie más huebón!")