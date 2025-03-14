-- Ensure user_0d_1 exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';

-- Ensure user_0d_2 exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant some privileges to user_0d_2 (if necessary)
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- Display privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Display privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
