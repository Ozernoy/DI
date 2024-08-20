BEGIN;

-- Part I: Customer and Customer Profile Tables

-- Create Customer table
CREATE TABLE Customer (
    id SERIAL PRIMARY KEY,  -- Primary key auto-incremented
    first_name VARCHAR(50) NOT NULL,  -- First name cannot be NULL
    last_name VARCHAR(50) NOT NULL  -- Last name cannot be NULL
);

-- Create CustomerProfile table with a reference to Customer
CREATE TABLE CustomerProfile (
    id SERIAL PRIMARY KEY,  -- Primary key auto-incremented
    isLoggedIn BOOLEAN DEFAULT FALSE,  -- Default value is FALSE
    customer_id INTEGER UNIQUE REFERENCES Customer(id)  -- One-to-one relationship with Customer
);

-- Insert customers into the Customer table
INSERT INTO Customer (first_name, last_name) VALUES
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');

-- Insert customer profiles using subqueries
INSERT INTO CustomerProfile (isLoggedIn, customer_id)
VALUES 
(TRUE, (SELECT id FROM Customer WHERE first_name = 'John' AND last_name = 'Doe')),
(FALSE, (SELECT id FROM Customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'));

-- Query to display the first name of the LoggedIn customers
SELECT c.first_name
FROM Customer c
JOIN CustomerProfile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = TRUE;

-- Query to display all customers' first name and isLoggedIn status, including those without a profile
SELECT 
    c.first_name, 
    CASE 
        WHEN cp.isLoggedIn IS NULL THEN FALSE --Just to have False instead of NULL inside our data
        ELSE cp.isLoggedIn
    END AS isLoggedIn
FROM Customer c
LEFT JOIN CustomerProfile cp ON c.id = cp.customer_id;

-- Query to count the number of customers that are not LoggedIn
SELECT COUNT(*)
FROM CustomerProfile
WHERE isLoggedIn = FALSE;

-- Part II: Book, Student, and Library Tables

-- Create Book table
CREATE TABLE Book (
    book_id SERIAL PRIMARY KEY,  -- Primary key auto-incremented
    title VARCHAR(100) NOT NULL,  -- Title cannot be NULL
    author VARCHAR(100) NOT NULL  -- Author cannot be NULL
);

-- Insert books into the Book table
INSERT INTO Book (title, author) VALUES
('Alice In Wonderland', 'Lewis Carroll'),
('Harry Potter', 'J.K Rowling'),
('To kill a mockingbird', 'Harper Lee');

-- Create Student table with a CHECK constraint to ensure age is <= 15
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,  -- Primary key auto-incremented
    name VARCHAR(50) NOT NULL UNIQUE,  -- Name cannot be NULL and must be unique
    age INTEGER CHECK (age <= 15)  -- Age cannot be greater than 15
);

-- Insert students into the Student table
INSERT INTO Student (name, age) VALUES
('John', 12),
('Lera', 11),
('Patrick', 10),
('Bob', 14);

-- Create Library (junction) table for Many-to-Many relationship between Book and Student
CREATE TABLE Library (
    book_fk_id INTEGER REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,  -- Foreign key with cascading delete and update
    student_fk_id INTEGER REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,  -- Foreign key with cascading delete and update
    borrowed_date DATE,  -- Date the book was borrowed
    PRIMARY KEY (book_fk_id, student_fk_id)  -- Composite primary key
);

-- Insert records into Library table using subqueries
INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES 
((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'John'), '2022-02-15'),
((SELECT book_id FROM Book WHERE title = 'To kill a mockingbird'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-03-03'),
((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'Lera'), '2021-05-23'),
((SELECT book_id FROM Book WHERE title = 'Harry Potter'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-08-12');

-- Query to select all columns from the Library table
SELECT * FROM Library;

-- Query to select the name of the student and the title of the borrowed books
SELECT s.name, b.title
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id;

-- Query to select the average age of the children who borrowed "Alice In Wonderland"
SELECT AVG(s.age) AS average_age
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland';

-- Delete a student named 'Bob' and observe the cascading effect
DELETE FROM Student WHERE name = 'Bob';

-- Check the remaining records in the Library table after the deletion
SELECT * FROM Library;



ROLLBACK;