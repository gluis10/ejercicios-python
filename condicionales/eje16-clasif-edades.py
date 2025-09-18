#Clasificación de edades → Pide la edad de una persona e imprime: “Niño” si es menor de 12, “Adolescente” si está entre 12 y 17, “Adulto” si está entre 18 y 64, y “Adulto mayor” si tiene 65 o más.

print("BIENVENIDO")

edad = float(input("Ingrese su edad: "))

if (edad > 300 or edad < 0):
    print("La edad ingresada esta fuera del rango.")
elif (edad < 12):
    print("- Usted es aún un niño.")
elif (edad >= 12 and edad <= 17):
    print("- Usted entra en el rango de adolecentes.")
elif (edad >= 18 and edad <= 64):   
    print("- Usted entra en el rango de adultos")
else: 
    print("- Usted es adulto mayor.")


"""
RECOMENDACIÓN PARA SIMPLIFICAR EL CÓDIGO

No es tan necesario poner "edad >= 12" ni "edad >= 18", porque si el programa llega a ese elif, significa que ya no entró en los casos anteriores (edad < 12). Eso implícitamente asegura que la edad ya es mayor o igual a 12.

Porque el flujo del if/elif/else ya se encarga de que el número esté dentro del rango correcto ✅.
"""
