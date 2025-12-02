-------------- SENTENCIAS EN SQL ----------------
-- DISTINCT EN SQL --

#El distinct se utiliza para eliminar los registros duplicados en los resultados de una consulta.

#Mostrar toda la información de la tabla users sin registros duplicados.
SELECT DISTINCT * FROM users;

#Mostrar solo la columna edad de la tabla users sin registros duplicados.
SELECT DISTINCT edad FROM users;

#Mostrar solo la columna name de la tabla users sin registros duplicados donde el año sea igual a 2021.
SELECT DISTINCT name FROM users WHERE año = 2021;

#Mostrar solo la columna edad de la tabla users sin registros duplicados donde la edad sea mayor a 18.
SELECT DISTINCT edad FROM users WHERE edad > 18;


