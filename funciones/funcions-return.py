#FUNCIONES - RETURN

"""
return sirve para que una función devuelva un resultado.
"""
print("\n--- Ejemplo1 de return - suma ---")

def sumar1(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

total = sumar1(5, 3)
print(total)

# Explicación de Lógica
"""
- Se define la función sumar1() con dos parámetros.
- La función suma numero1 y numero2 y guarda el resultado en resultado.
- return resultado devuelve ese valor hacia donde se llamó la función.
- total = sumar1(5, 3) recibe el valor devuelto por la función y lo guarda en total.
- print(total) muestra el valor almacenado en total.
"""

#La diferencia importante entre "print()" y "return"
"""
- print() → muestra algo en pantalla.
- return → devuelve un valor para que podamos guardarlo en una variable, utilizarlo en otra operación, utilizarlos fuera de la función o seguir trabajando con él.
"""

print("\n--- ¿Qué pasa si quito return? ---")
def sumar2(numero1, numero2):
    resultado = numero1 + numero2

total = sumar2(5, 3)
print(total)

#El resultado será: None ¿Por qué?
"""
Porque la función sí realiza la suma, pero no devuelve el resultado.
"""


print("\n--- Ejemplo2 de return - suma ---")

def suma3(x, y, z):
    resultado = x + y + z
    return resultado

resultado_suma = suma3(5, 6, 8)
print(resultado_suma)

# Explicación de Lógica
"""
- Se define la función suma3() con tres parámetros: x, y y z.
- La función suma los tres valores y guarda el resultado en la variable resultado.
- return resultado devuelve ese valor fuera de la función.
- resultado_suma = suma3(5, 6, 8) recibe el valor que devuelve la función y lo guarda en resultado_suma.
- print(resultado_suma) muestra el valor almacenado.
"""

#La conexión entre las dos variables
"""
En este caso:
    resultado = x + y + z
    return resultado
La función calcula: 5 + 6 + 8 = 19

Luego: 
    resultado_suma = suma3(5, 6, 8)
es como decir: 
    resultado_suma = 19
"""

# ---- Return con lista ------¨
print("----- Return con lista -----")
lista = [4, 7, 3, 2, 4]

def suma4(lista):
    resultado1 = sum(lista)
    return resultado1

resultado_suma1 = suma4(lista)
print(resultado_suma1)

# Explicación de Lógica
"""
- Se crea una lista con varios números.
- La función suma4() recibe la lista como parámetro.
- sum(lista) calcula automáticamente la suma de todos los elementos.
- return devuelve el resultado de la suma.
- resultado_suma1 recibe el valor que devuelve la función.
- print() muestra el resultado.
"""

#Ventaja de utilizar una lista
"""
Usar una lista permite agregar o quitar números sin tener que modificar la función ni agregar más parámetros.

Por ejemplo: 
    lista = [4, 7, 3, 2, 4]
Podemos agregar más:
    lista = [4, 7, 3, 2, 4, 10, 15, 20]
Y la función sigue funcionando exactamente igual:
    resultado_suma1 = suma4(lista)

En resumen: una lista hace que la función sea más flexible, porque puede trabajar con cualquier cantidad de números sin tener que definir un parámetro para cada uno.
"""

#Resumen rápido
"""
Concepto  ¿Para qué sirve?

def	= Crear una función
Parámetro = Recibir datos
Argumento = Dato que enviamos
return = Devolver un resultado
print()	= Mostrar algo en pantalla
"""

#Una forma sencilla de recordarlo:
"""
    - Parámetro → entra información a la función.
    - return → sale información de la función.
"""

