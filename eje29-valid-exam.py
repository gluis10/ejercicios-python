#Validación de examen múltiple: Pide tres notas de 0 a 100 y un porcentaje de asistencia (0 a 100). El estudiante aprueba si todas las notas son mayores o iguales a 60 y la asistencia es mayor o igual a 75%, y reprueba si alguna nota es menor a 60 o la asistencia es menor a 75%. También valida que tanto las notas como la asistencia estén dentro de sus rangos correspondientes.

print("BIENVENIDO")
nota1 = float(input("Ingrese su nota1 (0/100): "))
nota2 = float(input("Ingrese su nota2 (0/100): "))
nota3 = float(input("Ingrese su nota3 (0/100): "))
asistencia = int(input("Ingrese su porcentaje de asistencia (0/100): "))

if not(0 <= nota1 <= 100 and 0 <= nota2 <= 100 and 0 <= nota3 <= 100 and 0 <= asistencia <= 100):
    print("- Una de las notas ingresadas o el porcentaje está fuera del rango!")
elif (nota1 >= 60 and nota2 >= 60 and nota3 >= 60 and asistencia >= 75): 
    print("- Aprobado, felicidades!")
else:
    print("- Reprobado, estudie más huebón!")


