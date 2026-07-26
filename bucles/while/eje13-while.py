#BUCLE WHILE - #EJERCICIO 13

print("\n--------- BIENVENIDO ----------")
"""
Crea un menú que muestre las siguientes opciones:
- Saludar
- Mostrar fecha (puedes mostrar un mensaje fijo)
- Salir
El menú debe mostrarse repetidamente hasta que el usuario seleccione la opción "Salir".
"""
numero = 0;

while numero != 3:

    print("\n----- MENÚ DE OPCIONES ----")
    print("1. Saludar")
    print("2. Mostrar fecha")
    print("3. Salir")
    numero = int(input("\n- Ingrese un número de opción que desea: "))

    if numero == 1:
        print("- Hola! ¿Como estas?")
    elif numero == 2:
        print("- Hoy es jueves!")
    else:
        print("- Número inválido")
print("Hasta luego!")

# Explicación de Lógica
"""
- Se inicializa la variable numero en 0 para que el ciclo while pueda comenzar.
- El while se ejecuta mientras el usuario no seleccione la opción 3 (Salir).
- En cada iteración se muestra el menú con las opciones disponibles.
- Se solicita al usuario que ingrese el número de la opción que desea ejecutar.
- Si el usuario ingresa 1, se muestra un saludo.
- Si el usuario ingresa 2, se muestra un mensaje con la fecha (en este caso, un mensaje fijo).
- Si el usuario ingresa un número diferente de 1, 2 o 3, se muestra un mensaje indicando que la opción es inválida.
- Cuando el usuario selecciona la opción 3, la condición del while deja de cumplirse, el ciclo finaliza y se muestra el mensaje de despedida.
"""

"""
En este ejercicio, el while no repite un cálculo, sino que repite un menú de opciones. Es decir, cada vuelta del ciclo le permite al usuario elegir una acción distinta.
"""
