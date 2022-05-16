from flask import make_response
import json
from src.utils.constants import HOME_URL
from src.utils.scraper import parse_home, parse_bitcoin, save_data, print_json, print_data


def root_coin():
    try:
        link_to_bitcoin_page = parse_home(HOME_URL)
        data = parse_bitcoin(link_to_bitcoin_page)
        time = data['Obtained']
        save_data(data, time)
        response = make_response(json.dumps(data))
        response.headers["Content-Type"] = "application/json"
        return response
    except Exception as e:
        return make_response({"message": str(e)}, 404)


def get_coin():
    try:
        response = make_response(json.dumps(print_data()))
        response.headers["Content-Type"] = "application/json"
        return response
    except Exception as e:
        return make_response({"message": str(e)}, 404)
