#BUCLE FOR - #EJERCICIO 26

print("\n--------- BIENVENIDO ----------")
"""
Buscar un número en una lista.
Crea una lista de números y solicita al usuario un número que quiera buscar.

Utiliza for para recorrer la lista. Si encuentras el número, muestra un mensaje indicando que fue encontrado y utiliza break para detener el recorrido.

Si termina el recorrido y no se encontró, muestra un mensaje indicando que el número no existe en la lista.
"""
print("\n-- Buscar un número en una lista --")

print("Mi lista: ")
numeros = [1,2,3,5,6,7,9,10,11,12,14,15]
print(numeros)

numero_elegido = int(input("\nIngrese el número que desea buscar: "))

for contador in numeros:
    if contador == numero_elegido:
        print(contador)
        print("El número fué encontrado en la lista!")
        break;
else:
    print("El número no existe en la lista")

# Explicación de Lógica
"""
- Se crea una lista de números y se muestra en pantalla.
- Se solicita al usuario el número que desea buscar.
- El for recorre cada elemento de la lista.
- El if compara el número de la lista con el número ingresado por el usuario.
- Si lo encuentra, muestra un mensaje y break detiene el recorrido.
- Si el for termina sin ejecutar break, se ejecuta el else indicando que el número no existe en la lista.
"""

"""
El for recorre internamente la lista mediante contador, pero no tienes obligación de imprimir cada valor.
Y aquí aprendiste algo bastante importante: for ... else en Python.
- Si encuentra el número → break detiene el for y el else no se ejecuta.
- Si recorre toda la lista y nunca encuentra el número → no hay break, entonces se ejecuta el else.
"""

#----------- espaciado final ---------------
print("\n")