#BUCLE WHILE - #EJERCICIO 7

print("\n--------- BIENVENIDO ----------")
"""
Contar cuántos dígitos tiene un número.
Pide al usuario un número entero positivo y determina cuántos dígitos contiene utilizando un bucle while.
"""

numero = int(input("\n- Digite un número  positivo: "));

while numero < 0:
    print("El número es negativo")
    numero = int(input("- Vuelva a digitar el número: "))

contador = 0;
while numero > 0:
    numero = (numero // 10)
    contador = contador + 1;
print("El número ingresado tiene: ", contador, "dígitos.")

#Dividir entre 10 usando el operador "//" elimina el último dígito de un número entero positivo.

# Explicación de Lógica
"""
- Se solicita al usuario un número positivo.
- Si el número es negativo, se muestra un mensaje y se vuelve a solicitar hasta que ingrese un valor válido.
- Se crea un contador para almacenar la cantidad de dígitos.
- El while se ejecuta mientras el número sea mayor que 0.
- En cada iteración se elimina el último dígito mediante una división entera entre 10.
- Cada vez que se elimina un dígito, el contador aumenta en 1.
- Cuando el número llega a 0, el contador contiene la cantidad total de dígitos del número ingresado.
"""

# Explicación detallada de la lógica
"""
- El operador // realiza una división entera, eliminando los decimales.
- Al dividir un número entre 10 usando //, se elimina el último dígito.
- Por ejemplo:
  1234 // 10 = 123
  123  // 10 = 12
  12   // 10 = 1
  1    // 10 = 0
- El while repite este proceso hasta que el número llega a 0.
- Cada vez que se elimina un dígito, el contador aumenta en 1.
- La cantidad de veces que se puede eliminar un dígito antes de llegar a 0 es exactamente la cantidad de dígitos que tiene el número.
"""

"""
El operador // en Python sirve para realizar la división entera. 
A diferencia de la división normal (/) que devuelve un número decimal.
Por ejemplo:
-- 10 / 3 #Resultado: 3.3333333333
-- 10 // 3 #Resultado: 3
"""

"""
Observa que:
1234 tiene 4 dígitos.
Fueron necesarias 4 vueltas para llegar a 0.
El contador terminó valiendo 4.
"""