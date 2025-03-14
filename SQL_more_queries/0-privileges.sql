-- Fix privileges for user_0d_1 to match the expected root privileges
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user_0d_1'@'localhost';

GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, 
      ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, 
      REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, 
      TRIGGER, CREATE TABLESPACE, CREATE ROLE, DROP ROLE 
ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

GRANT APPLICATION_PASSWORD_ADMIN, AUDIT_ADMIN, BACKUP_ADMIN, BINLOG_ADMIN, BINLOG_ENCRYPTION_ADMIN, 
      CLONE_ADMIN, CONNECTION_ADMIN, ENCRYPTION_KEY_ADMIN, FLUSH_OPTIMIZER_COSTS, FLUSH_STATUS, 
      FLUSH_TABLES, FLUSH_USER_RESOURCES, GROUP_REPLICATION_ADMIN, INNODB_REDO_LOG_ARCHIVE, 
      INNODB_REDO_LOG_ENABLE, PERSIST_RO_VARIABLES_ADMIN, REPLICATION_APPLIER, REPLICATION_SLAVE_ADMIN, 
      RESOURCE_GROUP_ADMIN, RESOURCE_GROUP_USER, ROLE_ADMIN, SERVICE_CONNECTION_ADMIN, 
      SESSION_VARIABLES_ADMIN, SET_USER_ID, SHOW_ROUTINE, SYSTEM_USER, SYSTEM_VARIABLES_ADMIN, 
      TABLE_ENCRYPTION_ADMIN, XA_RECOVER_ADMIN 
ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Fix privileges for user_0d_2
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user_0d_2'@'localhost';

GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Verify the changes
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
