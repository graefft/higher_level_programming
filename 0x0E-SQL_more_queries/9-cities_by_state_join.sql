-- Script that lists all cities contained in `hbtn_0d_usa`
-- List cities by `cities.id`
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states
ON states.id = cities.state_id
ORDER BY cities.id;
