# Summary
Discover music in other languages.


## Run

For running the data collection script, ensure Spotify client credentials are available as environment variables.

```
export SPOTIPY_CLIENT_ID = <client_id>
export SPOTIPY_CLIENT_SECRET = <client_secret>
python data-collection/get_spotify_data.py
```


Running the `get_spotify_data.py` script will generate a csv file `multilang_playlist.csv` with songs from the defined playlists in the script.


# Discover Foreign Music
Music streaming services such as Spotify, YouTube and many others have long had recommendation systems to suggest similar music to a user’s taste. However, one of these providers have an out-of-the-box feature where it is possible to provide recommendations of songs in languages different than a user’s profile setting, or different than the language of the songs the user is currently playing or has played recently.

This project uses clustering methods to recommend hip-hop music in other languages to a user. Within the hip-hop genre, there are still numerous styles that may not appeal to everyone. Utilizing clustering techniques, we aim to group together hip-hop tracks with similar audio features. With a combined dataset consisting of tracks of many different languages, we aim to generate a list of songs based on a user provided seed track that allows the user to discover music in languages different from their own
