#Validación de notas múltiples → Pide tres notas (0 a 100). Si las tres son mayores o iguales a 60 → imprime “Aprobado”. Si al menos una es menor a 60 → imprime “Reprobado”.

print("BIENVENIDO")
nota1 = float(input("Ingrese su primera nota (0/100): "))
nota2 = float(input("Ingrese su segunda nota (0/100): "))
nota3 = float(input("Ingrese su tercera nota (0/100): "))

#VERSIÓN JUNIOR
# if (nota1 > 100 or nota1 < 0) or (nota2 > 100 or nota2 < 0) or (nota3 > 100 or nota3 < 0) :
#     print("- Una de las notas ingresadas está fuera del rango (0/100)!")
# elif (nota1 >= 60) and (nota2 >= 60) and (nota3 >= 60):
#     print("- Aprobado, felicidades!")
# else:
#     print("- Reprobado, estudie más!") 

#VERSION SENIOR - OPTIMIZADO
if not (0 <= nota1 <= 100 and 0 <= nota2 <= 100 and 0 <= nota3 <= 100):
    print("- Una de las notas ingresadas está fuera del rango (0/100)!")
elif (nota1 >= 60 and nota2 >= 60 and nota3 >= 60):
    print("- Aprobado, felicidades!")
else:
    print("- Reprobado, estudie más!") 

"""
- Si todas están en el rango → la condición es True, pero con not se vuelve False (no entra al if).
- Si alguna falla → el and ya da False, y con el not se vuelve True (entra al if).

Tú usaste or para comprobar error por error.
Yo GPT usé and + not para comprobar todo válido y luego negar.
Tu: Si alguna nota está fuera del rango 0–100, es error.
Yo GPT: Si no todas las notas están en el rango, es error.

"""


