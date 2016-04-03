from flask import Flask
from spotifyThing import authorize
from showPlaylists import show_tracks
from flask import redirect
from flask import request
app = Flask(__name__)

from flask import render_template

@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/auth/')
def test(name=None):
    return redirect(authorize(), code=302)

@app.route('/tracks')
def tracks(name=None):
    token = authorize().access_token
    return token;
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
