-- Ensure the users do not exist before proceeding
DROP USER IF EXISTS 'user_0d_1'@'localhost';
DROP USER IF EXISTS 'user_0d_2'@'localhost';

-- Re-check if users exist to match expected output
SELECT user FROM mysql.user WHERE user IN ('user_0d_1', 'user_0d_2');

-- Create new users
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant necessary privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT SELECT, INSERT ON `user_2_db`.* TO 'user_0d_2'@'localhost';

-- Display grants for confirmation
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
