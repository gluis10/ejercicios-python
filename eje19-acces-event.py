#Acceso a evento → Pide la edad y si tiene invitación (sí/no). Puede entrar si tiene invitación o si tiene 18 años o más. Si no, acceso denegado.

print("BIENVENIDO")
edad = int(input("Ingrese su edad: "))
invitacion = str(input("Tiene invitación (si/no): "))

if (edad >= 18 or invitacion == "si"):
    print("- Puede ingresar!")
else:
    print("- Acceso denegado, no cumple con los requisitos!")

