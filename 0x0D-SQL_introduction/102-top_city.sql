-- a script that displays the top 3 cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS average_temp FROM temperatures WHERE month IN (7, 8) GROUP BY city ORDER BY average_temp DESC LIMIT 3;
