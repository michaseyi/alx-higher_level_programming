-- lists all shows contained in hbtn_0d_tvshows that have at lease one genre linked
SELECT t.title AS title, g.genre_id AS genre_id
   FROM tv_shows t
      JOIN tv_show_genres g
      ON t.id = g.show_id
   ORDER BY t.title, g.genre_id;