#BUCLE WHILE - #EJERCICIO 11

print("\n--------- BIENVENIDO ----------")
"""
Define un número secreto dentro del programa. 
Pide al usuario que lo adivine y sigue solicitando intentos hasta que acierte. 
Al final, muestra cuántos intentos realizó.
"""

intentos = 1;
secret_num = 12345;
numero_user = int(input("\n- Ingrese la contraseña correcta: "))

while numero_user != secret_num:
    intentos = intentos + 1;
    print("Numero incorrecta!")
    numero_user = int(input("- Vuelva a ingresarlo!: "))
print("-Número ingresada correctamente!")
print("-Número de intentos realizados:", intentos)

# Explicación de Lógica
"""
- Se define un número secreto que el usuario debe adivinar.
- Se inicializa un contador de intentos en 1, ya que el primer número ingresado cuenta como el primer intento.
- Se solicita al usuario que ingrese un número.
- El while se ejecuta mientras el número ingresado sea diferente al número secreto.
- Si el usuario se equivoca, el contador de intentos aumenta en 1, se muestra un mensaje indicando que el número es incorrecto y se solicita un nuevo intento.
- Cuando el usuario ingresa el número secreto, la condición del while deja de cumplirse y el ciclo termina.
- Finalmente, se muestra un mensaje indicando que el número fue adivinado correctamente y la cantidad total de intentos realizados.
"""
