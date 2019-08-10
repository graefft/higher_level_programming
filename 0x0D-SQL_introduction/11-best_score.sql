-- Lists students with score >= 10
-- Ordered top to bottom
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC
