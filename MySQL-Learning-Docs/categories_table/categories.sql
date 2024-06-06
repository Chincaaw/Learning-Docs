-- Create a table to store categories with an ID and name
DROP TABLE categories;

CREATE TABLE categories
(
    id   VARCHAR(10)  NOT NULL, -- Unique identifier for the category
    name VARCHAR(100) NOT NULL, -- Name of the category
    PRIMARY KEY (id)            -- Define the primary key
) ENGINE = InnoDB;

-- Describe the structure of the categories table
DESCRIBE categories;

-- Remove the category column from the products table
ALTER TABLE products
    DROP COLUMN category;

-- Describe the structure of the products table after dropping the column
DESCRIBE products;

-- Add a new column to the products table to store the category ID
ALTER TABLE products
    ADD COLUMN id_category VARCHAR(10);

-- Add a foreign key constraint to link products to categories
ALTER TABLE products
    ADD CONSTRAINT fk_products_categories
        FOREIGN KEY (id_category) REFERENCES categories (id);

-- Display the SQL statement used to create the products table
SHOW CREATE TABLE products;

-- Display all records from the products table
SELECT *
FROM products;

-- Display all records from the categories table
SELECT *
FROM categories;

-- Insert categories into the categories table
INSERT INTO categories(id, name)
VALUES ('C0001', 'Food'),
       ('C0002', 'Beverage'),
       ('C0003', 'Others');

-- Update products with corresponding category IDs
UPDATE products
SET id_category = 'C0001'
WHERE id IN ('P0001', 'P0002', 'P0003', 'P0004', 'P0005', 'P0006', 'P0013', 'P0014', 'P0015');

UPDATE products
SET id_category = 'C0002'
WHERE id IN ('P0007', 'P0008', 'P0009');

UPDATE products
SET id_category = 'C0003'
WHERE id IN ('P0010', 'P0011', 'P0012', 'P0016');

-- Retrieve product information along with category names
SELECT products.id, products.name, categories.name
FROM products
         JOIN categories ON (categories.id = products.id_category);

-- Display all records from the categories table
SELECT *
FROM categories;

-- Insert new categories into the categories table
INSERT INTO categories(id, name)
VALUES ('C0004', 'Souvenirs'),
       ('C0005', 'Gadgets');

-- Perform various types of joins between categories and products
SELECT *
FROM categories
         INNER JOIN products ON (products.id_category = categories.id);

SELECT *
FROM categories
         JOIN products ON (products.id_category = categories.id);

SELECT *
FROM categories
         LEFT JOIN products ON (products.id_category = categories.id);

SELECT *
FROM categories
         RIGHT JOIN products ON (products.id_category = categories.id);

SELECT *
FROM categories
         CROSS JOIN products;

-- Create a table to generate numbers from 1 to 10
CREATE TABLE numbers
(
    id INT NOT NULL,
    PRIMARY KEY (id)
) ENGINE = InnoDB;

-- Insert numbers from 1 to 10 into the numbers table
INSERT INTO numbers(id)
VALUES (1),
       (2),
       (3),
       (4),
       (5),
       (6),
       (7),
       (8),
       (9),
       (10);

-- Perform a cross join between the numbers table to get multiplication results
SELECT numbers1.id, numbers2.id, (numbers1.id * numbers2.id)
FROM numbers as numbers1
         CROSS JOIN numbers as numbers2
ORDER BY numbers1.id, numbers2.id;
