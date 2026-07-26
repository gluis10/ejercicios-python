#BUCLE FOR - #EJERCICIO 1

print("\n--------- BIENVENIDO ----------")
"""
Mostrar los números del 1 al 10
Utiliza un bucle for para imprimir en pantalla los números del 1 al 10, uno debajo del otro.
"""
print("\n-- Mostrar los números del 1 al 10 --")

for contador in range(1, 11):
    print(contador)

# Explicación de Lógica
"""
- Se utiliza un bucle for para repetir una acción varias veces de forma automática.
- La función range(1, 11) genera una secuencia de números desde el 1 hasta el 10.
- El número 11 no se incluye porque el límite superior de range() es exclusivo.
- En cada iteración del ciclo, el valor actual de la secuencia se almacena en la variable contador.
- La instrucción print(contador) imprime el valor actual de contador en pantalla.
- El proceso se repite hasta que se imprimen todos los números del 1 al 10.
- A diferencia del while, no es necesario incrementar manualmente la variable con contador += 1, ya que el for lo hace automáticamente.
"""