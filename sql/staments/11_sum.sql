-------------- SENTENCIAS EN SQL ----------------
-- SUM EN SQL --

#La función SUM se utiliza para calcular la suma total de una columna numérica en una tabla.

#Mostrar la suma total de la columna edad de la tabla users.
SELECT SUM(edad) FROM users;

----------- GENERADO POR IA -----------

#Mostrar la suma total de la columna edad de la tabla users donde el año sea igual a 2021.
SELECT SUM(edad) FROM users WHERE año = 2021;
#Mostrar la suma total de la columna edad de la tabla users donde la edad sea mayor a 18.
SELECT SUM(edad) FROM users WHERE edad > 18;
#Mostrar la suma total de la columna edad de la tabla users donde el email contenga "gmail.com".
SELECT SUM(edad) FROM users WHERE email LIKE "%gmail.com";
#Mostrar la suma total de la columna edad de la tabla users donde el email no sea igual a "gmail.com".
SELECT SUM(edad) FROM users WHERE email NOT LIKE "%gmail.com";
#Mostrar la suma total de la columna edad de la tabla users donde el email no sea igual a "gmail.com".
SELECT SUM(edad) FROM users WHERE NOT email LIKE "%gmail.com";
#Mostrar la suma total de la columna edad de la tabla users donde el email no sea igual a "gmail.com" y la edad sea mayor a 18.
SELECT SUM(edad) FROM users WHERE NOT email LIKE "%gmail.com" AND edad > 18;
#Mostrar la suma total de la columna edad de la tabla users donde el email no sea igual a "gmail.com" o la edad sea mayor a 18.
SELECT SUM(edad) FROM users WHERE NOT email LIKE "%gmail.com" OR edad > 18;
#Mostrar la suma total de la columna edad de la tabla users donde el email no sea igual a "gmail.com" o la edad sea mayor a 18, pero solo los primeros 2 registros.
SELECT SUM(edad) FROM users WHERE NOT email LIKE "%gmail.com" OR edad > 18 LIMIT 2;
#Mostrar la suma total de la columna edad de la tabla users sin registros duplicados.
SELECT SUM(DISTINCT edad) FROM users;
#Mostrar la suma total de la columna edad de la tabla users sin registros duplicados donde el email contenga "gmail.com".
SELECT SUM(DISTINCT edad) FROM users WHERE email LIKE "%gmail.com";

----------- FIN GENERADO POR IA -----------









