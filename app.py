from flask import Flask
from spotifyThing import func
app = Flask(__name__)

from flask import render_template

@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/auth/')
def test(name=None):
    return func(username)
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
