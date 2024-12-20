-- CREATE DATABASE bootcamp;

/*
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL
);

INSERT INTO students (first_name, last_name, birth_date) VALUES
('Marc', 'Benichou', '1998-11-02'),
('Yoan', 'Cohen', '2010-12-03'),
('Lea', 'Benichou', '1987-07-27'),
('Amelia', 'Dux', '1996-04-07'),
('David', 'Grez', '2003-06-14'),
('Omer', 'Simpson', '1980-10-03');

INSERT INTO students (first_name, last_name, birth_date) VALUES
('Danila', 'Ozernoy', '1999-11-14');

-- Fetch all of the data from the students table
SELECT * FROM students;

-- Fetch all students' first names and last names
SELECT first_name, last_name FROM students;

-- Fetch the student whose id is equal to 2
SELECT first_name, last_name FROM students WHERE id = 2;

-- Fetch the student whose last name is 'Benichou' AND first name is 'Marc'
SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc';

-- Fetch the students whose last names are 'Benichou' OR first names are 'Marc'
SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc';

-- Fetch the students whose first names contain the letter 'a'
SELECT first_name, last_name FROM students WHERE first_name ILIKE '%a%';

-- Fetch the students whose first names start with the letter 'a'
SELECT first_name, last_name FROM students WHERE first_name ILIKE 'a%';

-- Fetch the students whose first names end with the letter 'a'
SELECT first_name, last_name FROM students WHERE first_name ILIKE '%a';

-- Fetch the students whose second to last letter of their first names is 'a'
SELECT first_name, last_name FROM students WHERE first_name ILIKE '%a_';

-- Fetch the students whose ids are equal to 1 AND 3
SELECT first_name, last_name FROM students WHERE id IN (1, 3);

-- Fetch the students whose birth dates are equal to or come after 01/01/2000
SELECT * FROM students WHERE birth_date >= '2000-01-01';
*/

