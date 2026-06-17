#EJERCICIO 3 -COLECCIONES

#Escriba un programa donde cree una lista con los siguientes personajes del Señor de los anillos.

#Nombre: Aragorn, Clase: Guerrero, Raza: Dúnadan del Norte
#Nombre: Gandalf, Clase: Mago, Raza: Istar
#Nombre: Legolas, Clase: Arquero, Raza: Elfo Sindar

print("\n--------- BIENVENIDO ----------")

#Crear lista vacía
personajes = []

#Crear el primer personaje como tipo diccionario
p = {"Nombre":"Aragorn", "Clase":"Guerrero", "Raza":"Dúnadan del Norte"}
#Añadir el personaje a la lista vacía
personajes.append(p)

#Crear el segundo personaje como tipo diccionario
p = {"Nombre":"Gandalf", "Clase":"Mago", "Raza":"Istar"}
#Añadir el personaje a la lista vacía
personajes.append(p)

#Crear el tercer personaje como tipo diccionario
p = {"Nombre":"Legolas", "Clase":"Arquero", "Raza":"Elfo Sindar"}
#Añadir el personaje a la lista vacía
personajes.append(p)

#Mostrar lista
print(personajes)

# - Hemos utilizado diccionarios y luego lo metimos en la lista
# - Como la variable "p" ya está en la lista, podemos volverlo a utilizar.