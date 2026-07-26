#BUCLE WHILE - #EJERCICIO 14

print("\n--------- BIENVENIDO ----------")
"""
Inicio de sesión
Crea un programa que solicite al usuario un nombre de usuario y una contraseña.

- Define un usuario y una contraseña correctos dentro del programa.
- Mientras las credenciales sean incorrectas, el programa debe seguir solicitándolas.
- Utiliza una variable booleana (por ejemplo, acceso = False) para controlar el bucle.
- Cuando el usuario ingrese las credenciales correctas, cambia la variable a True, muestra un mensaje de bienvenida y finaliza el programa.
"""

acceso = False;
usuario_correcto = "gluis";
contraseña_correcta = "GLuis123";

while acceso == False:

    usuario_ingresado = str(input("\n- Ingrese su usuario: "))
    contraseña_ingresada = str(input("- Ingrese su contraseña: "))

    if usuario_ingresado == usuario_correcto and contraseña_ingresada == contraseña_correcta:
        acceso = True;
        print("CREDENCIALES CORRECTAS, BIENVENIDO!")
    else: 
        #acceso = False; → Opcional (Innecesario)
        print("Credenciales incorrectas, intente de nuevo!")


# Explicación de Lógica
"""
- Se define una variable booleana llamada acceso y se inicializa en False, indicando que el usuario aún no ha iniciado sesión.
- El while se ejecuta mientras acceso sea False, es decir, mientras el usuario no haya ingresado las credenciales correctas.
- En cada iteración se solicita al usuario que ingrese su nombre de usuario y contraseña.
- Se comparan las credenciales ingresadas con las credenciales correctas definidas en el programa.
- Si ambas coinciden, la variable acceso cambia de False a True y se muestra un mensaje de bienvenida.
- Al cambiar acceso a True, la condición del while deja de cumplirse, por lo que el ciclo termina automáticamente.
- Si las credenciales son incorrectas, acceso permanece en False, se muestra un mensaje de error y el ciclo vuelve a solicitar las credenciales.
"""

"""
Piensa así:
= → Guardar.
== → Preguntar.
"""

"""
Lo importante es entender esto:
- El while no sabe que el usuario escribió bien la contraseña.
- El while solo mira el valor de acceso.
Por eso, esta línea fue la que resolvió todo: acceso = True
"""

"""
En realidad, el mecanismo es el mismo en los tres casos: el while evalúa una condición al inicio de cada iteración. Lo único que cambia es qué variable controla esa condición. Esa idea te acompañará en prácticamente todos los programas que escribas a partir de ahora.
"""