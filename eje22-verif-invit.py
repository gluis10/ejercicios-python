#Verificación de invitación → Pide si tienes invitación (sí/no). Si la respuesta no es "sí", muestra que no puede ingresar, en caso contrario permite el acceso.

#USANDO EL IF NOT

print("BIENVENIDO")
invitacion = str(input("Tiene invitación (si/no)?: "))

if (invitacion not in ("si", "no")):
    print("- Opción de respuesta incorrecta (si/no)")
elif not (invitacion == "si"):
    print("- No puede ingresar sin invitación!")
else:
    print("- Puede ingresar!")