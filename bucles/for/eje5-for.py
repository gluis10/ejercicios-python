#BUCLE FOR - #EJERCICIO 5

print("\n--------- BIENVENIDO ----------")
"""
Calcular la suma de los números del 1 al 100.
Utiliza un bucle for para sumar todos los números desde el 1 hasta el 100 y mostrar el resultado final.
"""
print("\n-- Calcular la suma de los números del 1 al 100 --")
suma = 0;
 
for contador in range(1, 101):
    suma = suma + contador
print("La suma total de 1 hasta 100 es: ", suma)

# Explicación de Lógica
"""
- Se crea la variable suma y se inicializa en 0 para almacenar el resultado acumulado de las sumas.
- Se utiliza un bucle for para recorrer los números del 1 al 100.
- La función range(1, 101) genera una secuencia de números desde el 1 hasta el 100.
- Se utiliza 101 como límite superior porque el segundo parámetro de range() no se incluye en la secuencia.
- En cada iteración, el número actual se almacena en la variable contador.
- La instrucción suma = suma + contador agrega el valor actual de contador al total acumulado.
- La variable suma conserva el resultado de las iteraciones anteriores y se va actualizando en cada vuelta del ciclo.
- El proceso continúa hasta que se han sumado todos los números del 1 al 100.
- Una vez finalizado el bucle, se imprime el resultado final almacenado en la variable suma.
"""

"""
Pista:
Todo lo que esté dentro del for se ejecuta en cada iteración.
Todo lo que esté fuera del for se ejecuta una sola vez, cuando el ciclo ya terminó.
"""
