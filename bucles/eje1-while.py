#BUCLE WHILE - #EJERCICIO 1

"""
El bucle while en Python se utiliza para repetir un bloque de código mientras una condición sea verdadera. Primero se evalúa la condición; si es True, el código se ejecuta y vuelve a comprobar la condición. Este proceso se repite hasta que la condición sea False, momento en el que el bucle termina.
"""

print("\n--------- BIENVENIDO ----------")

print("\n--------- Ejemplo #1 ----------")
print("Imprimir los números de 1 al 5 usando el bucle while.")

contador = 1;

while contador <= 5:
    print(contador)
    contador = contador + 1;
    #Mod Senior contador += 1;

"""
En este ejemplo, el bucle imprime los números del 1 al 5 porque la variable contador aumenta en cada repetición hasta que deja de cumplir la condición "contador <= 5". Es importante modificar la variable de control dentro del bucle para evitar un ciclo infinito.
"""

#Llamada: "OPERADOR DE ASIGNACIÓN AUMENTADA o INCREMENTO" "contador = contador + 1" o "contador += 1".

"""
Su función es incrementar el valor de la variable en 1 cada vez que se ejecuta el bucle. Por ejemplo, si contador vale 1, después de "contador += 1" valdrá 2; luego 3, luego 4, y así sucesivamente.
"""
"""
Si no lo coloco (o no modifico la variable que controla la condición), el valor de contador nunca cambiará y la condición del while seguirá siendo verdadera, provocando un bucle infinito, porque así funciona el while.
"""

#Es decir, si solo pongo:
"""
contador = 1
while contador <= 5:
    print(contador)
"""
#Este código imprimirá 1 una y otra vez porque contador nunca aumenta.


print("\n--------- Ejemplo #2 ----------")
print("Imprimir o mostrar en pantalla Hola Mundo 10 veces")

inicilizador = 0;

while inicilizador < 10:
    print("Hola Mundo")
    inicilizador = inicilizador + 1;


