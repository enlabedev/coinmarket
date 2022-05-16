from src.utils.scraper import parse_bitcoin

from src.utils.constants import HOME_URL

BTC = HOME_URL + "/currencies/bitcoin/"


def test_btc_json():
    parse = parse_bitcoin(BTC)
    if type(parse) != type({}):
        assert False


def test_btc_happy_path():
    """Test that the scraper returns a list of values"""
    parse = parse_bitcoin(BTC)
    for p in parse:
        if parse[p] == "":
            assert False
    # assert isinstance(parse_bitcoin(BTC), list)
