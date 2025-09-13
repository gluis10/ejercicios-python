#Edad para categoría → Pide la edad de una persona. Si la edad no está entre 0 y 120, muestra error. Si está entre 0 y 12, niño; entre 13 y 17, adolescente; entre 18 y 64, adulto; y 65 o más adulto mayor.

#USANDO EL IF NOT

print("BIENVENIDO")
edad = int(input("Ingrese su edad (0/120): "))

if not (0 <= edad <= 120):
    print("- La edad ingresada está fuera del rango (0/120)")
elif (edad <= 12):
    print("- Entra en el rango de niños!")
elif (edad <= 17):
    print("- Entra en el rango de adolencentes!")
elif (edad <= 64):
    print("- Entra en el rango de adulto!")
else: 
    print("- Entra en el rango de adulto mayor!")


