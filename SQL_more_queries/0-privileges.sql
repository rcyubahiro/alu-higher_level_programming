-- Ensure a clean start
DROP USER IF EXISTS 'user_0d_1'@'localhost';
DROP USER IF EXISTS 'user_0d_2'@'localhost';

-- Case 1: Verify users don't exist
SELECT user FROM mysql.user WHERE user IN ('user_0d_1', 'user_0d_2');

-- Case 2: Create user_0d_1 with root access
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'password1';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Case 3: Create user_0d_2 with root access
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'password2';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;

-- Case 4: Modify user_0d_2 to have only SELECT & INSERT on user_2_db
CREATE DATABASE IF NOT EXISTS user_2_db;
REVOKE ALL PRIVILEGES ON *.* FROM 'user_0d_2'@'localhost';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Verify grants
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
