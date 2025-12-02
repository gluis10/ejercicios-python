-------------- SENTENCIAS EN SQL ----------------
-- AVG EN SQL --

#El AVG se utiliza para calcular el valor promedio de una columna numérica en una tabla.

#Mostrar el valor promedio de la columa edad de la tabla users.
SELECT AVG(edad) FROM users;

----------- GENERADO POR IA -----------
#Mostrar el valor promedio de la columna edad de la tabla users donde el año sea igual a 2021.
SELECT AVG(edad) FROM users WHERE año = 2021;
#Mostrar el valor promedio de la columna edad de la tabla users donde la edad sea mayor a 18.
SELECT AVG(edad) FROM users WHERE edad > 18;
#Mostrar el valor promedio de la columna edad de la tabla users donde el email contenga "gmail.com".
SELECT AVG(edad) FROM users WHERE email LIKE "%gmail.com";
#Mostrar el valor promedio de la columna edad de la tabla users donde el email no sea igual a "gmail.com".
SELECT AVG(edad) FROM users WHERE email NOT LIKE "%gmail.com";
#Mostrar el valor promedio de la columna edad de la tabla users donde el email no sea igual a "gmail.com".
SELECT AVG(edad) FROM users WHERE NOT email LIKE "%gmail.com";
#Mostrar el valor promedio de la columna edad de la tabla users donde el email no sea igual a "gmail.com" y la edad sea mayor a 18.
SELECT AVG(edad) FROM users WHERE NOT email LIKE "%gmail.com" AND edad > 18;
#Mostrar el valor promedio de la columna edad de la tabla users donde el email no sea igual a "gmail.com" o la edad sea mayor a 18.
SELECT AVG(edad) FROM users WHERE NOT email LIKE "%gmail.com" OR edad > 18;
#Mostrar el valor promedio de la columna edad de la tabla users donde el email no sea igual a "gmail.com" o la edad sea mayor a 18, pero solo los primeros 2 registros.
SELECT AVG(edad) FROM users WHERE NOT email LIKE "%gmail.com" OR edad > 18 LIMIT 2;
#Mostrar el valor promedio de la columna edad de la tabla users sin registros duplicados.
SELECT AVG(DISTINCT edad) FROM users;
#Mostrar el valor promedio de la columna edad de la tabla users sin registros duplicados donde el email contenga "gmail.com".
SELECT AVG(DISTINCT edad) FROM users WHERE email LIKE "%gmail.com";
----------- FIN GENERADO POR IA -----------
