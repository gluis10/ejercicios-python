#BUCLE FOR - BREAK Y ENUMERATE - #EJERCICIO 24

print("\n--------- BIENVENIDO ----------")
"""
Buscar la primera vocal.
Solicita al usuario una palabra y utiliza enumerate() para recorrer
cada letra junto con su posición.

Cuando encuentres la primera vocal, muestra:
- Qué vocal encontraste.
- En qué posición se encuentra.

Después, utiliza break para detener el recorrido.

Ejemplo:
Ingrese una palabra: Python

Resultado:
La primera vocal encontrada es "o".
Se encuentra en la posición 4.
"""

print("\n-- Buscar la primera vocal y su posisión --")
palabra = str(input("\nIngrese una palabra: "))

for posicion, caracter in enumerate(palabra):

    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u" or caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U":
        print("- La primera vocal encontrada es: ", caracter)
        print("- Se encuentra en la posición: ", posicion)
        break;

# Explicación de Lógica
"""
- Se solicita una palabra al usuario y se almacena en palabra.
- enumerate() recorre cada carácter y proporciona dos valores:
  la posición y el carácter.
- posicion almacena el índice y caracter almacena la letra actual.
- El if verifica si caracter corresponde a una vocal.
- Cuando encuentra la primera vocal, muestra la vocal y su posición.
- break detiene inmediatamente el for después de encontrarla.
"""

#----------- espaciado final ---------------
print("\n")