#Acceso a descuento especial → Pide la edad y si es estudiante (sí/no). Si la persona es menor de 18 o es estudiante, obtiene descuento.

print("BIENVENIDO")
edad = int(input("- Ingrese su edad: "))
estudiante = str(input("- Eres estudiante? (si/no): "))

if (edad < 18 or estudiante == "si"):
    print("Tienes un descuento")
else: 
    print("No tienes descuento")

