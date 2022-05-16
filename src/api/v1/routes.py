from flask_restful import Resource
from flask import g, request
from src.api.v1.endpoints.coin import root_coin, get_coin


class Main(Resource):
    def get(self):
        return root_coin()


class Coin(Resource):
    def get(self):
        return get_coin()
