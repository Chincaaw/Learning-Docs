-- Create a table to store wishlist items
CREATE TABLE wishlist
(
    id          INT         NOT NULL AUTO_INCREMENT, -- Unique identifier for each wishlist item
    id_product  VARCHAR(10) NOT NULL, -- Identifier of the product in the wishlist
    description TEXT, -- Description of the wishlist item
    PRIMARY KEY (id), -- Primary key constraint on 'id' column
    CONSTRAINT fk_wishlist_product -- Foreign key constraint to link to products table
        FOREIGN KEY (id_product) REFERENCES products (id)
) ENGINE = InnoDB;

-- Describe the structure of the 'wishlist' table
DESCRIBE wishlist;

-- Show the SQL query used to create the 'wishlist' table
SHOW CREATE TABLE wishlist;

-- Drop the existing foreign key constraint
ALTER TABLE wishlist
    DROP CONSTRAINT fk_wishlist_product;

-- Add a new foreign key constraint with cascade actions for delete and update
ALTER TABLE wishlist
    ADD CONSTRAINT fk_wishlist_product
        FOREIGN KEY (id_product) REFERENCES products (id)
            ON DELETE CASCADE ON UPDATE CASCADE;

-- Insert some sample data into the 'wishlist' table
INSERT INTO wishlist(id_product, description)
VALUES ('P0001', 'Favorite Food'), -- Inserting a valid product ID
       ('SALAH', 'Favorite Food'); -- Inserting an invalid product ID

-- Select all data from the 'wishlist' table
SELECT * FROM wishlist;

-- Delete a product from the 'products' table that is referenced in the 'wishlist' table
DELETE
FROM products
WHERE id = 'Pxxxx'; -- Deleting a product with ID 'Pxxxx'

-- Try to insert a wishlist item with a non-existent product ID
INSERT INTO wishlist(id_product, description)
VALUES ('Pxxxx', 'Favorite Food');

-- Join 'wishlist' table with 'products' table to fetch related product information
SELECT *
FROM wishlist
         JOIN products ON (wishlist.id_product = products.id);

-- Select specific columns from 'wishlist' and 'products' tables with aliases
SELECT w.id          as wishlist_id,
       p.id          AS product_id,
       p.name        as product_name,
       w.description AS wishlist_description
FROM wishlist AS w
         JOIN products AS p ON (w.id_product = p.id);

-- Describe the structure of the 'wishlist' table after modifications
DESC wishlist;

-- Add a new column 'id_customer' to the 'wishlist' table
ALTER TABLE wishlist
ADD COLUMN id_customer INT;

-- Add a foreign key constraint to link 'id_customer' column to 'customers' table
ALTER TABLE wishlist
ADD CONSTRAINT fk_wishlist_customer
FOREIGN KEY (id_customer) REFERENCES customers(id);

-- Select all data from the 'customers' table
SELECT * FROM customers;

-- Update the 'id_customer' column in the 'wishlist' table for a specific entry
UPDATE wishlist
SET id_customer = 1
WHERE id = 1;

-- Select all data from the 'wishlist' table after the update
SELECT * FROM wishlist;

-- Select relevant information from 'wishlist', 'products', and 'customers' tables
SELECT customers.email, products.id, products.name, wishlist.description
FROM wishlist
JOIN products ON (products.id = wishlist.id_product)
JOIN customers ON (customers.id = wishlist.id_customer);
