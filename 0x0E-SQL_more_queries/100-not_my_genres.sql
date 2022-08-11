-- list all genres not linked to the show Dexter

SELECT name
   FROM tv_genres
   WHERE name NOT IN (
      SELECT g.name
         FROM tv_shows t
         JOIN tv_show_genres tg
         ON t.id = tg.show_id
         JOIN tv_genres g
         ON tg.genre_id = g.id
         WHERE t.title = "Dexter")
   ORDER BY name;