import sys
import spotipy
import spotipy.util as util
SPOTIPY_CLIENT_ID='a81f0f66c3774954b0eeda5564e918b7'
SPOTIPY_CLIENT_SECRET='b3b19f4192804965b6529bb9cb1c6509'
SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
scope = 'user-library-read'


def func(username):
    if len(sys.argv)>1:
        username = sys.argv[1]
    else:
        print "Usage: %s username" % (sys.argv[0],)
        sys.exit()

    token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            print track['name'] + ' - ' + track['artists'][0]['name']
    else:
        print "Can't get token for", username
