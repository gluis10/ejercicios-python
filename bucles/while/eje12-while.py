#BUCLE WHILE - #EJERCICIO 12

print("\n--------- BIENVENIDO ----------")
"""
Calcular el factorial de un número.
Solicita un número entero positivo y calcula su factorial utilizando únicamente un bucle while.
"""

#¿Qué es el factorial de un número?
"""
El factorial de un número es el resultado de multiplicar ese número por todos los números enteros positivos menores que él, hasta llegar a 1.
Se representa con el símbolo !.
Por ejemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120
"""

numero = int(input("\n- Ingrese un número positivo: "))

while numero < 0:
    print("El número ingresado es inválido!")
    numero = int(input("- Vuelva a ingresar el número: "))

numero_original = numero;
acumulador = 1;

while numero > 0:
    acumulador = acumulador * numero;
    numero = numero - 1;
print("-El factorial de", numero_original, "es: ", acumulador)

# Explicación de Lógica
"""
- Se solicita al usuario un número entero positivo.
- Si el usuario ingresa un número negativo, se muestra un mensaje y se vuelve a solicitar hasta que ingrese un valor válido.
- Se guarda una copia del número original para mostrarlo al finalizar, ya que durante el proceso el valor del número se modifica.
- Se inicializa un acumulador en 1, ya que el factorial se obtiene mediante multiplicaciones sucesivas.
- El while se ejecuta mientras el número sea mayor que 0.
- En cada iteración, el acumulador se multiplica por el valor actual del número y luego el número disminuye en 1.
- Cuando el número llega a 0, el ciclo termina.
- Finalmente, se muestra el número original junto con el resultado de su factorial.
"""

#Tomemos en cuenta que factorial de: 0! = 1

"""
¿Qué hace programa cuando el usuario ingresa 0?:

- La validación lo acepta (porque no es negativo).
- El while numero > 0 no se ejecuta.
- El acumulador sigue valiendo 1.
Entonces el resultado será:
- El factorial de 0 es: 1
"""