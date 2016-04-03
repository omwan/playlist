# shows a user's playlists (need to be authenticated via oauth)

import sys
import spotipy
import spotipy.util as util
from spotifyThing import authorize

def show_tracks(token):
    
    sp = spotipy.Spotify(auth=token)
    username = sp.me()["id"]
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['owner']['id'] == username:
            print
            print playlist['name']
            print '  total tracks', playlist['tracks']['total']
            results = sp.user_playlist(username, playlist['id'],
                fields="tracks,next")
            tracks = results['tracks']
            show_tracks(tracks)
            while tracks['next']:
                tracks = sp.next(tracks)
                show_tracks(tracks)
                
    for i, item in enumerate(tracks['items']):
        track = item['track']
        return "   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name'])


    
