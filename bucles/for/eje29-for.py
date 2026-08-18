#BUCLE FOR - #EJERCICIO 29

print("\n--------- BIENVENIDO ----------")
"""
Encontrar el primer número mayor que 50
Crea una lista con diferentes números.

Recórrela utilizando for y encuentra el primer número mayor que 50.

Cuando lo encuentres:
    Muéstralo en pantalla.
    Utiliza break para detener el bucle.
""" 

print("\n-- Encontrar el primer número mayor que 50 --")

print("Mi lista: ")
numeros = [1,5,10,12,16,20,30,35,40,45,48,49,50,58,60,70,100]
print(numeros)

for contador in numeros:
    if contador > 50:
        print("El primer número mayor que 50 es: ", contador)
        break;
print("\nBucle terminado")

# Explicación de Lógica
"""
- Se crea una lista con diferentes números.
- El for recorre cada número de la lista.
- El if verifica si el número es mayor que 50.
- Cuando encuentra el primer número que cumple la condición, lo muestra en pantalla.
- break detiene inmediatamente el recorrido para no seguir revisando los demás números.
- Al finalizar el bucle, se muestra el mensaje "Bucle terminado".
"""

#----------- espaciado final ---------------
print("\n")