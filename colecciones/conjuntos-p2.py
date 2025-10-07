#Tuplas
#Si quiero crear un conjunto vacío siempre se setea primero. Si creo un conjunto ya con valores, no hay necesidad de setearlo (a = set()) .

a = {1,2,3}
b = {3,4,5, 7}
c = {3,1,2}

print("--------- Ver la igualdad de dos conjuntos -----------")
print(a == b)
#Están en orden diferente pero los elementos son iguales
print(a == c)

print("--------- Ver cuántos elementos tiene un conjunto -----------")
print(len(b))

print("--------- UNIÓN DE CONJUNTOS -----------")
a = {1,2,3}
b = {3,1,2}
c = {1, 3, 4, 5, 7}

print("--------- unión de dos conjuntos -----------")
#Se utiliza el símbolo "|" para unir dos conjuntos
principal = a | b 
print(principal)
#Eje2
principal = a | c 
print(principal)
#Recordemos que en los conjuntos son valores unitarios (no duplicados)

print("--------- INTERSECCIÓN DE CONJUNTOS -----------")
#La intersección son aquellos elementos que están en ambos conjuntos
a = {1,2,3, 5}
b = {3,1,2}
c = {1, 3, 4, 5, 7}

interseccion = a & c
print(interseccion)

print("--------- DIFERENCIA CONJUNTOS -----------")
#La diferencia son los elementos de a y que no están en c
a = {1,2,3, 5}
b = {3,1,2}
c = {1, 3, 4, 5, 7}

diferencia = a - c
print(diferencia)


print("--------- DIFERENCIA CIMÉTRICA -----------")
#La diferencia simétrica son los elementos que están en a y en b pero que no están en ambos
a = {1,2,3, 5}
b = {3,1,2}
c = {1, 3, 4, 5, 7}

diferenciasim = a ^ c
print(diferenciasim)


print("--------- SUBCONJUNTOS -----------")
#Ejem, verificar si el conjunto B es un subconjunto de conjunto A (Si todos los elementos de B están en A)
a = {1,2,3,5,4}
b = {3,1,2}
c = {1, 3, 4, 5, 7}

print(b.issubset(a))
#Eje2: A no es un subconjunto de C
print(a.issubset(c))

print("--------- SUPERCONJUNTOS -----------")
#Ejem, verificar si A es el superconjunto de B, (verificar si en A están todos los elementos de conjunto B)
a = {1,2,3,5,4}
b = {3,1,2}
c = {1, 3, 4, 5, 7}

print(a.issuperset(b))

print("--------- CONJUNTOS DISCONEXOS -----------")
#Ejem, verificar si ambos conjuntos no comparten ningún elemento en común
a = {1,2,3,5,4}
b = {2,6,8}
c = {1, 3, 4, 5, 7}

print(a.isdisjoint(b)) #Falses
#Eje2
print(c.isdisjoint(b)) #True

print("--------- CONJUNTOS INMUTABLES -----------")
#Un conjunto inmutable no se puede modificar (add, edit, delete)
a = frozenset({1,2,3,5,4})
a.add(6)
print(a) #Error
