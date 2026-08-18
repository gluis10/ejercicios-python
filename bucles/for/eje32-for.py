#BUCLE FOR - #EJERCICIO 32

print("\n--------- BIENVENIDO ----------")
"""
Buscar una palabra dentro de una lista

Crea una lista de nombres.
Solicita al usuario el nombre que desea buscar.
Utiliza enumerate() para recorrer la lista y, si encuentras el nombre, muestra el nombre y su posición dentro de la lista.

Si no existe, muestra un mensaje indicándolo.
""" 

print("\n-- Buscar una palabra dentro de una lista --")

nombres = ["Genry", "Luis", "Harry", "Potter", "Cristiano", "Ronaldo", "Cr7", "Siuu"]
nombre_deseado = str(input("Ingrese el nombre que desea buscar: "))

for posicion, name in enumerate(nombres):
    if name == nombre_deseado:
        print("Posición: ", posicion, ":", name)
        break;
else:
    print("El nombre buscado no existe en la lista!")

# Explicación de Lógica
"""
- Se crea una lista de nombres y se solicita al usuario el nombre que desea buscar.
- enumerate() recorre la lista proporcionando dos valores:
  la posición y el nombre actual.
- El if compara cada nombre de la lista con el nombre ingresado por el usuario.
- Si encuentra coincidencia, muestra la posición y el nombre encontrado.
- break detiene el recorrido para no seguir buscando después de encontrarlo.
- Si el for termina sin ejecutar break, se ejecuta el else indicando que el nombre no existe en la lista.
"""

#----------- espaciado final ---------------
print("\n")