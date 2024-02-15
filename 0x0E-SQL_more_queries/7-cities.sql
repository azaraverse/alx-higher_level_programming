-- a script that creates a database with the specified name and a table with the specified name into the database on a MySQL server
-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- specify the database to use
USE hbtn_0d_usa;

-- create the table with the relevant constraints
CREATE TABLE IF NOT EXISTS cities (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id), name VARCHAR(256) NOT NULL);
