#BUCLE FOR - BREAK - #EJERCICIO 22

print("\n--------- BIENVENIDO ----------")
"""
Buscar un número específico.
Solicita al usuario un número y utiliza un bucle for para recorrer
los números del 1 al 100.

Cuando encuentres el número ingresado por el usuario, muestra un mensaje
indicando que fue encontrado y utiliza break para detener el bucle.

Si el número está fuera del rango del 1 al 100, muestra un mensaje indicando
que no se puede encontrar dentro del rango.
"""
print("\n-- Buscar un número específico usando break --")
numero = int(input("\n- Ingrese un número: "))

for contador in range(1, 101):
    print(contador)
    if contador == numero:
        print("El número ingresado por el usuario fué encontrado!")
        break;
print("Programa finalizado")

# Explicación de Lógica
"""
- Se solicita un número al usuario.
- El for recorre los números del 1 al 100.
- En cada vuelta se imprime el número actual.
- El if comprueba si contador coincide con el número ingresado.
- Si coincide, se muestra el mensaje y break detiene el bucle.
- Al finalizar el bucle, se imprime "Programa finalizado".
"""