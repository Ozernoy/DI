/*
EXERCISE 1

We will work on the public database that we created yesterday.

Use SQL to get the following from the database:

1) All items, ordered by price (lowest to highest).

2) Items with a price above 80 (80 included), 
ordered by price (highest to lowest).

3) The first 3 customers in alphabetical order 
of the first name (A-Z) – exclude the primary key 
column from the results.

4) All last names (no other columns!),
in reverse alphabetical order (Z-A)
*/


SELECT * FROM items
ORDER BY price ASC;

SELECT * FROM items
WHERE price >= 80
ORDER BY price DESC;

SELECT first_name, last_name FROM customers
ORDER BY first_name ASC
LIMIT 3;

SELECT last_name FROM customers
ORDER BY last_name DESC;







