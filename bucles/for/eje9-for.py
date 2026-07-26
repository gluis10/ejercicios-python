#BUCLE FOR - #EJERCICIO 9

print("\n--------- BIENVENIDO ----------")
"""
Calcular el factorial de un número.
Solicita un número entero positivo y calcula su factorial utilizando únicamente un bucle for.
Ejemplo: 5! = 120
Explicación: 5x4x3x2x1 = 120.
"""

print("\n-- Calcular el factorial de un número. --")
numero = int(input("Ingrese un número: "))

acumulador = 1;

for contador in range(numero, 0, -1):
    acumulador = acumulador * contador;
print("\n- El el factorial de", numero, "es", acumulador)


# Explicación de Lógica
"""
- Se solicita al usuario que ingrese un número entero y se almacena en la variable numero.
- Se crea la variable acumulador y se inicializa en 1.
- Se utiliza 1 como valor inicial porque estamos realizando multiplicaciones y 1 es el elemento neutro de la multiplicación.
- Se utiliza un bucle for para recorrer los números desde el número ingresado hasta llegar al 1.
- La función range(numero, 0, -1) genera una secuencia descendente.
- El primer parámetro indica el número inicial, que corresponde al número ingresado por el usuario.
- El segundo parámetro indica el límite final. Como range() no incluye el límite final, se utiliza 0 para poder incluir el número 1 en la secuencia.
- El tercer parámetro -1 indica que el contador debe disminuir de uno en uno.
- En cada iteración, el valor actual de contador se multiplica por el valor acumulado anteriormente.
- El resultado de cada multiplicación se guarda nuevamente en acumulador.
- De esta forma, el acumulador conserva el resultado de todas las multiplicaciones anteriores.
- Cuando el for termina, el acumulador contiene el resultado final del factorial.
- Finalmente, se muestra el número ingresado junto con el resultado de su factorial.
"""


"""
Un pequeño ejemplo de cómo funcionaría

Si el usuario ingresa 5:
acumulador = 1

contador = 5
acumulador = 1 × 5 = 5

contador = 4
acumulador = 5 × 4 = 20

contador = 3
acumulador = 20 × 3 = 60

contador = 2
acumulador = 60 × 2 = 120

contador = 1
acumulador = 120 × 1 = 120
"""

"""
En resumen el for controla el recorrido de los números y el acumulador se encarga de conservar el resultado de las multiplicaciones. Al finalizar el recorrido, el acumulador contiene el factorial del número ingresado.
"""