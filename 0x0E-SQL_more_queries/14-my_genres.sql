-- Import the database dump from hbtn_0d_tvshows to your MySQL server

SELECT genres.name
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY genres.name ASC;
