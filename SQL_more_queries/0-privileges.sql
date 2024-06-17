-- lists all privileges for user_0d_1 and user_0d_2 on the server

SELECT * FROM information_schema.user_privileges
WHERE user = 'user_0d_1' OR user = 'user_0d_2';
