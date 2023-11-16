--  lists all shows without the genre Comedy in the database hbtn_0d_tvshows

SELECT v.title
FROM tv_shows v
WHERE v.title NOT IN (
      SELECT v.title
      FROM tv_shows v
      INNER JOIN tv_show_genres y ON v.id = y.show_id
      INNER JOIN tv_genres r ON y.genre_id = r.id
      WHERE r.name = 'Comedy'
)
ORDER BY v.title ASC
