#Colas
"""
Una cola en Python es una estructura de datos que sigue el principio FIFO (First In, First Out), donde el primer elemento en entrar es el primero en salir; se puede implementar con listas usando append() para agregar y pop(0) para quitar, aunque es más eficiente usar deque del módulo collections, siendo útil para manejar procesos en orden, como tareas en espera o gestión de turnos.
"""
print("\n-------Ejemplo de Cola-------")

cola = ["María", "Genry", "José", "Mario"]
print(cola)

print("\n-----Agregar elementos al final de la cola----")
cola.append("Karla")
cola.append("Flor")
print(cola)

print("\n-----Sacando elementos al principio de la cola----")
n = cola.pop(0)
print(f"Atendiendo a {n}")
#Le indicamos que vamos a sacar el primer elemento poniendo el índice del elemento
print(cola)


print("\n")