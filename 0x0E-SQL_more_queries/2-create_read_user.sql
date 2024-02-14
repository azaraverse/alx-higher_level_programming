-- a script that creates a specified database and a specified user
-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create the user with a password set to user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- grant SELECT privilege to user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- flush privileges to effect new privileges by reloading grant tables
FLUSH PRIVILEGES;
