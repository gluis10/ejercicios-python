"""
Pide al usuario un año y determina si es bisiesto. Un año es bisiesto si:
- Si es divisible por 4, es bisiesto
- Si es divisible por 100, no es bisiesto
- Si es divisible por 400, es bisiesto. 
"""

print("BIENVENIDO")

entrada = int(input("Ingrese un año random: "))

if (entrada % 4 == 0 and entrada % 100 != 0):
    print("El año es bisiesto!")
elif (entrada % 400 == 0):
    print("El año es bisiesto!")
else:
    print("El año no es bisiesto!")

"""
- Un año bisiesto es un año que tiene un día extra, 366 días en total, en lugar de los 365 días de un año común.

Años bisiestos (ejemplos):
1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096.

Años no bisiestos (ejemplos):
2021, 2022, 2023, 2025, 2026, 2027, 2029, 2030, 2031, 2033, 2034, 2035, 2037, 2038, 2039.

"""