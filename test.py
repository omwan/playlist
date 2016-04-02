from flask import Flask
from test2 import func
app = Flask(__name__)

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/test/')
def test(name=None):
    return func()
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
