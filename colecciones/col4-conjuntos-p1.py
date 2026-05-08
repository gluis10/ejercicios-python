#Conjuntos
"""
Un conjunto en Python es una colección desordenada de elementos únicos, lo que significa que no permite duplicados y no mantiene un orden específico; se define con llaves {} o con la función set(), y es útil para operaciones matemáticas como unión, intersección o diferencia, así como para eliminar duplicados de una lista de forma sencilla.
"""

print("-----------Creación de conjunto vacío-------------------")
conjunto = set()
#Un conjunto primero lo creamos como una función (set) porque si solo lo creamos con corchetes, python va a entender que es un diccionario.
#Conjunto vacío
conjunto = {}
print(conjunto)

print("\t")
print("-----------Ejemplo de conjunto-------------------")
conjunto = {1,2,3, "Hola", 4.56}
print(conjunto)

#Tomar en cuenta que dentro de un conjunto no puede haber otro tipo de colección como una lista:
#conjunto = {1,2,3, "Hola", 4.56, [4,5,6]}: Esto me da error

print("\t")
print("-----------Suprime valores duplicados-------------------")
#En los conjuntos, no importa si pones valores duplicados, triplicados, siempre te va a imprimir solo una vez!
conjunto = {1,2,3, "Hola", 4.56, 3, 1, "Hola"}
print(conjunto)

print("\t")
print("-----------Agregar elementos al conjunto-------------------")
conjunto = {1,2,3, "Hola", 4.56}
conjunto.add(5)
print(conjunto)
#El 5 te lo agrega en una posición random cada que lo ejecutes, no sigue un orden en específico
conjunto.add("Adios")
print(conjunto)

print("\t")
print("-----------Eliminar un elemento de un conjunto-------------------")
conjunto = {1,2,3, "Hola", 4.56, "adios"}
conjunto.discard(3)
print(conjunto)
#Eliminamos el valor de 3 y "Hola"
conjunto.discard("Hola")
print(conjunto)

print("\t")
print("-----------Vaciar el conjunto-------------------")
conjunto = {1,2,3, "Hola", 4.56, "adios"}
conjunto.clear()
print(conjunto)

print("\t")
print("-----------Buscar un determinado elemento-------------------")
conjunto = {1,2,3, "Hola", 4.56, "adios"}
print(3 in conjunto) #Verdadero
print("adios" in conjunto) #Verdadero
print(5 in conjunto) #Falso

print("\t")
print("-----------Buscar un elemento en forma de negación-------------------")
conjunto = {1,2,3, "Hola", 4.56, "adios"}
print(3 not in conjunto)
print("Hi" not in conjunto)
print(4.56 not in conjunto)
#También se puede aplicar en litas y tuplas

