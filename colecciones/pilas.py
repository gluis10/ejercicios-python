#Pilas
"""
Una pila en Python es una estructura de datos que sigue el principio LIFO (Last In, First Out), donde el último elemento en entrar es el primero en salir; se puede implementar fácilmente usando una lista con los métodos append() para agregar elementos y pop() para quitarlos, siendo útil para manejar tareas como historial de navegación, deshacer acciones o evaluación de expresiones.
"""

print("-------Ejemplo de Pila-------")
pila = [1,2,3]
print(pila)

print("\n-------Agregar elementos al final de la Pila-------")
pila.append(4)
pila.append(5)
print(pila)

print("\n-------Eliminar el ultimo elemento de la pila-------")
pila.pop()
print(pila)

print("\n-------Eliminar el ultimo elemento retornando el valor eliminado-------")
n = pila.pop()
print(f"Eliminando el elemento {n}")
print(pila)

print("\n")






