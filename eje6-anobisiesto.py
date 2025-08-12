"""
Pide al usuario un año y determina si es bisiesto. Un año es bisiesto si:
- Si es divisible por 4, es bisiesto
- Si es divisible por 100, no es bisiesto
- Si es divisible por 400, es bisiesto. 
"""

print("BIENVENIDO")
entrada = int(input("Ingrese un año: "))

if (entrada % 4 == 0 and entrada % 100 != 0) or (entrada % 400 == 0):
    print("El año es bisiesto ")
else: 
    print("El año no es bisiesto")

"""
- Un año bisiesto es un año que tiene un día extra, 366 días en total, en lugar de los 365 días de un año común.

Bisiestos:
2000, 2004, 2012, 2016, 2020, 2024, 2400

No bisiestos:
1900, 2001,2010, 2015, 2019, 2023, 2100

"""