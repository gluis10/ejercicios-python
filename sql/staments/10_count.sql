-------------- SENTENCIAS EN SQL ----------------
-- COUNT EN SQL --

#El COUNT se utiliza para contar el número de filas que cumplen con una condición específica en una consulta SQL.

#Contar el número total de registros en la tabla users.
SELECT COUNT(*) FROM users;

#Contar cuántos registros tienen un valor en la columna edad dentro de la tabla users.
SELECT COUNT(edad) FROM users;



----------- GENERADO POR IA -----------

#Contar el número de registros en la tabla users donde la edad sea mayor a 18.
SELECT COUNT(*) FROM users WHERE edad > 18;

#Contar el número de registros en la tabla users donde el email contenga "gmail.com".
SELECT COUNT(*) FROM users WHERE email LIKE "%gmail.com";

#Contar el número de registros distintos en la columna edad de la tabla users.
SELECT COUNT(DISTINCT edad) FROM users;

#Contar el número de registros en la tabla users donde el año sea igual a 2021.
SELECT COUNT(*) FROM users WHERE año = 2021;

#Contar el número de registros en la tabla users donde la edad sea menor a 30 y el email contenga "example.com".
SELECT COUNT(*) FROM users WHERE edad < 30 AND email LIKE "%example.com";
#Contar el número de registros en la tabla users donde el email no sea igual a "example.com".
SELECT COUNT(*) FROM users WHERE email <> "example.com";
#Contar el número de registros en la tabla users donde el email termine con "yahoo.com".
SELECT COUNT(*) FROM users WHERE email LIKE "%yahoo.com";
#Contar el número de registros en la tabla users donde la edad sea igual a 25 o 30.
SELECT COUNT(*) FROM users WHERE edad = 25 OR edad = 30;
#Contar el número de registros en la tabla users donde el email empiece con "john".
SELECT COUNT(*) FROM users WHERE email LIKE "john%";
#Contar el número de registros en la tabla users donde la edad sea mayor a 18 y menor a 30.
SELECT COUNT(*) FROM users WHERE edad > 18 AND edad < 30;
#Contar el número de registros en la tabla users donde el email contenga "hotmail.com" y la edad sea mayor a 20.
SELECT COUNT(*) FROM users WHERE email LIKE "%hotmail.com" AND edad > 20;
#Contar el número de registros en la tabla users donde el email no contenga "gmail.com".
SELECT COUNT(*) FROM users WHERE email NOT LIKE "%gmail.com";
#Contar el número de registros en la tabla users donde la edad sea igual a 18, 25 o 30.
SELECT COUNT(*) FROM users WHERE edad IN (18, 25, 30);
#Contar el número de registros en la tabla users donde la edad sea mayor a 21 o el email termine con "edu".
SELECT COUNT(*) FROM users WHERE edad > 21 OR email LIKE "%edu";
#Contar el número de registros en la tabla users donde el email sea igual a "
SELECT COUNT(*) FROM users WHERE email = "example.com";example.com";
#Contar el número de registros en la tabla users donde la edad sea menor a 18 o mayor a 65.
SELECT COUNT(*) FROM users WHERE edad < 18 OR edad > 65;
#Contar el número de registros en la tabla users donde el email empiece con "admin" y la edad sea menor a 50.
SELECT COUNT(*) FROM users WHERE email LIKE "admin%" AND edad < 50;
#Contar el número de registros en la tabla users donde la edad sea igual a 30.
SELECT COUNT(*) FROM users WHERE edad = 30;
#Contar el número de registros en la tabla users donde el email contenga "pro".
SELECT COUNT(*) FROM users WHERE email LIKE "%pro%";
#Contar el número de registros en la tabla users donde la edad sea mayor a 40.
SELECT COUNT(*) FROM users WHERE edad > 40;
#Contar el número de registros en la tabla users donde el email termine con "org".
SELECT COUNT(*) FROM users WHERE email LIKE "%org";
#Contar el número de registros en la tabla users donde la edad sea menor a 25.
SELECT COUNT(*) FROM users WHERE edad < 25;
#Contar el número de registros en la tabla users donde el email empiece con "user".
SELECT COUNT(*) FROM users WHERE email LIKE "user%";
#Contar el número de registros en la tabla users donde la edad sea igual a 21.
SELECT COUNT(*) FROM users WHERE edad = 21;
#Contar el número de registros en la tabla users donde el email contenga "test".
SELECT COUNT(*) FROM users WHERE email LIKE "%test%";
#Contar el número de registros en la tabla users donde la edad sea mayor a 50.
SELECT COUNT(*) FROM users WHERE edad > 50;
#Contar el número de registros en la tabla users donde el email termine con "net".
SELECT COUNT(*) FROM users WHERE email LIKE "%net";
#Contar el número de registros en la tabla users donde la edad sea menor a 20.
SELECT COUNT(*) FROM users WHERE edad < 20;
#Contar el número de registros en la tabla users donde el email empiece con "guest".
SELECT COUNT(*) FROM users WHERE email LIKE "guest%";
#Contar el número de registros en la tabla users donde la edad sea igual a 35.
SELECT COUNT(*) FROM users WHERE edad = 35;
#Contar el número de registros en la tabla users donde el email contenga "info".
SELECT COUNT(*) FROM users WHERE email LIKE "%info%";
#Contar el número de registros en la tabla users donde la edad sea mayor a 60.
SELECT COUNT(*) FROM users WHERE edad > 60;
#Contar el número de registros en la tabla users donde el email termine con "co".
SELECT COUNT(*) FROM users WHERE email LIKE "%co";
#Contar el número de registros en la tabla users donde la edad sea menor a 22.
SELECT COUNT(*) FROM users WHERE edad < 22;
#Contar el número de registros en la tabla users donde el email empiece con "member".
SELECT COUNT(*) FROM users WHERE email LIKE "member%";
#Contar el número de registros en la tabla users donde la edad sea igual a 28.
SELECT COUNT(*) FROM users WHERE edad = 28;
#Contar el número de registros en la tabla users donde el email contenga "service".
SELECT COUNT(*) FROM users WHERE email LIKE "%service%";
#Contar el número de registros en la tabla users donde la edad sea mayor a 45.
SELECT COUNT(*) FROM users WHERE edad > 45;
#Contar el número de registros en la tabla users donde el email termine con "biz".
SELECT COUNT(*) FROM users WHERE email LIKE "%biz";
#Contar el número de registros en la tabla users donde la edad sea menor a 27.
SELECT COUNT(*) FROM users WHERE edad < 27;
#Contar el número de registros en la tabla users donde el email empiece con "customer".
SELECT COUNT(*) FROM users WHERE email LIKE "customer%";
#Contar el número de registros en la tabla users donde la edad sea igual a 32.
SELECT COUNT(*) FROM users WHERE edad = 32;
#Contar el número de registros en la tabla users donde el email contenga "support".
SELECT COUNT(*) FROM users WHERE email LIKE "%support%";
#Contar el número de registros en la tabla users donde la edad sea mayor a 55.
SELECT COUNT(*) FROM users WHERE edad > 55;
#Contar el número de registros en la tabla users donde el email termine con "info".
SELECT COUNT(*) FROM users WHERE email LIKE "%info";    
#Contar el número de registros en la tabla users donde la edad sea menor a 29.
SELECT COUNT(*) FROM users WHERE edad < 29;
#Contar el número de registros en la tabla users donde el email empiece con "admin".
SELECT COUNT(*) FROM users WHERE email LIKE "admin%";
#Contar el número de registros en la tabla users donde la edad sea igual a 40.
SELECT COUNT(*) FROM users WHERE edad = 40;
#Contar el número de registros en la tabla users donde el email contenga "mail".
SELECT COUNT(*) FROM users WHERE email LIKE "%mail%";
#Contar el número de registros en la tabla users donde la edad sea mayor a 35.
SELECT COUNT(*) FROM users WHERE edad > 35;
#Contar el número de registros en la tabla users donde el email termine con "site".
SELECT COUNT(*) FROM users WHERE email LIKE "%site";
#Contar el número de registros en la tabla users donde la edad sea menor a 24.
SELECT COUNT(*) FROM users WHERE edad < 24;
#Contar el número de registros en la tabla users donde el email empiece con "test".
SELECT COUNT(*) FROM users WHERE email LIKE "test%";
#Contar el número de registros en la tabla users donde la edad sea igual a 27.
SELECT COUNT(*) FROM users WHERE edad = 27;
#Contar el número de registros en la tabla users donde el email contenga "user".
SELECT COUNT(*) FROM users WHERE email LIKE "%user%";
#Contar el número de registros en la tabla users donde la edad sea mayor a 70.
SELECT COUNT(*) FROM users WHERE edad > 70;
#Contar el número de registros en la tabla users donde el email termine con "club".
SELECT COUNT(*) FROM users WHERE email LIKE "%club";
#Contar el número de registros en la tabla users donde la edad sea menor a 26.
SELECT COUNT(*) FROM users WHERE edad < 26;

----------- FIN GENERADO POR IA -----------










