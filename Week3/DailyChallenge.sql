-- CREATE DATABASE Hollywood;


CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','08/10/1970', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('George','Clooney','06/05/1961', 2);

-- Add two more female actors one by one
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Meryl', 'Streep', '1949-06-22', 3);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Scarlett', 'Johansson', '1984-11-22', 0);

-- Add three more actors in one query
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES
('Leonardo', 'DiCaprio', '1974-11-11', 1),
('Tom', 'Hanks', '1956-07-09', 2),
('Jennifer', 'Lawrence', '1990-08-15', 1);

UPDATE actors SET age='1970-01-01' WHERE first_name='Matt' AND last_name='Damon';

-- Update the first name of Matt Damon to "Maty"
UPDATE actors
SET first_name = 'Maty'
WHERE first_name = 'Matt' AND last_name = 'Damon';

-- Update the number of oscars for George Clooney to 4, and return the updated record
UPDATE actors
SET number_oscars = 4
WHERE first_name = 'George' AND last_name = 'Clooney'
RETURNING *;

-- Rename the 'age' column to 'birthdate'
ALTER TABLE actors
RENAME COLUMN age TO birthdate;

-- Delete Leonardo DiCaprio and return the deleted record
DELETE FROM actors
WHERE first_name = 'Leonardo' AND last_name = 'DiCaprio'
RETURNING *;

-- Starting of DailyChallenge

/*
     | |
     | |
     | |
     | |
     | |
    \   /
     \ /
      v

*/

SELECT COUNT(*) AS total_actors FROM actors;

/*
INSERT INTO actors (first_name, last_name, birthdate, number_oscars)
VALUES ('Chris', 'Evans', '1981-06-13', NULL);

This code will raise an ERROR as when creating the table we've stated that all our columns NOT NULL

*/
