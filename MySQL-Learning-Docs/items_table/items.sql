-- Show available database engines
DROP TABLE items;

SHOW ENGINES;

-- Show existing tables in the database
SHOW TABLES;

DROP TABLE items;
-- Create a table to store item information
CREATE TABLE items
(
    id      INT          NOT NULL, -- Unique identifier for each item
    name    VARCHAR(100) NOT NULL, -- Name of the item
    price   INT          NOT NULL DEFAULT 0, -- Price of the item with default value 0
    quantity INT         NOT NULL DEFAULT 0 -- Quantity of the item with default value 0
) ENGINE = InnoDB; -- Using InnoDB engine for table

-- Describe the structure of the items table
DESCRIBE items;

-- Show the SQL statement used to create the items table
SHOW CREATE TABLE items;

-- Add a column to the items table to store item descriptions
ALTER TABLE items
    ADD COLUMN description TEXT;

-- Add a column to the items table to store a placeholder value
ALTER TABLE items
    ADD COLUMN placeholder TEXT;

-- Remove the 'placeholder' column from the items table
ALTER TABLE items
    DROP COLUMN placeholder;

-- Modify the 'name' column in the items table to have a maximum length of 200 characters and place it after the 'description' column
ALTER TABLE items
    MODIFY name VARCHAR(200) AFTER description;

-- Modify the 'name' column in the items table to be the first column
ALTER TABLE items
    MODIFY name VARCHAR(200) FIRST;

-- Modify the 'id' column in the items table to be not null
ALTER TABLE items
    MODIFY id INT NOT NULL;

-- Modify the 'name' column in the items table to be not null
ALTER TABLE items
    MODIFY name VARCHAR(200) NOT NULL;

-- Show the SQL statement used to create the items table after modifications
SHOW CREATE TABLE items;

-- Modify the 'quantity' column in the items table to be not null with a default value of 0
ALTER TABLE items
    MODIFY quantity INT NOT NULL DEFAULT 0;

-- Modify the 'price' column in the items table to be not null with a default value of 0
ALTER TABLE items
    MODIFY price INT NOT NULL DEFAULT 0;

-- Add a column to store the creation timestamp of the item
ALTER TABLE items
    ADD created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;

-- Insert an item record into the items table
INSERT INTO items (id, name)
VALUES (1, 'Apple');

-- Retrieve all records from the items table
SELECT *
FROM items;

-- Remove all records from the items table
TRUNCATE items;

-- Show existing tables in the database after truncating the items table
SHOW tables;

-- Drop the items table from the database
DROP TABLE items;
