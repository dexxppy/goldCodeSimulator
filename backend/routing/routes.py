from flask import Blueprint, current_app, render_template, session, request, redirect, url_for

from goldCodeSimulator.backend.services.pipeline import run_full_simulation
from goldCodeSimulator.backend.utils.validator import validate_form_input

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/explain')
def explaination_page():
    return render_template('explaination.html')

@bp.route('/transmit', methods=['POST'])
def run_simulator():
    runs = request.form.get("runs")
    sent_to_transmit = request.form.get("sent_to_transmit")
    error_rate = request.form.get("error_rate")

    n = request.form.get("degree_n")
    seed1 = request.form.get("seed1")
    seed2 = request.form.get("seed2")

    try:
        input_data = validate_form_input(
            sent_to_transmit=sent_to_transmit,
            error_rate_id=error_rate,
            runs=runs,
            n=n,
            seed1=seed1,
            seed2=seed2
        )
    except ValueError as e:
        return str(e), 400

    n = input_data["n"]
    seed1 = input_data["seed1"]
    seed2 = input_data["seed2"]

    results = run_full_simulation(
        runs=int(runs),
        sent_to_transmit=sent_to_transmit,
        error_rate_id=int(error_rate),
        n=n,
        seed1=seed1,
        seed2=seed2
    )
    session.pop('results', None)
    session['results'] = results

    return redirect(url_for('main.result_page'))

@bp.route('/results')
def result_page():
    data = session.get('results')
    if not data:
        data = "no results"

    return render_template('results.html', data=data)
