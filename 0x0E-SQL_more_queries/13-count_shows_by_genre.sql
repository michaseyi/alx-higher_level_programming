-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT g.name AS genre, COUNT(g.name) AS number_of_shows
   FROM tv_genres g JOIN tv_show_genres t
   ON t.genre_id = g.id
GROUP BY g.id
ORDER BY number_of_shows DESC;