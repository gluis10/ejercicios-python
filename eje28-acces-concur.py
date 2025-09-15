#Acceso a concurso: Solicita la edad de una persona, si es miembro de un club (sí/no) y si tiene invitación (sí/no). La persona puede ingresar si tiene 18 años o más y es miembro, o si tiene una invitación; en cualquier otro caso el acceso debe ser denegado. También valida que la edad esté entre 0 y 120.

print("BIENVENIDO")
edad = int(input("Ingrese su edad: "))
miembro = str(input("Eres miembro del club? (si/no): ")).lower()
invitacion = str(input("Tiene invitación? (si/no): ")).lower()

if not (0 <= edad <= 120):
    print("- La edad ingresada está fuera del rango!")
elif (edad >= 18 and miembro == "si") or (invitacion == "si"):
    print("- Puede ingresar!")
else: 
    print("- Acceso denegado!")
