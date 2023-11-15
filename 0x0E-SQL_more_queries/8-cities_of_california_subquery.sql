--  a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id, cities.name
FROM cities, (SELECT id FROM states WHERE name = 'California') AS california_states
WHERE cities.state_id = california_states.id
ORDER BY cities.id ASC;
