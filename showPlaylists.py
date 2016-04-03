# shows a user's playlists (need to be authenticated via oauth)

import sys
import spotipy
import spotipy.util as util
from spotifyThing import authorize

def show_tracks(token):
    
    sp = spotipy.Spotify(auth=token)
    username = sp.me()["id"]
    return sp.user_playlists(username)
##    returnString = ""
##    for playlist in playlists['items']:
##        returnString += '<li>' + playlist['name'] + '</li>'
##    return returnString
