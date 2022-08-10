-- list all comedy shows

SELECT t.title AS title
   FROM tv_shows t
   JOIN tv_show_genres tg
   ON t.id = tg.show_id
   JOIN tv_genres g
   ON tg.genre_id = g.id
   WHERE g.name = "Comedy"
   ORDER BY t.title;