-- Creating a table to store information about sellers
DROP TABLE sellers;

CREATE TABLE sellers
(
    id    INT          NOT NULL AUTO_INCREMENT, -- Unique identifier for each seller
    name  VARCHAR(100) NOT NULL, -- Name of the seller
    name2 VARCHAR(100), -- Secondary name of the seller (if any)
    name3 VARCHAR(100), -- Tertiary name of the seller (if any)
    email VARCHAR(100) NOT NULL, -- Email address of the seller
    PRIMARY KEY (id), -- Defining primary key constraint
    UNIQUE KEY email_unique (email), -- Ensuring email uniqueness
    INDEX name_index (name), -- Indexing the name column
    INDEX name2_index (name2), -- Indexing the name2 column
    INDEX name3_index (name3), -- Indexing the name3 column
    INDEX name1_name2_name3_index (name, name2, name3) -- Indexing a combination of name, name2, and name3 columns
) ENGINE = InnoDB; -- Specifying storage engine

-- Describing the structure of the sellers table
DESC sellers;

-- Showing the SQL query used to create the sellers table
SHOW CREATE TABLE sellers;

-- Retrieving sellers with the name 'X'
SELECT * FROM sellers WHERE name = 'X';

-- Retrieving sellers with the name 'X' and secondary name 'X'
SELECT * FROM sellers WHERE name = 'X' AND name2 = 'X';

-- Retrieving sellers with the secondary name 'X'
SELECT * FROM sellers WHERE name2 = 'X';

-- Retrieving sellers with the name 'X', secondary name 'X', and tertiary name 'X'
SELECT * FROM sellers WHERE name = 'X' AND name2 = 'X' AND name3 = 'X';

-- Altering the sellers table to drop the name_index index
ALTER TABLE sellers DROP INDEX name_index;
