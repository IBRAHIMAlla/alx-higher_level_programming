-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

SELECT tv_g.name
FROM tv_genres g
WHERE tv_g.name NOT IN (
      SELECT tv_g.name
      FROM tv_genres tv_g
      INNER JOIN tv_show_genres y ON tv_g.id = y.genre_id
      INNER JOIN tv_shows m ON y.show_id = m.id
      WHERE m.title = 'Dexter'
)
ORDER BY tv_g.name ASC;
