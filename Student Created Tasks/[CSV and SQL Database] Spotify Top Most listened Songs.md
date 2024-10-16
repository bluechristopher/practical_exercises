# Task 1

You are working as a data engineer for a music analytics company that tracks and analyzes the performance of top songs on various streaming platforms. The company has provided you with a CSV file, Spotify Most Streamed Songs.csv, which contains data about the most streamed songs on Spotify and other music platforms. The company needs to process this data, store it in a structured database, and extract insights through SQL queries to support the analytics team in understanding trends related to song performance, artist popularity, and other key metrics.

You are tasked with analyzing and storing the data from the CSV file. The file contains the following columns related to song metadata:

- track_name: track name of the song
- artist(s)_name: name of the artist(s) of the song
- artist_count: number of artists involved in the song
- released_year: year the song was released
- released_month: month the song was released
- released_day: day the song was released
- in_spotify_playlists: number of playlists the song is in on Spotify
- in_spotify_charts: number of charts the song is in on Spotify
- streams: number of streams the song has
- in_apple_playlists: number of playlists the song is in on Apple Music
- in_apple_charts: number of charts the song is in on Apple Music
- in_deezer_playlists: number of playlists the song is in on Deezer
- in_deezer_charts: number of charts the song is in on Deezer
- in_shazam_charts: number of charts the song is in on Shazam
- bpm: beats per minute of the song
- key: key of the song
- mode: mode of the song
- danceability_%: danceability percentage of the song
- valence_%: valence percentage of the song
- energy_%: energy percentage of the song
- acousticness_%: acousticness percentage of the song
- instrumentalness_%: instrumentalness percentage of the song
- liveness_%: liveness percentage of the song
- speechiness_%: speechiness percentage of the song
- cover_url: URL of the cover image of the song

An example row from the CSV file looks like this:

`LALA, Myke Towers, 1, 2023, 3, 23, 1474, 48, 133716286, 48, 126, 58, 14, 382, 92, C#, Major, 71, 61, 74, 7, 0, 10, 4, https://i.scdn.co/image/ab67616d0000b2730656d5ce813ca3cc4b677e05`

## Task 1.1

Write a Python script that reads and processes the data from the provided CSV file. Filter out any songs that do not have a valid cover URL (i.e., songs where the cover_url is listed as “Not Found”). For each valid song, extract and store the following columns into a 2-dimensional list called spotify_streams:

- track_name
- artist(s)_name
- released_year
- released_month
- released_day
- cover_url

After processing, print the first 5 rows of the spotify_streams list to verify the results.

## Task 1.2

Create a database called Spotify.db. In this database, create a table called songs to store all the data from the spotify_streams list, excluding the artist(s)_name column.

## Task 1.3

Create a list called artists_list, which contains each artist name from the artist(s)_name column of the CSV file, ensuring that each artist is only included once. Then, create a table called artists in the Spotify.db database to store these artist names.

## Task 1.4

Create a junction table called SongArtist to store the relationship between the songs and their respective artists. This table will serve as a bridge between the songs and artists tables.

## Task 1.5

Insert the data from the spotify_streams list into the songs table, the data from the artists_list into the artists table, and the data into the SongArtist junction table, representing the relationships between the songs and their artists.

## Task 1.6

Write the following SQL queries and output the results:

1. Query all songs that were released in the year 2013.
2. Query the artist(s) with the most number of songs in the songs table.
3. Query the songs with the highest number of streams, sorting the results in descending order.

## Task 1.7

Write an SQL query to retrieve the track_name, streams, and artist_name for all songs by the artist “Olivia Rodrigo,” and output the results.

## Task 1.8

Write an SQL query to retrieve the artist_name and the songs in which the artist “Taylor Swift” has appeared in the “Spotify Most Streamed Songs” data, and output the results.
