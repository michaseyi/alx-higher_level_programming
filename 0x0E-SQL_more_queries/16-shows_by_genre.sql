-- lists all shows, and all genres linked to that show

SELECT t.title AS title, g.name AS name
   FROM tv_shows t
   LEFT JOIN 
      (tv_show_genres tg
      JOIN tv_genres g
      ON tg.genre_id = g.id)
   ON t.id = tg.show_id
   ORDER BY t.title, g.name;