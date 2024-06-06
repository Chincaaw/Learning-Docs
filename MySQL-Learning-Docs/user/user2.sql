-- Start a transaction
START TRANSACTION;

-- Select all records from the guestbooks table
SELECT * FROM guestbooks;

-- Update the title of a guestbook entry modified by User 1
UPDATE guestbooks
SET title = 'Modified By User 1'
WHERE id = 9;

-- Commit the transaction
COMMIT;

-- Start a new transaction
START TRANSACTION;

-- Select all records from the products table
SELECT * FROM products;

-- Select a specific product for update
SELECT * FROM products WHERE id = 'P0001' FOR UPDATE;

-- Update the quantity of a product after purchase
UPDATE products
SET quantity = quantity - 10
WHERE id = 'P0001';

-- Commit the transaction
COMMIT;

-- Start another transaction
START TRANSACTION;

-- Select a specific product for update (potential deadlock scenario)
SELECT * FROM products WHERE id = 'P0001' FOR UPDATE;

-- Select another product for update (potential deadlock scenario)
SELECT * FROM products WHERE id = 'P0002' FOR UPDATE;

-- Lock the products table for reading
LOCK TABLES products READ;

-- Update the quantity of a product (read lock)
UPDATE products
SET quantity = 100
WHERE id = 'P0001';

-- Release the table lock
UNLOCK TABLES;

-- Lock the products table for writing
LOCK TABLES products WRITE;

-- Update the quantity of a product (write lock)
UPDATE products
SET quantity = 100
WHERE id = 'P0001';

-- Select all records from the products table after the update
SELECT * FROM products;

-- Release the table lock
UNLOCK TABLES;

-- Lock the entire database instance for backup
LOCK INSTANCE FOR BACKUP;

-- Release the instance lock
UNLOCK INSTANCE;
