-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows

SELECT title
   FROM tv_shows
   WHERE title NOT IN (
      SELECT t.title
         FROM tv_shows t
         JOIN tv_show_genres tg
         ON t.id = tg.show_id
         JOIN tv_genres g
         ON tg.genre_id = g.id
         WHERE g.name = "Comedy")
   ORDER BY title;