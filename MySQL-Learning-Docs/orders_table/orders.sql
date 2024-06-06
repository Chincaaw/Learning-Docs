-- Creating table 'orders' to store order information
CREATE TABLE orders
(
    id         INT      NOT NULL AUTO_INCREMENT, -- Unique identifier for each order
    total      INT      NOT NULL,                -- Total amount of the order
    order_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order is placed
    PRIMARY KEY (id)                            -- Defining 'id' as the primary key
) ENGINE = InnoDB;

-- Describing the structure of table 'orders'
DESCRIBE orders;

-- Creating table 'orders_detail' to store detailed information about each order
CREATE TABLE orders_detail
(
    id_product VARCHAR(10) NOT NULL,  -- Identifier for the product
    id_order   INT         NOT NULL,  -- Identifier for the order
    price      INT         NOT NULL,  -- Price of the product
    quantity   INT         NOT NULL,  -- Quantity of the product ordered
    PRIMARY KEY (id_product, id_order) -- Defining composite primary key using 'id_product' and 'id_order'
) ENGINE = InnoDB;

-- Describing the structure of table 'orders_detail'
DESCRIBE orders_detail;

-- Adding foreign key constraint to enforce referential integrity with table 'products'
ALTER TABLE orders_detail
    ADD CONSTRAINT fk_orders_detail_product
        FOREIGN KEY (id_product) REFERENCES products (id);

-- Adding foreign key constraint to enforce referential integrity with table 'orders'
ALTER TABLE orders_detail
    ADD CONSTRAINT fk_orders_detail_orders
        FOREIGN KEY (id_order) REFERENCES orders (id);

-- Showing the SQL statement used to create table 'orders_detail'
SHOW CREATE TABLE orders_detail;

-- Querying all records from table 'orders'
SELECT *
FROM orders;

-- Inserting a new record into table 'orders'
INSERT INTO orders(total)
VALUES (75000); -- Changed value for demonstration

-- Inserting records into table 'orders_detail' for the newly inserted order
INSERT INTO orders_detail(id_product, id_order, price, quantity)
VALUES ('P0005', 4, 30000, 2), -- Changed values for demonstration
       ('P0006', 4, 45000, 1); -- Changed values for demonstration

-- Querying all records from table 'orders_detail'
SELECT *
FROM orders_detail;

-- Querying order details along with product information
SELECT *
FROM orders
         JOIN orders_detail ON (orders_detail.id_order = orders.id)
         JOIN products ON (products.id = orders_detail.id_product);

-- Querying specific order details along with product information
SELECT orders.id, products.id, products.name, orders_detail.quantity, orders_detail.price
FROM orders
         JOIN orders_detail ON (orders_detail.id_order = orders.id)
         JOIN products ON (products.id = orders_detail.id_product);
