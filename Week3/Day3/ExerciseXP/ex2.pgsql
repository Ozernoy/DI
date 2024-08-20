BEGIN;


/*
Use UPDATE to change the language of some films. 
Make sure that you use valid languages.
*/

UPDATE film
SET language_id = 2
WHERE film_id = 1;

SELECT film_id, language_id, title
FROM film
ORDER BY film_id
LIMIT 5;

/*
Which foreign keys (references) are defined for the customer table? 
How does this affect the way in which we INSERT into the customer table?
*/

/*
address_id and store_id
We can't add entries which do not have a corresponding entry in address and store fields

*/

/*
We created a new table called customer_review. Drop this table. 
Is this an easy step, or does it need extra checking?
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

-- Combined insertion with SELECT and VALUES
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
    LIMIT 3
) AS subquery

UNION ALL

SELECT 
    1 AS film_id,
    1 AS language_id,
    'Inception went WILD!' AS title,
    9 AS score,
    'Yeah, I didn''t expect that from Nolan''s new creation. It''s a mind-blowing blockbuster.' AS review_text,
    NOW() AS last_update;


DROP TABLE customer_review;


--SELECT * FROM customer_review; --relation "customer_review" does not exist
/* It was easy and did not required any extra checking
It could be restricted if we had any other table child to "customer review"
with foreign keys to it with RESTRICT ON DELETE

*/

/*
Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
*/

SELECT COUNT(*) FROM rental
WHERE return_date = NULL; --all rentals have been returned


/*
Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
*/

--No such movies?

/*
Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
*/

SELECT * FROM film_actor
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
LEFT JOIN film ON film_actor.film_id = film.film_id
WHERE first_name = 'Penelope' AND last_name = 'Monroe' AND description ILIKE '%sumo%'
;

/*
The 2nd film : A short documentary (less than 1 hour long), rated “R”.
*/

SELECT * FROM film
WHERE description ILIKE '%documentary%' AND length < 60 AND rating = 'R'
LIMIT 10;

/*
The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
*/

SELECT * FROM rental
LEFT JOIN customer ON rental.customer_id = customer.customer_id
LEFT JOIN payment ON rental.rental_id = payment.rental_id
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' AND payment.amount > 4 AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01'
LIMIT 10;

/*
The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
*/

SELECT * FROM rental
LEFT JOIN customer ON rental.customer_id = customer.customer_id
LEFT JOIN inventory ON rental.inventory_id = inventory.inventory_id
LEFT JOIN film ON inventory.film_id = film.film_id
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' AND (film.title ILIKE '%boat%' OR film.description ILIKE '%boat%')
ORDER BY film.replacement_cost DESC 
LIMIT 1;

ROLLBACK;