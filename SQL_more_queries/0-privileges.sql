-- Check if user_0d_1 exists
SELECT COUNT(*) INTO @user_0d_1_exists FROM mysql.user WHERE user='user_0d_1' AND host='localhost';
SELECT 'user_0d_1_exists', @user_0d_1_exists;

-- If user_0d_1 exists, show grants
IF @user_0d_1_exists THEN
    SHOW GRANTS FOR 'user_0d_1'@'localhost';
ELSE
    SELECT 'There is no such grant defined for user ''user_0d_1'' on host ''localhost''';
END IF;

-- Check if user_0d_2 exists
SELECT COUNT(*) INTO @user_0d_2_exists FROM mysql.user WHERE user='user_0d_2' AND host='localhost';
SELECT 'user_0d_2_exists', @user_0d_2_exists;

-- If user_0d_2 exists, show grants
IF @user_0d_2_exists THEN
    SHOW GRANTS FOR 'user_0d_2'@'localhost';
ELSE
    SELECT 'There is no such grant defined for user ''user_0d_2'' on host ''localhost''';
END IF;
