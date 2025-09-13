#Validación de usuario → Pide el nombre de usuario y la contraseña, solo permite acceso si el usuario es “admin” y la contraseña es “1234”, en caso contrario imprime “Acceso denegado”.

print("BIENVENIDO")
name = str(input("Ingrese su nombre de usuario: "))
password = str(input("Ingrese su contraseña: "))

if (name == "admin" and password == "1234"):
    print("- Usuario ingresado correctamente!")
else:
    print("Acceso denegado!")
 


