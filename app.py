from flask import Flask, session
from flask.ext.session import Session
from spotifyThing import authorize
import sys
import spotipy
import spotipy.util as util
from showPlaylists import show_tracks
from flask import redirect
from flask import render_template
from flask import request
from spotifychooser import *
import copy
from spotipy import Spotify
app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)
app.debug = True


from flask import render_template

@app.route('/')
def hello(name=None, code=None):
    code = request.args.get("code", None)
    if code is None:
        return render_template('index.html', name=name)
    else:
        print "we have a code, which is: " + code
        sp_oauth = authorize()
        token = sp_oauth.get_access_token(code)
        sp = spotipy.Spotify(auth=token['access_token'])
        user = sp.me()
        session['uid'] = user['id']
        session['token'] = token['access_token']
        return render_template('index.html', code=code)

@app.route('/auth/')
def test(name=None):
    return redirect(authorize().get_authorize_url(), code=302)

@app.route('/tracks/')
def tracks(name=None):
    name = show_tracks(session.get('token', None))
    return render_template('index2.html', name=name)

@app.route('/chooser/<playlistid>')
def chooser(playlistid=None, userid=None):
    userid = session.get('uid', None)
    token = session.get('token', None)
    sp = spotipy.Spotify(auth=token)
    get_playlist_json(sp, userid, playlistid)
    return render_template('index2.html', userid=userid, playlistid=playlistid)

        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
