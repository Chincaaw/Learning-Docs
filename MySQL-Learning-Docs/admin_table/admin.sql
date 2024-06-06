-- Create table to store admin data
DROP TABLE admin;

CREATE TABLE admin
(
    id         INT          NOT NULL AUTO_INCREMENT, -- Unique identifier for each admin
    first_name VARCHAR(100) NOT NULL, -- First name of the admin
    last_name  VARCHAR(100) NOT NULL, -- Last name of the admin
    PRIMARY KEY (id) -- Define primary key constraint on id column
) ENGINE = InnoDB; -- Use InnoDB engine for table

-- Describe the structure of the admin table
DESCRIBE admin;

-- Insert initial data of admins
INSERT INTO admin(first_name, last_name)
VALUES ('Harry', 'Potter'), -- Inserting Harry Potter as an admin
       ('Hermione', 'Granger'), -- Inserting Hermione Granger as an admin
       ('Ron', 'Weasley'); -- Inserting Ron Weasley as an admin

-- Retrieve all admins from the admin table and display them in ascending order of their IDs
SELECT * FROM admin ORDER BY id;

-- Delete admin with ID 3 (which is Ron Weasley)
DELETE FROM admin WHERE id = 3;

-- Insert new admin data
INSERT INTO admin(first_name, last_name)
VALUES ('Albus', 'Dumbledore'); -- Inserting Albus Dumbledore as a new admin

-- Retrieve the ID of the last inserted admin
SELECT LAST_INSERT_ID();