#Acceso a curso especial → Pide la edad y si es estudiante (sí/no). Solo puede acceder si la edad está entre 18 y 25 y es estudiante. En cualquier otro caso, denegar el acceso.

#USANDO EL IF NOT

print("BIENVENIDO")
edad = int(input("Ingrese su edad: "))
estudiante = str(input("Es estudiante (si/no)?: "))

if not (18 <= edad <= 25 and estudiante == "si"):
    print("- Acceso denegado!")
else:
    print("- Puede acceder!")

