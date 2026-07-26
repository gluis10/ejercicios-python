#BUCLE WHILE - #EJERCICIO 15

print("\n--------- BIENVENIDO A MI CALCULADORA BÁSICA ----------")
"""
MENÚ DE CALCULADORA
Desarrolla una calculadora con el siguiente menú:
1. Sumar dos números.
2. Restar dos números.
3. Multiplicar dos números.
4. Dividir dos números.
5. Salir.

Requisitos:
- El menú debe mostrarse continuamente utilizando un while.
- Utiliza una variable booleana (por ejemplo, salir = False) para controlar cuándo termina el programa.
- Cuando el usuario seleccione la opción 5, cambia la variable a True para finalizar el bucle.
- Si el usuario ingresa una opción inválida, muestra un mensaje y vuelve a presentar el menú.
- En la opción de división, evita que el usuario divida entre cero.
"""

salir = False;

while salir == False:
    print("\n----- MENÚ DE OPCIONES ----")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Hasta luego!")
    numero = int(input("\n- Ingrese el número de opción que desea: "))

    if numero == 1:
        print("1. Sumar dos números")
        num1 = int(input("\n- Ingrese el primer número: "))
        num2 = int(input("- Ingrese el segundo número: "))
        resultado = num1 + num2
        print("EL RESULTADO DE LA SUMA ES: ", resultado)
    elif numero == 2: 
        print("2. Restar dos números")
        num1 = int(input("\n- Ingrese el primer número: "))
        num2 = int(input("- Ingrese el segundo número: "))
        resultado = num1 - num2
        print("EL RESULTADO DE LA RESTA ES: ", resultado)
    elif numero == 3:
        print("3. Multiplicar dos números")
        num1 = int(input("\n- Ingrese el primer número: "))
        num2 = int(input("- Ingrese el segundo número: "))
        resultado = num1 * num2
        print("EL RESULTADO DE LA MULTIPLICACIÓN ES: ", resultado)
    elif numero == 4:
        print("4. Dividir dos números")
        num1 = int(input("\n- Ingrese el primer número: "))
        num2 = int(input("- Ingrese el segundo número: "))

        if num2 != 0:
            resultado = num1 / num2
            print("EL RESULTADO DE LA DIVISIÓN ES: ", resultado)
        else:
            print("- No se puede dividir entre cero.")
    elif numero == 5:
        salir = True
        print("Saliendo del programa!")
    else:
        print("¡Opción inválida! Intente de nuevo.")


# Explicación de Lógica Resumida
"""
1. Crear una variable booleana salir = False.
2. Iniciar un while que se repita mientras salir sea False.
3. Mostrar el menú.
4. Solicitar al usuario una opción.
5. Utilizar if/elif/else para determinar qué operación realizar.
6. Realizar la operación seleccionada.
7. En la división, validar que el divisor no sea 0.
8. Si la opción es inválida, mostrar un mensaje y continuar con el menú.
9. Si el usuario selecciona 5, cambiar salir = True.
10. El while vuelve a evaluar la condición.
11. Como salir ahora es True, la condición es falsa y el ciclo termina.
"""

"""
En este caso:
El menú continúa mientras salir sea False y termina cuando salir cambia a True.
"""

# Explicación de Lógica a Profundidad
"""
- Se crea la variable booleana salir y se inicializa con el valor False.
- Esta variable se utilizará para controlar cuándo debe finalizar el programa.

- Se utiliza un bucle while con la condición salir == False.
- Mientras la variable salir tenga el valor False, el menú continuará mostrándose y el programa seguirá funcionando.
- Esto permite que el usuario pueda realizar varias operaciones sin que el programa termine después de una sola operación.

- Dentro del while se muestran las cinco opciones disponibles:
  1. Sumar.
  2. Restar.
  3. Multiplicar.
  4. Dividir.
  5. Salir.

- Se solicita al usuario que ingrese un número para seleccionar una opción.
- La estructura if, elif y else se utiliza para determinar qué acción debe realizar el programa según la opción seleccionada.

- Si el usuario selecciona la opción 1:
  - Se solicitan dos números.
  - Se suman ambos números.
  - El resultado se muestra en pantalla.
  - Al terminar la operación, el while vuelve a comenzar y muestra nuevamente el menú.

- Si el usuario selecciona la opción 2:
  - Se solicitan dos números.
  - Se realiza la resta.
  - Se muestra el resultado.
  - El menú vuelve a aparecer.

- Si el usuario selecciona la opción 3:
  - Se solicitan dos números.
  - Se realiza la multiplicación.
  - Se muestra el resultado.
  - El menú vuelve a aparecer.

- Si el usuario selecciona la opción 4:
  - Se solicitan dos números.
  - Antes de realizar la división, se verifica que el segundo número sea diferente de 0.
  - Si num2 es diferente de 0, se realiza la división.
  - Si num2 es igual a 0, se muestra un mensaje indicando que no se puede dividir entre cero.
  - De esta manera se evita realizar una operación matemática inválida.

- Si el usuario selecciona la opción 5:
  - La variable salir cambia de False a True.
  - Se muestra un mensaje indicando que el programa está finalizando.

- Después de cambiar salir a True, el while vuelve a evaluar su condición.
- Como la condición salir == False ya no se cumple, el ciclo termina y el programa finaliza.

- Si el usuario ingresa una opción diferente de 1, 2, 3, 4 o 5:
  - Se ejecuta el bloque else.
  - Se muestra un mensaje indicando que la opción es inválida.
  - Como salir sigue siendo False, el while continúa y el menú vuelve a mostrarse.
"""


