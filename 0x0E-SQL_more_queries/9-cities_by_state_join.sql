-- This script lists all cities contained in the database hbtn_0d_usa
-- return the id, name of cities joined with state
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
