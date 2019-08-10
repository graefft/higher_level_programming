-- Script to list all genres from `hbtn_0d_tvshows` and display number of shows linked to each
-- List genres
SELECT tv_genres.name AS "genre",
       COUNT(tv_show_genres.genre_id) AS "number_of_shows"
	FROM tv_show_genres
LEFT JOIN tv_genres
ON tv_genres.id = genre_id
GROUP BY genre_id
ORDER BY number_of_shows DESC
