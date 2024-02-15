-- a script that creates a table from the specified name on a MySQL server with unqiue ID
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
