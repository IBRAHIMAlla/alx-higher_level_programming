--  lists all shows without the genre Comedy in the database hbtn_0d_tvshows

SELECT t.title
FROM tv_shows t
WHERE t.title NOT IN (
      SELECT t.title
      FROM tv_shows t
      INNER JOIN tv_show_genres y ON m.id = y.show_id
      INNER JOIN tv_genres n ON y.genre_id = n.id
      WHERE n.name = 'Comedy'
)
ORDER BY n.title ASC;
