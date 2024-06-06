-- Creating a table named 'wallet' to store customer wallet information
CREATE TABLE wallet
(
    id          INT NOT NULL AUTO_INCREMENT, -- Unique identifier for each wallet record
    id_customer INT NOT NULL, -- Identifier of the associated customer
    balance     INT NOT NULL DEFAULT 0, -- Current balance in the wallet with a default of 0
    PRIMARY KEY (id), -- Defining primary key constraint on 'id' column
    UNIQUE KEY id_customer_unique (id_customer), -- Ensuring uniqueness of 'id_customer'
    FOREIGN KEY fk_wallet_customer (id_customer) REFERENCES customers (id) -- Creating a foreign key constraint referencing 'id' column in 'customers' table
) ENGINE = InnoDB; -- Specifying the storage engine for the table

-- Describing the structure of the 'wallet' table
DESCRIBE wallet;

-- Displaying all records from the 'customers' table
SELECT *
FROM customers;

-- Inserting records into the 'wallet' table for customers with IDs 1 and 3
INSERT INTO wallet(id_customer)
VALUES (1), -- Customer with ID 1
       (3); -- Customer with ID 3

-- Displaying all records from the 'wallet' table
SELECT *
FROM wallet;

-- Retrieving customer email and wallet balance by joining 'wallet' and 'customers' tables
SELECT customers.email, wallet.balance
FROM wallet
JOIN customers ON (wallet.id_customer = customers.id);
