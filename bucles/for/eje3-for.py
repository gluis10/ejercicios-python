#BUCLE FOR - #EJERCICIO 3

print("\n--------- BIENVENIDO ----------")
"""
Mostrar únicamente los números pares del 2 al 20.
Crea un programa que imprima solamente los números pares comprendidos entre 2 y 20.
"""
print("\n-- Mostrar únicamente los números pares del 2 al 20 --")

for contador in range(2, 22, 2):
    print(contador)

# Explicación de Lógica
"""
- Se utiliza un bucle for para repetir una acción varias veces de forma automática.
- La función range(2, 22, 2) genera una secuencia de números desde el 2 hasta el 20.
- El primer parámetro (2) indica el número inicial de la secuencia.
- El segundo parámetro (22) indica el límite final, pero este valor no se incluye en la secuencia.
- Se utiliza 22 y no 20 porque el límite superior de range() es exclusivo, es decir, no se toma en cuenta.
- El tercer parámetro (2) indica que el contador avanzará de dos en dos en cada iteración.
- Gracias a este incremento de 2 en 2, el programa solo genera números pares y evita tener que verificar si un número es par o impar.
- En cada iteración, el valor actual se almacena en la variable contador.
- La instrucción print(contador) muestra el número par actual en pantalla.
- El ciclo finaliza automáticamente cuando el siguiente valor supera el límite establecido por range().
"""