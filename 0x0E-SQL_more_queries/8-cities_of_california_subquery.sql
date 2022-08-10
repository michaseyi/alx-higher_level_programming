-- lists all city of California that cn be found in hbtn_0d_use
SELECT id, name
   FROM cities
   WHERE state_id = (
      SELECT id
         FROM state
         WHERE name = 'California';
   )
   ORDER BY id;