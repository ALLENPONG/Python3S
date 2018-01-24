from flask import Flask
from flask import request
import sys


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def sign_form():
    return '''<form action="/signin" method="POST">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">sign in</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def singin():
    if request.form['username'] == 'admin' and request.form['password'] == '123':
        return '<h3> hello </h3>'
    else:
        return '<h3>Bad request username or password</h3>'

if __name__ == '__main__':
    app.run()

