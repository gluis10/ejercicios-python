#Edad para votar y licencia → Pide la edad y pregunta si tiene licencia (sí/no). Imprime si puede manejar legalmente (se necesita ser mayor o igual a 18 y tener licencia).

print("BIENVENIDO")

edad = int(input("-Ingrese la edad: "))
licencia = str(input("-Tiene licencia (si/no): "))

if (edad >= 18 and licencia == "si"):
    print("Puede conducir")
else:
    print("No puede conducir")

"NIVEL JUNIOR"
# if (licencia == "no" and edad >= 18) or (licencia == "si" and edad < 18):
#     print("No puede conducir")
# elif (licencia == "si" and edad >= 18):
#     print("Puede conducir")
# else:
#     print("No puede conducir")
    



"""
Windows/Linux: Ctrl + K seguido de Ctrl + C para comentar, y Ctrl + K seguido de Ctrl + U para descomentar.
"""
