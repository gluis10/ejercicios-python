-------------- SENTENCIAS EN SQL ----------------
-- ORDER BY EN SQL --

#El order by se utiliza para ordenar los registros en los resultados de una consulta, ya sea en orden ascendente (ASC) o descendente (DESC).

#Mostrar toda la información de la tabla users ordenada por la columna edad en orden ascendente.
SELECT * FROM users ORDER BY edad ASC;

#Mostrar toda la información de la tabla users ordenada por la columna edad en orden descendente.
SELECT * FROM users ORDER BY edad DESC;

-- Cuando no le ponemos ASC o DESC, por defecto se ordena en orden ascendente.

#Mostrar toda la información de la tabla users donde el email sea igual a "sara@example.com";
SELECT * FROM users WHERE email = "sara@example.com";

#Mostrar toda la información de la tabla users donde el email sea igual a "sara@example.com" ordenada por la columna edad en orden descendente.
SELECT * FROM users WHERE email = "sara@example.com" ORDER BY edad DESC;

#Mostrar solo la columna name de la tabla users donde el email sea igual a "sara@example.com" ordenada por la columna edad en orden descendente.
SELECT name FROM users WHERE email = "sara@example.com" ORDER BY edad DESC;

