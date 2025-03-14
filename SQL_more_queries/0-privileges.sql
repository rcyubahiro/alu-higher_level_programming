-- File: main_0_0.sql
-- Attempt to create users and handle the grant error
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'password';
-- Expect error message if GRANT is not allowed
-- Expected: There is no such grant defined for user 'user_0d_1' on host 'localhost'

-- File: main_2_0.sql
-- Grant full privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Grant full privileges to user_0d_2
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;

-- Attempt to revoke privileges to test error 1269
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user_0d_1'@'localhost';
-- Expected error: Can't revoke all privileges for one or more of the requested users

-- File: main_3_0.sql
-- Grant specific privileges to users on user_2_db
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';
-- Grant root privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
