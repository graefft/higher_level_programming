-- Displays max temperature of each state
-- Ordered by state name
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state;
