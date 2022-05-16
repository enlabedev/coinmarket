from flask_restful import Api
from src.api.v1.routes import Main, Coin


def generate_routes(app):
    # Create api.
    api = Api(app)
    api.add_resource(Main, "/coin")
    api.add_resource(Coin, "/coin/get")
