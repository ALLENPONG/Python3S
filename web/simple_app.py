from flask import Flask, request, render_template


'''
注意: 模板html文件必须放在与app.py 同级的文件夹下面

'''

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def sign_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def singin():
    username = request.form['username']
    password = request.form['password']
    if username == 'allen' and password == '123':
        return render_template('signin_ok.html', username=username)
    else:
        return render_template('form.html', message='Bad request username or password', username=username)


if __name__ == '__main__':
    app.run()
