-- Grant all privileges to user_0d_1 (root user)
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Ensure privileges are applied
FLUSH PRIVILEGES;

-- Revoke all privileges from user_0d_2 (if necessary to reset)
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user_0d_2'@'localhost';

-- Grant only SELECT and INSERT privileges to user_0d_2 on user_2_db
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;

-- Optional: Verify grants (uncomment if needed)
-- SHOW GRANTS FOR 'user_0d_1'@'localhost';
-- SHOW GRANTS FOR 'user_0d_2'@'localhost';
