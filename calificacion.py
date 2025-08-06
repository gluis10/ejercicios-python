#Solicita una calificación del 0 al 100 e indica si el estudiante aprueba (>=60) o reprueba (<60).

print("BIENVENIDO")
calificacion = float(input("Ingrese una calificación del 0 al 100: "))

if (calificacion > 100 or calificacion < 0):
    print("Calificación fuera de rango!.")
elif (calificacion >= 60):
    print("Usted aprobó el examen, felicidades!.")
else:
    print("Usted reprobó el examen, estudie más!.")

