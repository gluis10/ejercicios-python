-------------- SENTENCIAS EN SQL ----------------
-- NULL EN SQL --

#El NULL se utiliza para representar un valor desconocido o ausente en una columna de una tabla.

#Mostrar toda la información de la tabla users donde el email sea NULL.
SELECT * FROM users WHERE email IS NULL;

/*
Por ejemplo, si tenemos una tabla de usuarios y algunos usuarios no han proporcionado su dirección de correo electrónico, el valor de la columna de correo electrónico para esos usuarios será NULL. Al realizar consultas, podemos utilizar IS NULL para filtrar y obtener solo aquellos registros donde el valor es NULL. 
*/
/*
O por ejemplo si tengo una aplicación de gestión de empleados y algunos empleados no tienen un número de teléfono registrado, el valor del número de teléfono para esos empleados será NULL. Al realizar consultas, podemos utilizar IS NULL para filtrar y obtener solo aquellos registros donde el número de teléfono es NULL.
*/

#Mostrar toda la información de la tabla users donde el email no sea NULL.
SELECT * FROM users WHERE email IS NOT NULL;

#Mostrar toda la información de la tabla users donde el email no sea NULL y la edad sea mayor a 18.
SELECT * FROM users WHERE email IS NOT NULL AND edad > 18;


