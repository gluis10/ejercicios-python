#Diccionarios

print("-------Dicionario de ejemplo-------")
equipo = {10:"Paulo Dybala", 11:"Douglas Costa", 7:"Cristiano Ronaldo", 17:"Mario Mandzukic"}
#Clave de tipo entero y valor de tipo cadena 
print(equipo)

print("\n----Ver a quien pertenece la dorsal No.10----")
print(equipo[10])
#Pasándole la clave
print(equipo[7])

print("\n----Buscar un jugador usando el get y validar si existe----")
#print(equipo[6]) #Esto da error porque la clave no existe
#Sin embargo, al usar el get podemos validar si existe la clave o no mostrando una alerta, sin que tire error en consola.
print(equipo.get(7, "No existe un jugador con ese dorsal"))

print("\n----Buscar un dorsal en específico----")
print(10 in equipo)
#Verificar si dorsal está en mi equipo

print("\n----Mostrar solo las claves (dorsales) de mi diccionario----")
print(equipo.keys())

print("\n----Mostrar solo los valores (nombres de mis judadores) de mi diccionario----")
print(equipo.values())

print("\n----Mostrar claves y valores----")
print(equipo)

print("\n----Mostrar claves y valores usando el el método items()----")
print(equipo.items())
#Esto es muy utilizado para recorrer diccionarios con el bucle for
#Si nos damos agrega el diccionario dentro de una lista pero también dentro de tuplas

print("\n----Mostrar cuántos elementos (jugadores) hay en mi equipo----")
print(len(equipo))

print("\n----Limpiar mi diccionario (vendí todos mis jugadores)----")
equipo.clear()
print(equipo)

print("\n")

