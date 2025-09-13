#Clasificación de notas → Pide una nota del 0 al 100 e imprime “Excelente” si es mayor o igual a 90, “Aprobado” si es mayor o igual a 70 y menor a 90, y “Reprobado” si es menor a 70.

print("BIENVENIDO")
nota = float(input("Ingrese su nota final (0/100): "))

if (nota > 100 or nota < 0):
    print("-La nota ingresada esta fuera del rango (0/100)")
elif (nota >= 90):
    print("-Excelente")
elif (nota >= 70):
    print("-Aprobado")
else: 
    print("-Reprobado")

"""
Windows/Linux: Ctrl + K seguido de Ctrl + C para comentar, y Ctrl + K seguido de Ctrl + U para descomentar.
"""