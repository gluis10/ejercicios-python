#BUCLE WHILE - #EJERCICIO 9

print("\n--------- BIENVENIDO ----------")
"""
Sumar números hasta que el usuario escriba 0.
Solicita números al usuario y acumula su suma. El programa debe finalizar cuando el usuario ingrese el número 0 y luego mostrar el total acumulado.
"""
suma_acumulador = 0;
numero = int(input("\n- Digite un número random: "))

while numero != 0:
    suma_acumulador = suma_acumulador + numero;
    numero = int(input("- Vuelva a ingresar el número: "))
print("\n- La suma de los números ingresados es: ", suma_acumulador)

# Explicación de Lógica
"""
- Se inicializa una variable suma en 0 para almacenar la suma total de los números ingresados.
- Se solicita al usuario ingresar un número.
- El while se ejecuta mientras el número ingresado sea diferente de 0.
- En cada iteración, el número ingresado se suma a la variable suma.
- Luego se solicita un nuevo número para continuar o terminar el ciclo.
- Cuando el usuario ingresa 0, el ciclo termina porque es la condición de salida.
- Finalmente, se muestra la suma total de todos los números ingresados (sin contar el 0).
"""

