-- Create a table named 'customers' with columns for customer details
DROP TABLE customers;

CREATE TABLE customers
(
    id         INT          NOT NULL AUTO_INCREMENT,  -- Unique ID for each customer, automatically incremented
    email      VARCHAR(100) NOT NULL,                 -- Customer's email address, cannot be null
    first_name VARCHAR(100) NOT NULL,                 -- Customer's first name, cannot be null
    last_name  VARCHAR(100),                          -- Customer's last name, can be null
    PRIMARY KEY (id),                                 -- Define 'id' as the primary key
    UNIQUE KEY email_unique (email)                   -- Ensure emails are unique
) ENGINE = InnoDB;

-- Describe the structure of the 'customers' table
DESCRIBE customers;

-- Drop the existing unique constraint on the 'email' column
ALTER TABLE customers
DROP CONSTRAINT email_unique;

-- Add a new unique constraint on the 'email' column
ALTER TABLE customers
ADD CONSTRAINT email_unique UNIQUE (email);

-- Insert a new record into the 'customers' table
INSERT INTO customers(email, first_name, last_name)
VALUES ('eko@gmail.com', 'Eko', 'Kurniawan');

-- Retrieve all records from the 'customers' table
SELECT * FROM customers;

-- Insert another record into the 'customers' table
INSERT INTO customers(email, first_name, last_name)
VALUES ('kurniawan@gmail.com', 'Eko', 'Kurniawan');

-- Describe the structure of the 'customers' table after modifications
DESC customers;
