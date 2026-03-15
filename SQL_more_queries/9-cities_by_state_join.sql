-- List all cities with their corresponding state name using INNER JOIN
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id  -- match each city to its state
ORDER BY cities.id ASC;                            -- sort results by city id in ascending order