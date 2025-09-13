#Verificación de acceso → Pide un usuario y una clave. El acceso se concede si el usuario es "admin" o "root", y la clave es "1234". En cualquier otro caso, imprime “Acceso denegado”.

print("BIENVENIDO")

user = str(input("Ingrese su usuario: "))
password = str(input("Ingrese su contraseña: "))

if (user == "admin" or user == "root") and (password == "1234"):
    print("- Acceso satisfactorio!")
else:
    print("- Credenciales incorrectas!")



