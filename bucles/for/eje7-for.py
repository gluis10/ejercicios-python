#BUCLE FOR - #EJERCICIO 7

print("\n--------- BIENVENIDO ----------")
"""
Contar cuántas vocales tiene una palabra.
Solicita al usuario una palabra y utiliza un for para recorrer cada carácter y contar cuántas vocales contiene.

Ejemplo:
Ingrese una palabra: Programacion
La palabra contiene 5 vocales.
"""

print("\n-- Contar cuántas vocales tiene una palabra. --")
palabra = str(input("Ingrese una palabra: "))

contador_vocales = 0

for iterador in palabra:
    if (
        iterador == "a" or 
        iterador == "e" or 
        iterador == "i" or 
        iterador == "o" or 
        iterador == "u" or
        iterador == "A" or
        iterador == "E" or
        iterador == "I" or
        iterador == "O" or
        iterador == "U"
        ):
        contador_vocales = contador_vocales + 1;
print("\nEl caracter contiene", contador_vocales, "vocales.")

# Explicación de Lógica
"""
- Se solicita al usuario que ingrese una palabra y se almacena en la variable palabra.
- Se crea la variable contador_vocales y se inicializa en 0 para llevar el conteo de las vocales encontradas.
- Se utiliza un bucle for para recorrer cada carácter de la palabra uno por uno.
- En cada iteración, el carácter actual se almacena en la variable iterador.
- Se utiliza una condición if para comprobar si el carácter actual es una vocal.
- Se utiliza el operador or porque el carácter puede ser una vocal u otra: "a", "e", "i", "o", "u", incluyendo sus versiones mayúsculas.
- Si el carácter es una vocal, se aumenta el valor de contador_vocales en 1.
- Si el carácter no es una vocal, el contador no aumenta y el bucle continúa con el siguiente carácter.
- El proceso se repite hasta que el for haya recorrido todos los caracteres de la palabra.
- Una vez que el for termina, se muestra el total de vocales encontradas.
"""

"""
Aquí iterador irá tomando automáticamente cada carácter:
P → no es vocal
r → no es vocal
o → vocal → contador = 1
g → no es vocal
r → no es vocal
a → vocal → contador = 2
m → no es vocal
a → vocal → contador = 3
c → no es vocal
i → vocal → contador = 4
o → vocal → contador = 5
n → no es vocal
"""