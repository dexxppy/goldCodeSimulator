import inspect
import backend
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.register_blueprint(backend.routing.bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
