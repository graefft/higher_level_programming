-- Lists number of records with same score in `second_table`
-- Displays score and number of records with this score sorted descending
SELECT score, COUNT(score) AS "number"
FROM second_table
GROUP BY score
ORDER BY number DESC;
