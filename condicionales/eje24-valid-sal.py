#Validar salario → Pide el salario de una persona. Si no está en el rango de Q2,000 a Q10,000, muestra que está fuera del rango permitido; de lo contrario, confirma que es válido.

#USANDO EL IF NOT

print("BIENVENIDO")
salario = float(input("Ingrese su salario: "))

if not (2000 <= salario <= 10000):
    print("- El salario está fuera del rango (2000/10000)!")
else:
    print("- Salario válido")
