# shows a user's playlists (need to be authenticated via oauth)

import sys
import spotipy
import spotipy.util as util
from spotifyThing import authorize

def show_tracks(token):
    
    sp = spotipy.Spotify(auth=token)
    username = sp.me()['id']
    playlists = sp.user_playlists(username)
    returnList = []
    for playlist in playlists['items']:
        if playlist['owner']['name'] == sp.me()['display_name']:
            returnList.append({'title': playlist['name'], 'id': playlist['id']})
    return returnList
