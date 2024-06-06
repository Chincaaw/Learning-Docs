-- Create a table named products to store information about products
DROP TABLE products;

CREATE TABLE products
(
    id          VARCHAR(10)  NOT NULL, -- Unique identifier for each product
    name        VARCHAR(100) NOT NULL, -- Name of the product
    description TEXT, -- Description of the product
    price       INT UNSIGNED NOT NULL, -- Price of the product
    quantity    INT UNSIGNED NOT NULL DEFAULT 0, -- Quantity of the product with a default value of 0
    created_at  TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the product was created
) ENGINE = InnoDB; -- Use InnoDB engine for table

-- Show all tables in the database
SHOW TABLES;

-- Describe the structure of the products table
DESCRIBE products;

-- Insert initial data of a product
INSERT INTO products(id, name, price, quantity)
VALUES ('P0001', 'Original Chicken Noodle', 15000, 100);

-- Retrieve all products from the products table
SELECT *
FROM products;

-- Insert additional product data with description
INSERT INTO products(id, name, description, price, quantity)
VALUES ('P0002', 'Chicken Noodle with Meatballs', 'Original Chicken Noodle with Meatballs', 20000, 100);

-- Insert multiple product data at once
INSERT INTO products(id, name, price, quantity)
VALUES ('P0003', 'Chicken Noodle with Chicken Feet', 20000, 100),
       ('P0004', 'Special Chicken Noodle', 25000, 100),
       ('P0005', 'Chicken Noodle with Egg Noodles', 15000, 100);

-- Retrieve specific columns from products table
SELECT id, name, price, quantity
FROM products;

-- Alter table to add primary key constraint on id column
ALTER TABLE products
    ADD PRIMARY KEY (id);

-- Describe the structure of the products table after alteration
DESCRIBE products;

-- Show the create table statement for products table
SHOW CREATE TABLE products;

-- Insert additional data for product P0001
INSERT INTO products(id, name, price, quantity)
VALUES ('P0001', 'Original Chicken Noodle', 15000, 100);

-- Select products with quantity equal to 100
SELECT *
FROM products
WHERE quantity = 100;

-- Select products with price equal to 15000
SELECT *
FROM products
WHERE price = 15000;

-- Select product with ID P0001
SELECT *
FROM products
WHERE id = 'P0001';

-- Select product with name "Chicken Noodle with Meatballs" ignoring case
SELECT *
FROM products
WHERE name LIKE '%chicken noodle with meatballs%';

-- Describe the structure of the products table
DESCRIBE products;

-- Alter table to add a new column category
ALTER TABLE products
    ADD COLUMN category ENUM ('Food', 'Beverage', 'Others')
        AFTER name;

-- Retrieve all products from the products table
SELECT *
FROM products;

-- Select product with ID P0001
SELECT *
FROM products
WHERE id = 'P0001';

-- Update the category of product with ID P0001 to "Food"
UPDATE products
SET category = 'Food'
WHERE id = 'P0001';

-- Update the category and description of product with ID P0003
UPDATE products
SET category    = 'Food',
    description = 'Original Chicken Noodle with Chicken Feet'
WHERE id = 'P0003';

-- Increase the price of product with ID P0005 by 5000
UPDATE products
SET price = price + 5000
WHERE id = 'P0005';

-- Insert new product data
INSERT INTO products(id, name, price, quantity)
VALUES ('P0009', 'Original Chicken Noodle', 15000, 100);

-- Delete product with ID P0009
DELETE
FROM products
WHERE id = 'P0009';

-- Select specific columns with renamed aliases
SELECT id       AS Code,
       name     AS Name,
       category AS Category,
       price    AS Price,
       quantity AS Quantity
FROM products;

-- Select specific columns with renamed aliases using table alias
SELECT p.id       AS Code,
       p.name     AS Name,
       p.category AS Category,
       p.price    AS Price,
       p.quantity AS Quantity
FROM products AS p;

-- Insert multiple new product data
INSERT INTO products(id, name, category, price, quantity)
VALUES ('P0006', 'Rib Meatballs', 'Food', 25000, 200),
       ('P0007', 'Orange Juice', 'Beverage', 10000, 300),
       ('P0008', 'Mixed Ice', 'Beverage', 15000, 500),
       ('P0009', 'Sweet Iced Tea', 'Beverage', 5000, 400),
       ('P0010', 'Crackers', 'Others', 2500, 1000),
       ('P0011', 'Shrimp Chips', 'Others', 10000, 300),
       ('P0012', 'Ice Cream', 'Others', 5000, 200),
       ('P0013', 'Chicken Noodle with Mushrooms', 'Food', 20000, 50),
       ('P0014', 'Meatball Soup', 'Food', 20000, 150),
       ('P0015', 'Jando Meatballs', 'Food', 25000, 300);

-- Select products with quantity greater than 100
SELECT *
FROM products
WHERE quantity > 100;

-- Select products with quantity greater than or equal to 100
SELECT *
FROM products
WHERE quantity >= 100;

-- Select products with category not equal to "Food"
SELECT *
FROM products
WHERE category != 'Food';

-- Select products with category not equal to "Beverage"
SELECT *
FROM products
WHERE category <> 'Beverage';

-- Select products with quantity greater than 100 and price greater than 20000
SELECT *
FROM products
WHERE quantity > 100
  AND price > 20000;

-- Select products with category "Food" and price less than 20000
SELECT *
FROM products
WHERE category = 'Food'
  AND price < 20000;

-- Select products with quantity greater than 100 or price greater than 20000
SELECT *
FROM products
WHERE (category = 'Food' OR quantity > 500)
  AND price > 20000;

-- Select products with name containing "noodle"
SELECT *
FROM products
WHERE name LIKE '%noodle%';

-- Select products with name containing "meatball"
SELECT *
FROM products
WHERE name LIKE '%meatball%';

-- Select products with name containing "usu"
SELECT *
FROM products
WHERE name LIKE '%usu%';

-- Select products with null description
SELECT *
FROM products
WHERE description IS NULL;

-- Select products with non-null description
SELECT *
FROM products
WHERE description IS NOT NULL;

-- Select products with price between 10000 and 20000
SELECT *
FROM products
WHERE price BETWEEN 10000 AND 20000;

-- Select products with price not between 10000 and 20000
SELECT *
FROM products
WHERE price NOT BETWEEN 10000 AND 20000;

-- Select products with category "Food" or "Beverage"
SELECT *
FROM products
WHERE category IN ('Food', 'Beverage');

-- Select products with category not "Food" or "Beverage"
SELECT *
FROM products
WHERE category NOT IN ('Food', 'Beverage');

-- Select products and order them by category
SELECT id, category, name
FROM products
ORDER BY category;

-- Select products and order them by category in ascending order and by price in descending order
SELECT id, category, price, name
FROM products
ORDER BY category ASC, price DESC;

-- Retrieve the first 5 products ordered by ID
SELECT *
FROM products
ORDER BY id
LIMIT 5;

-- Retrieve the first 3 products ordered by ID
SELECT *
FROM products
ORDER BY id
LIMIT 3;

-- Retrieve products starting from the 1st record, fetch 5 records ordered by ID
SELECT *
FROM products
ORDER BY id
LIMIT 0, 5;

-- Retrieve products starting from the 6th record, fetch 5 records ordered by ID
SELECT *
FROM products
ORDER BY id
LIMIT 5, 5;

-- Retrieve products starting from the 11th record, fetch 5 records ordered by ID
SELECT *
FROM products
ORDER BY id
LIMIT 10, 5;

-- Retrieve products starting from the 16th record, fetch 5 records ordered by ID
SELECT *
FROM products
ORDER BY id
LIMIT 15, 5;

-- Retrieve distinct categories from products
SELECT DISTINCT category
FROM products;

-- Perform a mathematical operation
SELECT 10, 10, 10 * 10 as Result;

-- Select product ID, name, price, and price divided by 1000
FROM products
WHERE price DIV 1000 > 15;

-- Select product ID, cosine of price, sine of price, and tangent of price
FROM products
WHERE price DIV 1000 > 15;

-- Select product ID, name in lower case, name in upper case, and length of name
SELECT id,
       LOWER(name)  as 'Name Lower',
       UPPER(name)  as 'Name Upper',
       LENGTH(name) as 'Name Length'
FROM products;

-- Select product ID, created_at timestamp, year of creation, and month of creation
SELECT id,
       created_at,
       EXTRACT(YEAR FROM created_at)  as Year,
       EXTRACT(MONTH FROM created_at) as Month
FROM products;

-- Select product ID, created_at timestamp, year of creation, and month of creation
SELECT id, created_at, YEAR(created_at), MONTH(created_at)
FROM products;

-- Select product ID, category, and categorized as "Delicious" if it's food, "Refreshing" if it's beverage, else "What's This?"
SELECT id,
       category,
       CASE category
           WHEN 'Food' THEN 'Delicious'
           WHEN 'Beverage' THEN 'Refreshing'
           ELSE 'What This?'
           END AS 'Category'
FROM products;

-- Select product ID, price, and categorized as "Cheap" if price is less than or equal to 15000, "Expensive" if less than or equal to 20000, else "Very Expensive"
SELECT id,
       price,
       IF(price <= 15000, 'Cheap', IF(price <= 20000, 'Expensive', 'Very Expensive')) as 'Expensive?'
FROM products;

-- Select product ID, name, and description. If description is null, display "Empty"
SELECT id, name, IFNULL(description, 'Empty')
FROM products;

-- Select total number of products
SELECT COUNT(id) as 'Total Products'
FROM products;

-- Select maximum price among products
SELECT MAX(price) as 'Most Expensive Product'
FROM products;

-- Select minimum price among products
SELECT MIN(price) as 'Cheapest Product'
FROM products;

-- Select average price of products
SELECT AVG(price) as 'Average Price'
FROM products;

-- Select sum of quantities of all products
SELECT SUM(quantity) AS 'Total Stock'
FROM products;

-- Select count of products grouped by category
SELECT COUNT(id) as 'Total Products', category
FROM products
GROUP BY category;

-- Select maximum price of products grouped by category
SELECT MAX(price) as 'Most Expensive Product', category
FROM products
GROUP BY category;

-- Select minimum price of products grouped by category
SELECT MIN(price) as 'Cheapest Product', category
FROM products
GROUP BY category;

-- Select average price of products grouped by category
SELECT AVG(price) as 'Average Price', category
FROM products
GROUP BY category;

-- Select sum of quantities of products grouped by category
SELECT SUM(quantity) AS 'Total Stock', category
FROM products
GROUP BY category;

-- Select count of products grouped by category having more than 5 products
SELECT COUNT(id) as total,
       category
FROM products
GROUP BY category
HAVING total > 5;

-- Retrieve all products
SELECT *
FROM products;

-- Insert new product with ID P0016
INSERT INTO products(id, name, category, price, quantity)
VALUES ('P0016', 'Candy', 'Others', 500, 1000);

-- Update price of product with ID P0016 to 1000
UPDATE products
SET price = 1000
WHERE id = 'P0016';

-- Add price constraint to ensure price is greater than or equal to 1000
ALTER TABLE products
    ADD CONSTRAINT price_check CHECK ( price >= 1000 );

-- Show create table statement for products
SHOW CREATE TABLE products;

-- Insert new product with ID P0017
INSERT INTO products(id, name, category, price, quantity)
VALUES ('P0017', 'Another Candy', 'Others', 500, 1000);

-- Update price of product with ID P0016 to 500
UPDATE products
SET price = 500
WHERE id = 'P0016';

-- Add fulltext index on name and description columns
ALTER TABLE products
    ADD FULLTEXT product_fulltext (name, description);

-- Show create table statement for products
SHOW CREATE TABLE products;

-- Retrieve products with "ayam" in name or description using LIKE operator
SELECT *
FROM products
WHERE name LIKE '%chicken%' OR description LIKE '%chicken%';

-- Retrieve products with "ayam" in name or description using MATCH AGAINST in NATURAL LANGUAGE MODE
SELECT *
FROM products
WHERE MATCH(name, description) AGAINST('chicken' IN NATURAL LANGUAGE MODE);

-- Retrieve products with "ayam" in name or description using MATCH AGAINST in BOOLEAN MODE
SELECT *
FROM products
WHERE MATCH(name, description) AGAINST('+chicken' IN BOOLEAN MODE);

-- Retrieve products with "bakso" in name or description using MATCH AGAINST with QUERY EXPANSION
SELECT *
FROM products
WHERE MATCH(name, description) AGAINST('meatball' WITH QUERY EXPANSION);

-- Describe the structure of the products table
DESC products;

-- Retrieve all products
SELECT *
FROM products;

-- Insert new product with ID P0018
INSERT INTO products(id, name, category, price, quantity)
VALUES ('Pxxxx', 'Example', 'Others', 1000, 1000);

-- Insert multiple new products
INSERT INTO products(id, name, price, quantity)
VALUES ('X0001', 'X One', 25000, 200),
       ('X0002', 'X Two', 10000, 300),
       ('X0003', 'X Three', 15000, 500);

-- Retrieve products with price greater than the average price
SELECT *
FROM products
WHERE price > (SELECT AVG(price) FROM products);

-- Retrieve the maximum price among all products
SELECT MAX(price)
FROM products;

-- Retrieve all products
SELECT *
FROM products;