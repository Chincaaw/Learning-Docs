-- show all software component responsible for storing managing, and accessing data within tables.
SHOW ENGINES;
-- display a list of tables in the currently selected database or schema.
SHOW TABLES;
-- create a new table in a database.
CREATE TABLE item(  
    id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    price INT DEFAULT 0,
    stock INT DEFAULT 0
) ENGINE = InnoDB;
-- delete a table and all its data permanently from the database.
DROP TABLE item;
-- retrieve metadata about a table, such as its structure, column names, data types, constraints, and indexes.
DESCRIBE item;
DESC item;
-- display the SQL query that was used to create a specific table.
SHOW CREATE TABLE item;
-- modify an existing table.
ALTER TABLE item
ADD COLUMN description TEXT;

ALTER TABLE item
DROP COLUMN description;

ALTER TABLE item
MODIFY name VARCHAR(200) AFTER price;

ALTER TABLE item
MODIFY name VARCHAR(100) FIRST;

ALTER TABLE item
MODIFY id INT NOT NULL,
MODIFY name VARCHAR(100) NOT NULL,
MODIFY price INT NOT NULL;

ALTER TABLE item
ADD created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;
-- add new rows of data into a table.
INSERT INTO item(id, name) VALUES(1, 'Apple');
-- retrieve data from one or more tables.
SELECT * FROM item;
--  remove all rows from a table quickly, effectively performing the same action as a DELETE statement without the WHERE clause.
TRUNCATE item;

-- delete an entire table from the database.
DROP TABLE item;
