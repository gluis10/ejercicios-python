#BUCLE WHILE - #EJERCICIO 2

print("\n--------- BIENVENIDO ----------")

"""
Sacar raíz cuadrada de un número.
"""
import math

numero = int(input("\nDigite un número: "))

#Para sacar la raíz cuadrada de un número necesitamos que ese número sea positivo, entonces aquí es donde podemos utilizar el bucle while. 
#Mientras el número sea negativo el bucle se repite (vuelve a pedir el número!).

while numero<0:
    print("- Error!, el número ingresado es negativo.")
    numero = int(input("\n- Vuelve a digitar el número: "))
print("\nLa raíz cuadrada de", numero, "es: ", math.sqrt(numero))

"""
- Mientras la condición se cumple el bucle while se sigue ejecuntando.
- Cuando la condición deja de cumplirse el bucle deja de ejecutarse (se salta el while) y muestra el resultado.
"""


