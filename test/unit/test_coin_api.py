from flask import Flask
import json

from src.api.v1.routes import Main

def test_coin_endpoint():
    """Test the root endpoint"""
    app = Flask(__name__)
    #app.register_blueprint(Main, url_prefix="/coin")
    client = app.test_client()
    response = client.get("coin")
    assert response.status_code == 200
    for j in response.json:
        if response.json[j] == "":
            assert False
