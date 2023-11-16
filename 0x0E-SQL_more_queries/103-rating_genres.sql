-- lists all genres in the database hbtn_0d_tvshows_rate by their rating

SELECT tv_genres.name, SUM(tv_shows.rating) AS rating_sum
FROM tv_genres
JOIN tv_shows ON tv_genres.id = tv_shows.genre_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
