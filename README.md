## Summary
Discover music in other languages.

Music streaming services such as Spotify, YouTube and many others have long had recommendation systems to suggest similar music to a user’s taste. However, none of these providers have an out-of-the-box feature where it is possible to provide recommendations of songs in languages different than a user’s profile setting, or different than the language of the songs the user is currently playing or has played recently.

This project collects various playlists from Spotify to generate a list of hip-hop tracks in various languages, and uses clustering methods to recommend hip-hop music in other languages to a user. Within the hip-hop genre, there are still numerous styles that may not appeal to everyone.


## Run

For running the data collection script, ensure Spotify client credentials are available as environment variables.

```
export SPOTIPY_CLIENT_ID = <client_id>
export SPOTIPY_CLIENT_SECRET = <client_secret>
python data-collection/get_spotify_data.py
```

Running the `get_spotify_data.py` script will generate a csv file `multilang_playlist.csv` with songs from the defined playlists in the script.
