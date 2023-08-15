-- displays the average temperature (Fahrenheit) by city
SELECT city, ROUND(AVG(value), 4) AS avg_temp
	FROM temperatures
	WHERE month = 7 OR month = 8
        GROUP BY city
        ORDER BY avg_temp DESC
        LIMIT 3;
