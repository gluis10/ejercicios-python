-------------- SENTENCIAS EN SQL ----------------
-- LIKE EN SQL --

#El like se utiliza para buscar un patrón específico en una columna de texto.

#Mostrar toda la información de la tabla users donde el email sea similar a "sara@gmail.com".
SELECT * FROM users WHERE email = "sara@gmail.com";

#Mostrar toda la información de la tabla users donde el email termine con "gmail.com".
SELECT * FROM users WHERE email LIKE "%gmail.com";

#Mostrar toda la información de la tabla users donde el email empieza con "sara".
SELECT * FROM users WHERE email LIKE "sara%";

#Mostrar toda la información de la tabla users donde el email contenga "@".
SELECT * FROM user WHERE email LIKE "%@%";



