#PASS - #EJERCICIO 3

print("\n--------- BIENVENIDO ----------")
"""
El pass es una instrucción que no hace absolutamente nada. Se utiliza como un espacio reservado cuando Python necesita que exista una instrucción, pero todavía no queremos ejecutar ninguna acción.
"""

#Ejercicio
"""
Recorrer números y utilizar pass.
Utiliza un bucle for para recorrer los números del 1 al 6.
Cuando el número sea menor o igual a 3, utiliza pass para no realizar
ninguna acción específica y continuar con el bucle.

Cuando el número sea mayor a 3, muestra un mensaje indicando que
el valor es mayor a 3.
"""

print("\n-- Recorrer números y utilizar pass --")

for numero in range(1, 7):
    if numero <= 3:
        pass; #Aquí no pasa nada y el bucle sigue trabajando
    else:
        print("El siguiente valor es mayor a 3")
    print("El número es: ", numero)
print("Bucle terminado")

# Explicación de Lógica
"""
- El for recorre los números del 1 al 6.
- Si numero es menor o igual a 3, se ejecuta pass.
- pass no realiza ninguna acción y permite que el programa continúe.
- Si numero es mayor a 3, se muestra el mensaje correspondiente.
- Después, se imprime el valor actual de numero en cada iteración.
"""
  
"""
Un uso común de pass es cuando estás creando la estructura de un programa y todavía no has decidido qué código colocar:
    if edad >= 18:
        pass
Aquí le estás diciendo a Python: "Por ahora no hagas nada si se cumple esta condición."
En resumen: pass es como decirle a Python: "No hagas nada aquí, continúa."
"""


