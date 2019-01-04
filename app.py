from flask import Flask,render_template, redirect, url_for

app = Flask(__name__)


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/reset')
def reset():
    return render_template('reset.html')

if __name__ == '__main__':
    app.run(debug=True)