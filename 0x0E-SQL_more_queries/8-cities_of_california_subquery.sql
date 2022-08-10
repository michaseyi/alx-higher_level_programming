-- lists all city of California that cn be found in hbtn_0d_use
SELECT id, name
   FROM cities
   WHERE cities.state_id  IN (
      SELECT states.id
         FROM states
         WHERE states.name = 'California'
   )
   ORDER BY cities.id;