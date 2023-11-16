-- lists all genres in the database hbtn_0d_tvshows_rate 

SELECT tv_genres.name, SUM(rating) AS rating_sum FROM tv_genres
JOIN tv_shows ON tv_genres.id = tv_shows.genre_id
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
