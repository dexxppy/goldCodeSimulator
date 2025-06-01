from flask import Blueprint, current_app, render_template, session

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/')
def explaination_page():
    return render_template('explaination.html')

@bp.route('/submit', methods=['POST'])
def submit():
    return

@bp.route('/results')
def result_page():
    data = session.get('data', [])
    return render_template('result.html', data=data)
