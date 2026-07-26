#BUCLE FOR - #EJERCICIO 4

print("\n--------- BIENVENIDO ----------")
"""
Mostrar únicamente los números impares del 1 al 19.
Crea un programa que imprima únicamente los números impares entre 1 y 19.
"""
print("\n-- Mostrar únicamente los números impares del 1 al 19 --")

for contador in range(1, 21, 2):
    print(contador)

# Explicación de Lógica
"""
- Se utiliza un bucle for para repetir una acción varias veces de forma automática.
- La función range(1, 21, 2) genera una secuencia de números desde el 1 hasta el 19.
- El primer parámetro (1) indica el valor inicial de la secuencia.
- El segundo parámetro (21) indica el límite final, pero este valor no se incluye en la secuencia.
- Se utiliza 21 y no 19 porque el límite superior de range() es exclusivo.
- El tercer parámetro (2) indica que el contador aumentará de dos en dos en cada iteración.
- Como la secuencia inicia en un número impar (1) y avanza de dos en dos, todos los valores generados serán números impares.
- De esta manera, no es necesario verificar si cada número es impar o par mediante condiciones adicionales.
- En cada iteración, el valor actual se almacena en la variable contador.
- La instrucción print(contador) muestra el número impar actual en pantalla.
- El ciclo finaliza automáticamente cuando el siguiente valor alcanza o supera el límite definido en range().
"""
