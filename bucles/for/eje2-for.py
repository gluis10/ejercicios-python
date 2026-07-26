#BUCLE FOR - #EJERCICIO 2

print("\n--------- BIENVENIDO ----------")
"""
Mostrar los números del 10 al 1.
Utiliza un bucle for para mostrar los números del 10 al 1 en orden descendente.
"""
print("\n-- Mostrar los números del 10 al 1 --")

for contador in range(10, 0, -1):
    print(contador)

# Explicación de Lógica
"""
- Se utiliza un bucle for para repetir una acción un número determinado de veces.
- La función range(10, 0, -1) genera una secuencia de números desde el 10 hasta el 1.
- El primer parámetro (10) indica el valor inicial de la secuencia.
- El segundo parámetro (0) indica el límite final, pero este valor no se incluye en la secuencia.
- El tercer parámetro (-1) indica que en cada iteración el contador disminuirá de uno en uno.
- En cada vuelta del ciclo, el valor actual se almacena en la variable contador.
- La instrucción print(contador) muestra el valor actual del contador en pantalla.
- El ciclo finaliza automáticamente cuando el contador intenta continuar más allá del límite establecido por range().
"""


