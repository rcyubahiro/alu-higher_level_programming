-- Check if user_0d_1 exists
SELECT EXISTS(
    SELECT 1 FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost'
) AS user_0d_1_exists;

-- Check if user_0d_2 exists
SELECT EXISTS(
    SELECT 1 FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost'
) AS user_0d_2_exists;

-- Create user_0d_1 if not exists and grant privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Create user_0d_2 if not exists and grant SELECT, INSERT privileges
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Display the grants for both users
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

-- Attempt to revoke all privileges (This will trigger error if not possible)
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user_0d_1'@'localhost';
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user_0d_2'@'localhost';
