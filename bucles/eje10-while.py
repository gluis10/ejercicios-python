#BUCLE WHILE - #EJERCICIO 10

print("\n--------- BIENVENIDO ----------")
"""
Contar cuántos números ingresa el usuario y calcular el promedio.
Solicita números al usuario hasta que escriba 0. El programa debe contar cuántos números válidos ingresó y calcular el promedio de esos números.
Usando while.
"""
tnumeros_ingresados = 0;
sumat_acumulado = 0;
numero = int(input("\n- Digite un número random: "))

while numero != 0:
    tnumeros_ingresados = tnumeros_ingresados + 1;
    sumat_acumulado = sumat_acumulado + numero;
    numero = int(input("- Vuelva a ingresar el número: "))

if tnumeros_ingresados > 0:
    promedio = sumat_acumulado / tnumeros_ingresados;

    print("\n- El total de números ingresados es: ", tnumeros_ingresados);
    print("- La suma de los números ingresados es: ", sumat_acumulado);
    print("- El promedio total es: ", promedio);
else:
    print("No se puede calcular el promedio porque no se ingresaron números válidos.")


# Explicación de Lógica
"""
- Se inicializan dos variables: una para contar la cantidad de números ingresados y otra para acumular la suma de esos números.
- Se solicita al usuario que ingrese un número.
- El while se ejecuta mientras el número ingresado sea diferente de 0.
- En cada iteración, el contador aumenta en 1 para registrar un nuevo número válido.
- El número ingresado se agrega al acumulador para obtener la suma total.
- Luego se solicita un nuevo número al usuario.
- Cuando el usuario ingresa 0, el ciclo termina.
- Se valida que se haya ingresado al menos un número válido para evitar una división entre 0.
- Si hay números ingresados, se calcula el promedio dividiendo la suma acumulada entre la cantidad de números ingresados y se muestran los resultados.
- Si el usuario ingresa 0 desde el inicio, se muestra un mensaje indicando que no es posible calcular el promedio.
"""

"""
¿Por qué NO if dentro del while?
Si pones el if dentro del while, estarías evaluando esto muchas veces:
- Promedio incompleto
- Datos cambiando constantemente
- No tiene sentido calcular algo final aún.
"""
#No puedes imprimir una variable que no existe.
#Si una variable solo se crea en un camino del programa, no la puedes usar fuera de ese camino.
