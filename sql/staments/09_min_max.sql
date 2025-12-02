-------------- SENTENCIAS EN SQL ----------------
-- MIN Y MAX EN SQL --

#La función MIN se utiliza para obtener el valor mínimo de una columna en una consulta SQL.
#La función MAX se utiliza para obtener el valor máximo de una columna en una consulta SQL.

/* Por ejemplo: tengo a mis usuarios en mi aplicación y quiero saber cuál es el usuario con mayor edad porque quiero darle un premio.
*/
SELECT MAX(edad) FROM users;

/* Otro ejemplo: tengo una tienda en línea y quiero saber cuál es el producto más barato que tengo en mi inventario para destacarlo en la página principal.
*/
SELECT MIN(precio) FROM productos;

/* Otro ejemplo: tengo una base de datos de estudiantes y quiero saber cuál es la calificación más alta obtenida en un examen para felicitar al estudiante que la obtuvo.
*/
SELECT MAX(calificación) FROM estudiantes;


----------- GENERADO POR IA -----------

#Mostrar el valor mínimo de la columna edad en la tabla users.
SELECT MIN(edad) AS edad_minima FROM users;

#Mostrar el valor máximo de la columna edad en la tabla users.
SELECT MAX(edad) AS edad_maxima FROM users;

#Mostrar el valor mínimo y máximo de la columna edad en la tabla users.
SELECT MIN(edad) AS edad_minima, MAX(edad) AS edad_maxima FROM users;   