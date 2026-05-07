#Validación de usuario → Pide el nombre de usuario y la contraseña, solo permite acceso si el usuario es “admin” y la contraseña es “1234”, en caso contrario imprime “Acceso denegado”. Validar si el usuario o la contrase esta incorrecta.

print("BIENVENIDO")
name = str(input("Ingrese su nombre de usuario: "))
password = str(input("Ingrese su contraseña: "))

if (name == "admin" and password == "1234"):
    print("- Credenciales ingresado correctamente!")
elif (name == "admin" and password != "1234"):
    print("La contraseña es incorrecta!")
elif (name != "admin" and password == "1234"):
    print("El usuario es incorrecto!")
else:
    print("El usuario y contraseña son incorrectas!")
 



