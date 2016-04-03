# shows a user's playlists (need to be authenticated via oauth)

import sys
import spotipy
import spotipy.util as util
from spotifyThing import authorize

##def show_tracks(request):
##    for i, item in enumerate(tracks['items']):
##        track = item['track']
##        return "   %d %32.32s %s" % (i, track['artists'][0]['name'],
##            track['name'])
##
##
##if __name__ == '__main__':
##    if len(sys.argv) > 1:
##        username = sys.argv[1]
##    else:
##        print "Whoops, need your username!"
##        print "usage: python user_playlists.py [username]"
##        sys.exit()
##
##    token = util.prompt_for_user_token(username)
##
##    if token:
##        sp = spotipy.Spotify(auth=token)
##        playlists = sp.user_playlists(username)
##        for playlist in playlists['items']:
##            if playlist['owner']['id'] == username:
##                print
##                print playlist['name']
##                print '  total tracks', playlist['tracks']['total']
##                results = sp.user_playlist(username, playlist['id'],
##                    fields="tracks,next")
##                tracks = results['tracks']
##                show_tracks(tracks)
##                while tracks['next']:
##                    tracks = sp.next(tracks)
##                    show_tracks(tracks)
##    else:
##        print "Can't get token for", username
##



def getToken():

##    client_id = os.getenv('SPOTIPY_CLIENT_ID')
##    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
##    redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
##
##    sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri)
##    
##    auth_url = authorize()
##    code = sp_oauth.parse_response_code(auth_url)
##    token_info = sp_oauth.get_access_token(code)
    
    scope = 'user-library-read'
    token = util.prompt_for_user_token(username, scope)

    returnString = ""

    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        returnString = returnString + track['name'] + ' - ' + track['artists'][0]['name']

    return returnString
