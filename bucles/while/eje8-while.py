#BUCLE WHILE - #EJERCICIO 8

print("\n--------- BIENVENIDO ----------")
"""
Validar una contraseña.
Define una contraseña correcta en el programa. Solicita al usuario que la ingrese repetidamente hasta que escriba la contraseña correcta.
"""
password = "GLuis#123!";
correctpass = str(input("\n- Ingrese la contraseña correcta: "))

while correctpass != password:
    print("Contraseña incorrecta!")
    correctpass = str(input("- Vuelva a ingresar la contraseña: "))
print("-Contraseña ingresada correctamente.")

# Explicación de Lógica
"""
- Se define una contraseña correcta en el programa.
- Se solicita al usuario que ingrese una contraseña.
- El while se ejecuta mientras la contraseña ingresada sea diferente de la contraseña correcta.
- Si la contraseña es incorrecta, se muestra un mensaje y se vuelve a solicitar.
- Cuando el usuario ingresa la contraseña correcta, la condición del while deja de cumplirse y el ciclo termina.
- Finalmente, se muestra un mensaje indicando que la contraseña fue ingresada correctamente.
"""