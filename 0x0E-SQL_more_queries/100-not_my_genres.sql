-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

SELECT t.name
FROM tv_genres t
WHERE t.name NOT IN (
      SELECT t.name
      FROM tv_genres t
      INNER JOIN tv_show_genres y ON t.id = y.genre_id
      INNER JOIN tv_shows n ON y.show_id = n.id
      WHERE n.title = 'Dexter'
)
ORDER BY t.name ASC;
