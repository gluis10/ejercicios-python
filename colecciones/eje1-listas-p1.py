#Listas
"""
Una lista en Python es una estructura de datos que permite almacenar varios elementos en una sola variable, los cuales pueden ser de distintos tipos (números, cadenas, booleanos, etc.); se definen con corchetes [], mantienen el orden en que se agregan, permiten elementos repetidos y son mutables, es decir, se pueden modificar, añadir o eliminar elementos después de su creación.
"""

#Tomar en cuenta que las posiciones comienzan desde cero
#lunes=0, martes=1, miercoles=2, jueves=3, viernes=4

lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
print(lista) #Imprime toda la lista
print(lista[4]) #Imprime solo la que está en la posición 4 (viernes).
print(lista[0:3]) #Imprime de la posición 1 la 3 sin incluir la 3 (1=lunes a 2=miércoles).
print(lista[:4]) #Imprime de la 0 hasta 4 sin incluir la 4 (0=lunes a jueves=3).
print(lista[:]) #Imprime lunes hasta a viernes (todo)
print(lista[1:4]) #Imprime de la posición 1 hasta la 3 (martes a jueves).
print(lista[2:]) #Imprime de la posición 2 en adelante (miércoles a viernes).
print(lista[-1]) #Imprime el último elemento (Viernes).
print(lista[-3]) #Imprime el tercer elemento y viceversa (Miércoles).
print(lista[-5]) #Imprime el último elemento y viceversa (Lunes).
#print(lista[7]) Esto da error porque no existe el índice 7

#Una lista es una estructura de datos muy flexible
#Podemos imprimir de principio a fin y del último hasta el principio.
