BEGIN;

/*
Get a list of all the languages, from the language table.
*/



SELECT name FROM language;

/*
Get a list of all films joined with their languages – 
select the following details : film title, description, and language name.
*/

SELECT title, description, language.name FROM film
LEFT JOIN language ON film.language_id = language.language_id
LIMIT 10;

/*
Get all languages, even if there are no films in those 
languages – select the following details : film title, 
description, and language name.
*/

SELECT DISTINCT language.name FROM film
LEFT JOIN language ON film.language_id = language.language_id; --Returns only "English"

--? I do not understand the task


/*
Create a new table called new_film with the following columns : 
id, name. Add some new films to the table.
*/


CREATE TABLE new_film(
    new_film_id SERIAL PRIMARY KEY,
    name VARCHAR (50) NOT NULL
);
INSERT INTO new_film (name) VALUES
('Inception'),
('The Dark Knight'),
('Interstellar'),
('Pulp Fiction'),
('The Matrix'),
('The Godfather'),
('Forrest Gump'),
('The Shawshank Redemption'),
('Fight Club'),
('The Lord of the Rings: The Return of the King');

SELECT * FROM new_film;


/*
Create a new table called customer_review,
 which will contain film reviews that customers will make.
Think about the DELETE constraint: 
if a film is deleted, its review should be automatically deleted.
It should have the following columns:
review_id – a primary key, non null, auto-increment.
film_id – references the new_film table. 
The film that is being reviewed.
language_id – references the language table. 
What language the review is in.
title – the title of the review.
score – the rating of the review (1-10).
review_text – the text of the review. No limit on the length.
last_update – when the review was last updated.
*/


CREATE TABLE customer_review(
    review_id SERIAL PRIMARY KEY,
    film_id INTEGER NOT NULL REFERENCES film(film_id) ON DELETE CASCADE,
    language_id INTEGER REFERENCES language(language_id) NOT NULL,
    title VARCHAR(50) NOT NULL,
    score SMALLINT NOT NULL,
    review_text TEXT NOT NULL,
    last_update DATE NOT NULL
);


/*
Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
*/

--Let's look which movies worth writing a review
SELECT title, film_id, language_id FROM film
WHERE rating = 'NC-17'
ORDER BY rental_duration DESC
LIMIT 3;

--Now, let's add reviews
INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
SELECT 
    film_id,
    language_id,
    title,
    CASE 
        WHEN title = 'Adaptation Holes' THEN 9
        WHEN title = 'Chamber Italian' THEN 7
        WHEN title = 'Anonymous Human' THEN 8
    END AS score,
    CASE 
        WHEN title = 'Adaptation Holes' THEN 'Excellent movie!'
        WHEN title = 'Chamber Italian' THEN 'Good but could be better.'
        WHEN title = 'Anonymous Human' THEN 'Quite enjoyable.'
    END AS review_text,
    NOW()
FROM (
    SELECT title, film_id, language_id FROM film
    WHERE rating = 'NC-17'
    ORDER BY rental_duration DESC
    LIMIT 3);

SELECT * FROM customer_review;


/*
Delete a film that has a review from the new_film table, what happens to the customer_review table?
*/

--Let's first add a review to film from this table
INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update) VALUES
(
    1,
    1,
    'Inception went WILD!',
    9,
    'Yeah, I didn''t expect that from Nolan''s new creation. It''s a mind-blowing blockbuster.',
    NOW()
);

SELECT * FROM customer_review;

--Because of having the same ID's in film and in new_film we have THE SITUATION
SELECT title FROM film
WHERE film_id = 1; --Returns Academy Dinosaur
--But handling it is not the current task, so let's proceed

/*
DELETE FROM film
    WHERE film_id = 1;
*/

--The output is
/*
ERROR: update or delete on table "film" violates foreign key constraint 
"film_actor_film_id_fkey" on table "film_actor"
*/
--It'so because of ON DELETE RESTRICT in table film_actor

ROLLBACK;