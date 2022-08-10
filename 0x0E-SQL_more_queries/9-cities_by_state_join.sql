-- lists all cities contained in the database hbtn_0d_usa

SELECT cities.id AS id, cities.name AS name, states.name AS name 
   FROM states
   JOIN cities
   ON states.id = cities.state_id
   ORDER BY cities.id;