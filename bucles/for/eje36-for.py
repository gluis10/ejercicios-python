#BUCLE FOR - #EJERCICIO 36

print("\n--------- BIENVENIDO ----------")

"""
Sistema de acceso con intentos limitados

Crea un programa que solicite al usuario una contraseña.
El usuario tendrá un máximo de 3 intentos para ingresar la contraseña correcta.

- Define previamente una contraseña correcta.
- Utiliza un for para controlar los 3 intentos.
- Si la contraseña es correcta, muestra un mensaje indicando que el acceso fue concedido y utiliza break.
- Si la contraseña es incorrecta, muestra cuántos intentos le quedan.
- Si después de los 3 intentos nunca ingresó la contraseña correcta, muestra un mensaje indicando que el acceso fue bloqueado.
 
Objetivo: practicar for, if, break y contador de intentos.
"""

print("\n-- Sistema de acceso con intentos limitados --")

password_correcta = "LA123!"
intentos_disponibles = 2

for intentos in range(3):
    password = str(input("\nIngrese su contraseña: "))

    if password == password_correcta:
        print("Acceso concedido!")
        break
    else:
        print("Le quedan", intentos_disponibles - intentos, "intentos")
else:
    print("Acceso bloqueado!")


# Explicación de Lógica
"""
- Se define la contraseña correcta y se establece intentos_disponibles en 2,
  porque después del primer intento todavía quedan 2 oportunidades.

- El for con range(3) permite realizar como máximo 3 intentos.
- La variable intentos toma los valores 0, 1 y 2 en cada repetición.
- El if compara la contraseña ingresada con la contraseña correcta.
- Si coincide, se muestra "Acceso concedido" y break detiene el for.
- Si la contraseña es incorrecta, se calcula cuántos intentos quedan:
  intentos_disponibles - intentos.
- Si los 3 intentos terminan sin utilizar break, el else del for muestra
  "Acceso bloqueado".
"""

#¿Cómo se relacionan intentos_disponibles e intentos?
"""
intentos_disponibles = 2

intentos viene del for: for intentos in range(3):
Y va tomando:
Primer intento  → intentos = 0
Segundo intento → intentos = 1
Tercer intento  → intentos = 2

Entonces haces: intentos_disponibles - intentos

Y ocurre:
Primer intento:  2 - 0 = 2 intentos restantes
Segundo intento: 2 - 1 = 1 intento restante
Tercer intento:  2 - 2 = 0 intentos restantes
"""

#¿Por qué intentos_disponibles empieza en 2 y no en 3?
"""
Porque intentos empieza en 0, y yo quiero mostrar cuántas oportunidades quedan después de fallar el intento actual.
"""