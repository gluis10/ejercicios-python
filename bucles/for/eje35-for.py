#BUCLE FOR - #EJERCICIO 35

print("\n--------- BIENVENIDO ----------")

"""
Sistema de búsqueda con límite de intentos.

Crea una lista de nombres y solicita al usuario que busque uno de ellos.
El usuario tendrá 3 intentos para encontrar un nombre.
Utiliza un for para controlar los intentos.

Si encuentra el nombre, muestra un mensaje de éxito y utiliza break.
Si no lo encuentra después de los 3 intentos, muestra un mensaje indicando que se agotaron los intentos.
"""

print("\n-- Sistema de búsqueda con límite de intentos --")

nombres = ["Genry", "Luis", "Harry", "Potter", "Cristiano", "Ronaldo", "Cr7", "Siuu"]
print(nombres)

for intentos in range(3):
    nombre_deseado = str(input("\nIngrese el nombre que desea buscar: "))

    encontrado = False

    for posicion, valores in enumerate(nombres):

        if nombre_deseado == valores:
            encontrado = True
            break
    
    if encontrado:
        print("- Usuario", nombre_deseado, "encontrado y está en la posición", posicion)
        break
else:
    print("Intentos agotados!")

# Explicación de Lógica
"""
- Se crea una lista de nombres y se utiliza un for externo para controlar los 3 intentos disponibles.
- En cada intento se solicita al usuario el nombre que desea buscar.
- encontrado = False indica inicialmente que todavía no se ha encontrado el nombre.
- El segundo for recorre la lista utilizando enumerate(), obteniendo la posición y el nombre actual.
- El if compara el nombre ingresado con cada nombre de la lista.
- Si encuentra una coincidencia, encontrado = True indica que el nombre fue encontrado.
- El primer break detiene el segundo for porque ya no es necesario seguir buscando.
- Después, if encontrado verifica si el nombre fue encontrado.
- Si fue encontrado, se muestra el nombre y su posición.
- El segundo break detiene el for externo porque ya no es necesario utilizar los intentos restantes.
- Si los 3 intentos terminan sin encontrar el nombre, el else del for externo muestra "Intentos agotados".
"""

#La idea principal
"""
Puedes verlo como dos niveles de trabajo:

- Primer for → controla los 3 intentos.
- Segundo for → busca el nombre dentro de la lista.
- if → comprueba si encontró el nombre.
- encontrado → recuerda si se encontró o no.
- Primer break → detiene la búsqueda dentro de la lista.
- Segundo break → detiene los intentos porque ya tuvo éxito.

Y algo muy importante: encontrado = False y encontrado = True funcionan como una bandera: empiezas suponiendo "no encontrado" y la cambias a "encontrado" cuando aparece una coincidencia.
"""