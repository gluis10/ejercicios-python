-------------- SENTENCIAS EN SQL ----------------
-- AND - OR - NOT EN SQL --

#El AND se utiliza para combinar dos o más condiciones en una consulta SQL.
#El OR se utiliza para especificar múltiples condiciones, donde al menos una debe ser verdadera.
#El NOT se utiliza para negar una condición en una consulta SQL.

#Mostrar toda la información de la tabla users donde el email no sea igual a "sara@gmail.com".
SELECT * FROM users WHERE NOT email = "sara@gmail.com";

#Mostrar toda la información de la tabla users donde el email no sea igual a "sara@gmail.com" y la edad sea 15. 
SELECT * FROM users WHERE NOT email = "sara@gmail.com" AND edad = 15;

#Mostrar toda la información de la tabla users donde el email no sea igual a "sara@gmail.com" o la edad sea 15.
SELECT * FROM users WHERE NOT email = "sara@gmail.com" OR edad = 15;
-- Si cumple alguna de las dos condiciones se mostrará el resultado.




