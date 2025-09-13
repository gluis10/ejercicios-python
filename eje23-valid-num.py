#Validar usuario → Pide un nombre de usuario. Si el usuario no es "admin", imprime acceso denegado, de lo contrario acceso permitido.

#USANDO EL IF NOT

print("BIENVENIDO")
usuario = str(input("Ingrese su nombre: "))

if not (usuario == "admin"):
    print("- Acceso denegado")
else: 
    print("- Acceso satisfactorio!")

