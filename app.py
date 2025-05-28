from flask import Flask, render_template, request, redirect, url_for, session
from livereload import Server

app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():


@app.route('/result')
def result():
    data = session.get('data', [])
    return render_template('result.html', data=data)

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.watch('templates/')
    server.watch('static/')
    server.serve(debug=True, host='127.0.0.1', port=5000)
