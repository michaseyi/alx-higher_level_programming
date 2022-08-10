-- lists all showw contained in the database hbtn_0d_tvshows

SELECT t.title AS title, g.genre_id AS genre_id
   FROM tv_shows t
   LEFT JOIN tv_show_genres g
   ON t.id = g.show_id
   WHERE g.show_id is NULL
   ORDER BY t.title, g.genre_id;
