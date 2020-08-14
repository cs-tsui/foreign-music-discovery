#!/usr/bin/env python
# coding: utf-8

# In[23]:


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


# In[24]:



# IDs of playlists

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
#     {
#         'lang': 'English',
#         'id': '37i9dQZF1DX0XUsuxWHRQd',
#         'playlist_name': 'RapCaviar'
#     },
    {
        'lang': 'English',
        'id': '6MXkE0uYF4XwU4VTtyrpfP',
        'playlist_name': 'The Sound of Hip Hop'
    }
]
# playlists = playlists[4:5]

# playlist_ids = [sound_of_chinese_hip_hop,sound_of_ktrap,sound_of_thai_hip_hop]
all_tracks = []

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


# In[25]:


print("number of tracks", len(all_tracks))

# all_tracks[-2]['name']
# all_tracks[]

print("number of playlists:", len(playlists) )


# In[4]:


all_tracks[0]


# In[26]:


id1 = all_tracks[0]['id']
# aa = sp.audio_analysis(id1)
af = sp.audio_features(tracks=[id1])


# In[27]:


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


# In[28]:


all_chunks = chunks(all_tracks, 100)


# In[29]:


for chunk in all_chunks:
    track_ids = [track['id'] for track in chunk]
    chunk_afs = sp.audio_features(tracks=track_ids)
    
    for track, audio_feature in zip(chunk, chunk_afs):
        track['audio_features'] = audio_feature
    
    print(chunk[0])


# In[ ]:





# In[32]:


count=0
for track in all_tracks:
    if 'danceability' not in track:
#         print(track['name'])
        count += 1
print(count)

print(all_tracks[-1])


# In[31]:


# flatten tracks dictionary

keys_to_keep = ['id', 'name', 'popularity', 'uri', 'lang', 'duration_ms', 'time_signature', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'track_href', 'analysis_url']
# artists[0]['name']

cleaned_tracks = []
for track in all_tracks:
    track.update(track['audio_features'])
    new_track = {k: track[k] for k in keys_to_keep}
    new_track['artist'] = track['artists'][0]['name']
    cleaned_tracks.append(new_track)

print(len(cleaned_tracks))


# In[33]:


print(cleaned_tracks[-1])


# In[34]:


import pandas as pd
# cols = ['id', 'name', 'artist', 'popularity', 'uri', 'lang', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'track_href', 'analysis_url', 'time_signature']

mydf = pd.DataFrame(cleaned_tracks)


# In[35]:


mydf.to_csv('multilang_playlist.csv')


# In[36]:


# song_1['track']['id']


# In[37]:


read_df = pd.read_csv('multilang_playlist.csv')


# In[38]:


read_df.tail()


# In[39]:


read_df.describe()


# In[ ]:




