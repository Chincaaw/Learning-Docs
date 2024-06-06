-- Create a table to store guestbook entries
CREATE TABLE guestbooks
(
    id      INT NOT NULL AUTO_INCREMENT, -- Unique identifier for each entry
    email   VARCHAR(100), -- Email of the guestbook author
    title   VARCHAR(200), -- Title of the entry
    content TEXT, -- Content of the entry
    PRIMARY KEY (id) -- Primary key constraint
) ENGINE = InnoDB;

-- Display all records from the customers table
SELECT *
FROM users;

-- Insert sample data into the guestbooks table
INSERT INTO guestbooks(email, title, content)
VALUES ('guest@gmail.com', 'Greetings', 'Hello'),
       ('guest2@gmail.com', 'Greetings', 'Hello'),
       ('guest3@gmail.com', 'Greetings', 'Hello'),
       ('eko@gmail.com', 'Greetings', 'Hello'),
       ('eko@gmail.com', 'Greetings', 'Hello'),
       ('eko@gmail.com', 'Greetings', 'Hello');

-- Display all records from the guestbooks table
SELECT *
FROM guestbooks;

-- Retrieve unique emails from both customers and guestbooks tables
SELECT email
FROM users
UNION
SELECT email
FROM guestbooks;

-- Retrieve all emails, including duplicates, from both customers and guestbooks tables
SELECT email
FROM users
UNION ALL
SELECT email
FROM guestbooks;

-- Count the occurrences of each email from both tables combined
SELECT emails.email, COUNT(emails.email)
FROM (SELECT email
      FROM users
      UNION ALL
      SELECT email
      FROM guestbooks) as emails
GROUP BY emails.email;

-- Retrieve distinct emails from customers who have also signed the guestbook
SELECT DISTINCT email
FROM users
WHERE email IN (SELECT DISTINCT email FROM guestbooks);

-- Retrieve distinct emails from customers who have also signed the guestbook using INNER JOIN
SELECT DISTINCT users.email
FROM users
         INNER JOIN guestbooks ON (guestbooks.email = users.email);

-- Retrieve distinct emails from customers who haven't signed the guestbook using LEFT JOIN
SELECT DISTINCT users.email, guestbooks.email
FROM users
         LEFT JOIN guestbooks ON (users.email = guestbooks.email)
WHERE guestbooks.email IS NULL;
