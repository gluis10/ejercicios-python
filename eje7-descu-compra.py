#Descuento por compra → Pide el total de la compra y aplica un 10% de descuento si es mayor a Q100, o 20% si es mayor a Q500.

print("BIENVENIDO")
totalcompra = float(input("Ingrese el total de la compra: "))

#NIVEL SENIOR
if (totalcompra > 500):
    totalfinal = totalcompra - (totalcompra * 0.20)
    print(f"El tota de la compra sin descuento es {totalcompra}")
    print("El total de la compra con descuento es: ", totalfinal)
elif (totalcompra > 100):
    totalfinal = totalcompra - (totalcompra * 0.1)
    print(f"El tota de la compra sin descuento es {totalcompra}")
    print("El total de la compra es: ", totalfinal)
else:
    print("El total de la compra es: ", totalcompra)
 
#NIVEL JUNIOR
# if (totalcompra > 500):
#     descuento = totalcompra * 0.20;   
#     totalfinal = totalcompra - descuento;
#     print("El total de la compra es: ", totalfinal)
# elif (totalcompra > 100):
#     descuento = totalcompra * 0.1;
#     totalfinal = totalcompra - descuento;
#     print("El total de la compra es: ", totalfinal)
# else:
#     print("El total de la compra es: ", totalcompra)


"""
Windows/Linux: Ctrl + K seguido de Ctrl + C para comentar, y Ctrl + K seguido de Ctrl + U para descomentar.
"""

#print(f"El numero mayor es: {num2}") 