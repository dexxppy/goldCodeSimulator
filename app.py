from flask_session import Session
from flask import Flask
from goldCodeSimulator.backend.routing.routes import bp


def create_app():
    app = Flask(__name__)
    app.secret_key = "super_secret_key"

    app.config['SESSION_TYPE'] = 'filesystem'  # sesje będą zapisywane jako pliki
    Session(app)

    app.register_blueprint(bp)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
