-------------- SENTENCIAS EN SQL ----------------
-- LIMIT EN SQL --
 
#El LIMIT se utiliza para limitar el número de filas devueltas por una consulta SQL.

#Mostrar toda la información de la tabla users pero solo los primeros 2 registros.
SELECT * FROM users LIMIT 2;

#Mostrar toda la información de la tabla users pero solo los primeros 3 registros.
SELECT * FROM users LIMIT 3;

#Mostrar toda la información de la tabla users donde el email no sea igual a "sara@gmail.com" o la edad sea 15.
SELECT * FROM users WHERE NOT email = "sara@gmail.com" OR edad = 15;

#Mostrar solo los primeros 2 registros de la consulta anterior.
SELECT * FROM users WHERE NOT email = "sara@gmail.com" OR edad = 15 LIMIT 2;