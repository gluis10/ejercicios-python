#Conjuntos parte 2
#Si quiero crear un conjunto vacío siempre se setea primero. Si creo un conjunto ya con valores, no hay necesidad de setearlo (a = set()) .

a = {1,2,3}
b = {3,4,5, 7}
c = {3,1,2}

print("\t")
print("--------- Ver la igualdad de dos conjuntos -----------")
#Verificar si el conjunto "a" es igual al conjunto "b" (False)
print(a == b)
#Están en orden diferente pero los elementos son iguales (true)
print(a == c)

print("\t")
print("--------- Ver cuántos elementos tiene un conjunto -----------")
print(len(b)) #4 elementos

print("\t")
print("--------- UNIÓN DE CONJUNTOS -----------")
a = {1,2,3}
b = {3,1,2}
c = {1, 3, 4, 5, 7}

print("\t")
print("--------- Unión de dos conjuntos -----------")
#Se utiliza el símbolo "|" para unir dos conjuntos
principal = a | b #Imprime {1,2,3} porque no se repite elementos
print(principal)
#Eje2
principal = a | c 
print(principal)
#Recordemos que en los conjuntos son valores unitarios (no duplicados)

print("\t")
print("--------- INTERSECCIÓN DE CONJUNTOS -----------")
#La intersección son aquellos elementos que están en ambos conjuntos
a = {1,2,3, 5}
b = {3,1,2}
c = {1, 3, 4, 5, 7}

interseccion = a & c
print(interseccion) #Se imprime {1,2,5} que son los que están en ambos

print("\t")
print("--------- DIFERENCIA CONJUNTOS -----------")
#La diferencia son los elementos de "a" y que no están en "c"
a = {1,2,3, 5}
b = {3,1,2}
c = {1, 3, 4, 5, 7}

diferencia = a - c
print(diferencia)
#Se imprime 2 porque es el único elemento que está en "a" y no está en "c".

print("\t")
print("--------- DIFERENCIA CIMÉTRICA -----------")
#La diferencia simétrica son los elementos que están en "a" y en "b" pero que no están en ambos.
a = {1,2,3, 5}
b = {3,1,2}
c = {1, 3, 4, 5, 7}

diferenciasim = a ^ c
#Se imprime 2,4,7 porque son los elementos que no se repiten en ambos.

print("\t")
print("--------- SUBCONJUNTOS -----------")
#Ejem, verificar si el conjunto B es un subconjunto de conjunto A (Si todos los elementos de B están en A)
a = {1,2,3,5,4}
b = {3,1,2}
c = {1, 3, 4, 5, 7}

print(b.issubset(a)) 
#Verdadero porque 3,1,2 también están "A".
#Eje2: A no es un subconjunto de C
print(a.issubset(c))

print("\t")
print("--------- SUPERCONJUNTOS -----------")
#Ejem, verificar si A es el superconjunto de B, (verificar si en A están todos los elementos de conjunto B)
a = {1,2,3,5,4}
b = {3,1,2}
c = {1, 3, 4, 5, 7}

print(a.issuperset(b))

print("\t")
print("--------- CONJUNTOS DISCONEXOS -----------")
#Ejem, verificar si ambos conjuntos no comparten ningún elemento en común
a = {1,2,3,5,4}
b = {2,6,8}
c = {1, 3, 4, 5, 7}

print(a.isdisjoint(b)) #Falso, 2 se repite en ambos.
#Eje2
print(c.isdisjoint(b)) #True

print("\t")
print("--------- CONJUNTOS INMUTABLES -----------")
#Un conjunto inmutable no se puede modificar (add, edit, delete)
a = frozenset({1,2,3,5,4})
a.add(6)
print(a) #Esto da Error porque no se puede modificar los conjuntos inmutables.

