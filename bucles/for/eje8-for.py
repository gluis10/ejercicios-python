#BUCLE FOR - #EJERCICIO 8

print("\n--------- BIENVENIDO ----------")
"""
Contar cuántas letras "a" existen en una frase.
Solicita una frase al usuario y cuenta cuántas veces aparece la letra a.

Opcional: considera también la A mayúscula.
"""

print("\n-- Contar cuántas letras A existen en una frase. --")
frase = str(input("Ingrese una frase: "))

contador_a = 0;

for contador in frase:
    if (contador == "a" or contador == "A"):
        contador_a = contador_a + 1;
print("\n - En la frase ingresada, la letra A se repite", contador_a, "veces.")

# Explicación de Lógica
"""
- Se solicita al usuario que ingrese una frase y se almacena en la variable frase.
- Se crea la variable contador_a y se inicializa en 0 para llevar el conteo de las letras "a" encontradas.
- Se utiliza un bucle for para recorrer uno por uno todos los caracteres de la frase.
- En cada iteración, el carácter actual se almacena en la variable contador.
- Se utiliza una condición if para verificar si el carácter actual es la letra "a" minúscula o la letra "A" mayúscula.
- Se utiliza el operador or porque el carácter puede ser "a" o "A".
- Si el carácter coincide con alguna de estas dos opciones, se aumenta el contador_a en 1.
- Si el carácter no es una "a" ni una "A", el contador no aumenta y el for continúa con el siguiente carácter.
- El proceso se repite hasta que el for haya recorrido todos los caracteres de la frase.
- Una vez finalizado el ciclo, se muestra el total de veces que apareció la letra "a", considerando tanto mayúsculas como minúsculas.
"""

