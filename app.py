from flask import Flask, session
from spotifyThing import authorize
from showPlaylists import show_tracks
from flask import redirect
from flask import request
app = Flask(__name__)
SESSION TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

from flask import render_template

@app.route('/')
def hello(name=None):
    token = request.args.get("code", None)
    if token is None:
        return render_template('index.html', name=name)
    else:
        sp = spotipy.Spotify(auth=token)
        user = sp.me()
        session['token'] = token
        print "we have a token, which is: " + token
        return render_template('index.html', name=name)

@app.route('/auth/')
def test(name=None)
    return redirect(authorize(), code=302)

@app.route('/tracks')
def tracks(name=None):
    show_tracks(session.get('token', None))
    return render_template('index.html', name=name)
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
