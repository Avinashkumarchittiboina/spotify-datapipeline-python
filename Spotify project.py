#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install spotipy


# In[2]:


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



# In[3]:


client_credentials_manager = SpotifyClientCredentials(client_id ="5978f477dd62493fac776f11effa1c68",client_secret="f1904e78ce394a9abb376cd8a61289e4")


# In[4]:


sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


# In[5]:


playlist_link= "https://open.spotify.com/playlist/5ABHKGoOzxkaa28ttQV9sE"


# In[6]:


playlist_link


# In[7]:


playlist_URI = playlist_link.split("/")[-1]


# In[10]:


playlist_URI = playlist_link.split("/")[-1].split("?")[0]


# In[11]:


data = sp.playlist_tracks(playlist_URI)


# In[12]:


data['items'][44]


# In[13]:


data['items'][44]['track']['album']['external_urls']['spotify']


# In[20]:


album_list


# In[22]:


album_list = []
for row in data['items']:
    album_id = row['track']['album']['id']
    album_name = row['track']['album']['name']
    album_release_date = row['track']['album']['release_date']
    album_total_tracks = row['track']['album']['total_tracks']
    album_url = row['track']['album']['external_urls']['spotify']
    album_element = {'album_id' : album_id, 'name' : album_name , 'release_date' : album_release_date, 'total_tracks':album_total_tracks,
                    'url':album_url}
    
    album_list.append(album_element)


# In[21]:


album_list


# In[23]:


data['items'][44]['track']['artists']['']


# In[31]:


artist_list =[]
for row in data['items']:
    for key,value in row.items():
        if key =="track":
            for artist in value['artists']:
                artist_dict = {'artist_id':artist['id'],'artist_name' : artist['name'],'external_url':artist['href']}
                artist_list.append(artist_dict)
                
                


# In[33]:


artist_list


# In[36]:


song_list =[]
for row in data['items']:
    song_id = row['track']['id']
    song_name = row['track']['name']
    song_duration = row['track']['duration_ms']
    song_popularity = row['track']['popularity']
    song_url = row['track']['external_urls']['spotify']
    song_added = row['added_at']
    album_id = row['track']['album']['id']
    artist_id = row['track']['album']['artists'][0]['id']
    song_element = {'song_id' : song_id, 'song_name' : song_name, 'song_duration': song_duration,'song_popularity':song_popularity,
                   'song_url': song_url , 'song_added':song_added,'album_id':album_id,'artist_id':artist_id}
    song_list.append(song_element)
    
print (song_list)


# In[37]:


album_list


# In[38]:


import pandas as pd


# In[39]:


album_df = pd.DataFrame.from_dict(album_list)


# In[40]:


album_df.head()


# In[41]:


song_list_df = pd.DataFrame.from_dict(song_list)


# In[43]:


song_list_df.head()


# In[44]:


song_list_df['song_added'] = pd.to_datetime(song_list_df['song_added'])


# In[45]:


song_list_df.head()


# In[46]:


song_list_df.info()

