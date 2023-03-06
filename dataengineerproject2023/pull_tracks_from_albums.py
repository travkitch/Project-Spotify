import tekore as tk
from auth import get_user_token
import pandas as pd

# Initialise client with user's bearer token
token = get_user_token()
spotify = tk.Spotify(token)

#tracks, = spotify.search('monty python')
#for playlist in spotify.playlists(user_id = 'colewhoward').items:
 #   print(playlist.name)


playlists = {'Discover Weekly': '37i9dQZEVXcMnuEgfZEsgY','Daily Mix 4':'37i9dQZF1E35S7mPwutCZv','Daily Mix 2':'37i9dQZF1E3aiRrt42NEjI'}

playlists_tracks = {'Playlist':[],'Track_Name':[],'Artist':[],'Popularity':[],'Album_Name':[]}

for name,id in playlists.items(): 
    for song in spotify.playlist(playlist_id = id).tracks.items:
        playlists_tracks['Playlist'].append(name)
        playlists_tracks['Track_Name'].append(song.track.name)
        playlists_tracks['Artist'].append(song.track.album.artists[0].name)
        playlists_tracks['Popularity'].append(song.track.popularity)
        playlists_tracks['Album_Name'].append(song.track.album.name)


        #print(song.track.name,"|",song.track.populairty)

#print(spotify.playlist(playlist_id = '37i9dQZEVXcMnuEgfZEsgY').tracks.items[1].track.name)

#for song in spotify.playlist(playlist_id = '37i9dQZEVXcMnuEgfZEsgY').tracks.items:
 #   print(song.track.popularity)

tracks_df = pd.DataFrame.from_dict(playlists_tracks)
tracks_df.to_csv('/Users/colehoward/documents/Spotify Project/tracks_csv.csv',index=False, sep=',')
