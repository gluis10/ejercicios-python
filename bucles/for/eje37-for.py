#BUCLE FOR - #EJERCICIO 37

print("\n--------- BIENVENIDO ----------")

"""
Juego: encuentra el número secreto

Crea un pequeño juego donde el programa tenga un número secreto y el usuario tenga 5 oportunidades para adivinarlo.

En cada intento:

- Solicita un número al usuario.
- Si el número es igual al secreto, muestra un mensaje indicando que ganó y utiliza break.
- Si el número es menor que el secreto, indica: "El número secreto es mayor".
- Si el número es mayor que el secreto, indica: "El número secreto es menor".
- Si utiliza los 5 intentos sin acertar, muestra cuál era el número secreto.

Objetivo: practicar condiciones dentro de un for y utilizar break cuando se cumple el objetivo.
"""

print("\n-- Juego: encuentra el número secreto --")

numero_secreto = 12

for intentos in range(5):
    numero_ingresado = int(input("\nIngrese el número secreto: "))

    if numero_ingresado == numero_secreto:
        print("¡Acertó, ha ganado el juego!")
        break
    elif numero_ingresado < numero_secreto:
        print("El número secreto es mayor al número ingresado")
    elif numero_ingresado > numero_secreto:
        print("El número secreto es menor al número ingresado")
else:
    print("Intentos agotado!!")
    print("El número secreto era:", numero_secreto)

# Explicación de Lógica
"""
- Se define el número secreto que el usuario debe adivinar.
- El for controla los 5 intentos disponibles.
- En cada repetición se solicita al usuario un número.
- El if verifica si el número ingresado es igual al número secreto.
- Si coincide, se muestra un mensaje de victoria y break detiene el juego.
- El primer elif verifica si el número ingresado es menor que el secreto.
- Si es menor, se indica que el número secreto es mayor.
- El segundo elif verifica si el número ingresado es mayor que el secreto.
- Si es mayor, se indica que el número secreto es menor.
- Si los 5 intentos terminan sin ejecutar break, el else del for muestra el número secreto.
"""


