-------------- SENTENCIAS EN SQL ----------------
-- IN EN SQL --

#El IN se utiliza para filtrar los resultados de una consulta SQL basándose en una lista específica de valores.

/* El IN sirve para filtrar filas cuando una columna puede coincidir con varios valores posibles, y en lugar de usar muchos OR, los agrupás en una sola lista; por ejemplo, WHERE edad IN (20, 25, 30) devuelve solo los registros donde la edad sea exactamente 20, 25 o 30, haciendo la consulta más corta, clara y rápida de leer.
*/

#Mostrar toda la información de la tabla users donde la columna name sea igual a "Harry".
SELECT * FROM users WHERE name IN ('Harry');

----------- GENERADO POR IA -----------

#Mostrar toda la información de la tabla users donde la columna name sea igual a "Harry", "Sara" o "Maria".
SELECT * FROM users WHERE name IN ('Harry', 'Sara', 'Maria');
#Mostrar toda la información de la tabla users donde la columna edad sea igual a 15, 20 o 25.
SELECT * FROM users WHERE edad IN (15, 20, 25);
#Mostrar toda la información de la tabla users donde la columna edad sea igual a 15, 20 o 25 y el año sea 2021.
SELECT * FROM users WHERE edad IN (15, 20, 25) AND año = 2021;
#Mostrar toda la información de la tabla users donde la columna edad sea igual a 15, 20 o 25 o el año sea 2021.
SELECT * FROM users WHERE edad IN (15, 20, 25) OR año = 2021;
#Mostrar toda la información de la tabla users donde la columna edad no sea igual a 15, 20 o 25.
SELECT * FROM users WHERE edad NOT IN (15, 20, 25);
#Mostrar toda la información de la tabla users donde la columna edad no sea igual a 15, 20 o 25 y el año sea 2021.
SELECT * FROM users WHERE edad NOT IN (15, 20, 25) AND año = 2021;
#Mostrar toda la información de la tabla users donde la columna edad no sea igual a 15, 20 o 25 o el año sea 2021.
SELECT * FROM users WHERE edad NOT IN (15, 20, 25) OR año = 2021;

----------- FIN GENERADO POR IA -----------
