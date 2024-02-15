-- a script that creates a database from the specified name and a table into the database from the specified name on a MySQL server
-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- specify database to use for table creation
USE hbtn_0d_usa;

-- create the table with the relevant constraints
CREATE TABLE IF NOT EXISTS states (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
