from downtool import down
from flask import Flask


app = Flask(__name__)
app.debug=True

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login')
def login():
    return 'Login'


if __name__ == '__main__':
    app.run()