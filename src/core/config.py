from decouple import config
from flask import Flask
from src.core.routes import generate_routes


def conFlask():
    app = Flask(__name__)
    app.config["ENV"] = config("ENV")
    app.config["SECRET_KEY"] = config("SECRET_KEY")
    app.config["TESTING"] = config("TESTING")
    app.config["DEBUG"] = config("DEBUG")
    app.config["SERVER_NAME"] = "{0}:{1}".format(config("DOMAIN"), config("PORT"))
    app.config["SESSION_COOKIE_SECURE"] = config("HTTPS")
    app.config["SESSION_COOKIE_HTTPONLY"] = config("NOJAVASCRIPT")

    generate_routes(app)

    return app

