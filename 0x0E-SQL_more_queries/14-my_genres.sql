-- lists all genres of the show "Dexter"

SELECT name 
   FROM tv_genres
   WHERE id IN (
      SELECT genre_id
         FROM tv_shows t
         JOIN tv_show_genres tg
         ON t.id = tg.show_id
      WHERE t.title = "Dexter"
   )
   ORDER BY name;