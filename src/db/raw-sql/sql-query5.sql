SELECT
(
	SELECT
	COUNT(*)-1
	FROM operations
	GROUP BY operator, number1, number2
	HAVING COUNT(*) > 1
) as "duplicated_count",
(
	SELECT COUNT(*)
	FROM operations
	GROUP BY operator, number1, number2
	HAVING COUNT (*) = 1
) as "unique_count"
FROM operations
GROUP BY duplicated_count, unique_count;