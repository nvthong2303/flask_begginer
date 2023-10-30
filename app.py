import os
from flask import Flask
from database.db import db
from flask_cors import CORS
from dotenv import load_dotenv


load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS'))
    app.url_map.strict_slashes = False
    db.init_app(app)
    CORS(app)

    app.register_blueprint(users_blueprint, url='/api/v1')

    # @app.errorhandler(BadRequestException)
    # def bad_request_exception(e):
    #     return bad_request

    return app


app = create_app(app)
