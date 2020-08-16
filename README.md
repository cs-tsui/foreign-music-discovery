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