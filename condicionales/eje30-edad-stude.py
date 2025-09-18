#Pide la edad de un estudiante, tres notas (0/100) y el porcentaje de asistencia (0/100). El estudiante aprueba si todas sus notas son mayores o iguales a 60 y la asistencia es al menos del 75%. Si tiene todas las notas mayores o iguales a 85 y la asistencia es mayor o igual a 90%, aprueba con excelencia. Sin embargo, si el estudiante es menor de 18 años y tiene invitación especial (responder “si”), podrá aprobar incluso si no cumple con los requisitos normales.

print("BIENVENIDO")
edad = int(input("Ingrese su edad: "))
nota1 = float(input("Ingrese su nota1 (0/100): "))
nota2 = float(input("Ingrese su nota2 (0/100): "))
nota3 = float(input("Ingrese su nota3 (0/100): "))
asistencia = int(input("Ingrese su porcentaje de asistencia (0/100): "))
invitacion = str(input("- Tiene invitacion (no/si)?: ")).lower()

if not (0 <= nota1 <= 100 and 0 <= nota2 <= 100 and 0 <= nota3 <= 100 and 0 <= asistencia <= 100):
    print("- Una de las notas ingresadas o el porcentaje está fuera del rango!")
elif (nota1 >= 85 and nota2 >= 85 and nota3 >= 85 and asistencia >= 90):
    print("- Aprobado con Excelencia, felicidades!")
elif (nota1 >= 60 and nota2 >= 60 and nota3 >= 60 and asistencia >= 75): 
    print("- Aprobado, felicidades!")
elif (edad < 18 and invitacion == "si"):
    print("- Aprobado")
else:
    print("- Reprobado, estudie más huebón!")




