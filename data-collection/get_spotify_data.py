#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

# IDs of playlists
# TODO: automate gathering playlists in the first place
playlists = [
    {
        'lang': 'Chinese',
        'id': '0eoEJg0k4tV0Jw3gmTfRko',
        'playlist_name': 'The Sound of Chinese Hip Hop'
    },
    {
        'lang': 'Chinese',
        'id': '0AdCrGQY3vhJvKNUWeQGQy',
        'playlist_name': 'The Sound of Hong Kong Hip Hop'
    },    
    {
        'lang': 'Korean',
        'id': '1x5KJwBNPIy3bYltlNaNDK',
        'playlist_name': 'The Sound of Korean Trap'
    },
    {
        'lang': 'Korean',
        'id': '0thomPcNswX7vGOyBvHxMQ',
        'playlist_name': 'The Sound of K-Rap'
    },
    {
        'lang': 'Israeli',
        'id': '3zE5pYwFbC6sSjMRjvhePx',
        'playlist_name': 'The Sound of Israeli Trap'
    },
    {
        'lang': 'Romanian',
        'id': '5xxIhwNhCZlkyFKpA8hxRj',
        'playlist_name': 'The Sound of Romanian Hip Hop'
    },
    {
        'lang': 'Thai',
        'id': '0ic1I4rWzKchFqKE1HOWWH',
        'playlist_name': 'The Sound of Thai Hip Hop'
    },
    {
        'lang': 'Arabic',
        'id': '7zBydkoj9qpNmelxR9goHB',
        'playlist_name': 'The Sound of Arabic Hip Hop'
    },
    {
        'lang': 'Norwegian',
        'id': '1NJP3X0lK6XyEeKlI7m8Fb',
        'playlist_name': 'The Sound of Norwegian Hip Hop'
    },
    {
        'lang': 'Norwegian',
        'id': '4TaUNytRspBtacAOATKvF3',
        'playlist_name': 'The Sound of Norwegian Pop Rap'
    },
    {
        'lang': 'Turkish',
        'id': '4t5PSWEsLQeZ4i90PEpW9i',
        'playlist_name': 'The Sound of Turkish Hip Hop'
    },
    {
        'lang': 'Polish',
        'id': '78dAycV2sXjUhhhCrmgalT',
        'playlist_name': 'The Sound of Polish Trap'
    },
    
    {
        'lang': 'German',
        'id': '0N2gkh3nggtCtksCU2cSty',
        'playlist_name': 'The Sound of German Hip Hop'
        
    },
    {
        'lang': 'French',
        'id': '1Wc17kLi2R2EsIACx5ElYt',
        'playlist_name': 'The Sound of French Hip Hop'
        
    },
    {
        'lang': 'Russian',
        'id': '2NweJbjBo0jbtRgYOalUDO',
        'playlist_name': 'The Sound of Russian Trap'
        
    },
    
    {
        'lang': 'Russian',
        'id': '69d6UEZKkFtQNEDQyntv7S',
        'playlist_name': 'The Sound of Russian Hip Hop'
        
    },
    
    
    {
        'lang': 'Indonesian',
        'id': '0x3CJjEE1PFDkzRtjxbrwq',
        'playlist_name': 'The Sound of Indonesian Hip Hop'
        
    },
    {
        'lang': 'Greek',
        'id': '0NcAnGFICl7Oj202HLzPpf',
        'playlist_name': 'The Sound of Greek Hip Hop'
        
    },
    
    {
        'lang': 'Greek',
        'id': '38cq1JOTwmZbNcv3SwXuoa',
        'playlist_name': 'The Sound of Greek Trap'
        
    },
    {
        'lang': 'English',
        'id': '6MXkE0uYF4XwU4VTtyrpfP',
        'playlist_name': 'The Sound of Hip Hop'
    }
]

# Hold all tracks
all_tracks = []

# Fetch all songs from each playlist and push 
# to all_tracks array
for pl in playlists:
    print(pl['playlist_name'])
    results = sp.playlist_tracks(pl['id'])
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    for t in tracks:
        if t is None:
            print("t is none")
            continue
        if 'track' not in t:
            print('track key not in t')
            print(len(t))
            continue
        t['track']['lang'] = pl['lang']
        all_tracks.append(t['track'])
    print(len(tracks))
    print("Done")

print("number of tracks: ", len(all_tracks))
print("number of playlists: ", len(playlists) )

# Generate n size chunks to be used when 
# calling Spotify API
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

all_chunks = chunks(all_tracks, 100)

# Get audio features for chunked up all_tracks
for chunk in all_chunks:
    track_ids = [track['id'] for track in chunk]
    chunk_afs = sp.audio_features(tracks=track_ids)
    
    for track, audio_feature in zip(chunk, chunk_afs):
        track['audio_features'] = audio_feature
    
    print('chunk fetched')

# Flatten tracks dictionary since audio_features are nested currently
keys_to_keep = ['id', 'name', 'popularity', 'uri', 'lang', 'duration_ms',
                    'time_signature', 'danceability', 'energy', 'key', 'loudness',
                        'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness',
                            'valence', 'tempo', 'track_href', 'analysis_url']

cleaned_tracks = []
for track in all_tracks:
    track.update(track['audio_features'])
    new_track = {k: track[k] for k in keys_to_keep}
    new_track['artist'] = track['artists'][0]['name']
    cleaned_tracks.append(new_track)

print(len(cleaned_tracks))

# Create dataframe for ease of saving to CSV
# TODO: save to database in the future
mydf = pd.DataFrame(cleaned_tracks)
mydf.to_csv('multilang_playlist.csv')