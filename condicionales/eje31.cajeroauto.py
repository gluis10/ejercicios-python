#Hacer un programa que simule un cajero automático con un saldo inicial de Q1000 y tendrá el siguiente menú de opciones:

#Ingresar dinero en la cuenta
#Retirar dinero de la cuenta
#Mostrar dinero disponible
#Salir

print("BIENVENIDO")
saldo = 1000; #Salfo inicial en la cuenta

print("\t:MENÚ DE OPCIONES:." );
print("1. Ingresar dinero en la cuenta")
print("3. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")
opcion = int(input("Digite una opción de menú: "))

print()

if (opcion == 1):
    extra = float(input("Cuánto dinero desea ingresar?: "))
    saldo = saldo + extra;
    print(f"El dinero en la cuenta es: {saldo}")
elif (opcion == 2):
    retirar = float(input("Cuánto dinero desea retirar?: "))
    #El usuario no puede retirar más dinero de lo existente
    if (retirar>saldo):
        print("No tiene esa cantidad de dinero!")
    else:
        saldo = saldo - retirar;
        print()
        print(f"El dinero en la cuenta es: {saldo}")
elif (opcion == 3):
    print(f"El dinero en la cuenta es: {saldo}")
elif (opcion == 4):
    print("Gracias por utlizar el cajero!")
else:
    print("Opción de menú elegido no existe!")

#test