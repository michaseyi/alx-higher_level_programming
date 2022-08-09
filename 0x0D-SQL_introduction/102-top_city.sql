-- displays top 3 cities temperature during July and August ordered by temperatures
SELECT city, avg(value) AS avg_temp FROM temperatures WHERE month
BETWEEN 7 AND 8 GROUP BY city  ORDER BY avg_temp DESC LIMIT 3;