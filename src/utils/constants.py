HOME_URL = "https://coinmarketcap.com/"
SAVED_JSON = "Bitcoin.json"
TEMPORARY_JSON = "bitcoin-temp.json"

XPATH_BITCOIN_PAGE = "//tr[1]/td[3]/div/a/@href"
XPATH_BITCOIN_STATITICS = "/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/div/div[3]"
XPATH_BITCOIN_PRICE = (
    XPATH_BITCOIN_STATITICS + "/section/div/div[1]/table/tbody/tr[1]/td/text()"
)
XPATH_PRICE_CHANGE = (
    XPATH_BITCOIN_STATITICS + "/section/div/div[1]/table/tbody/tr[2]/td/span/text()"
)
XPATH_LOW_HIGH_24H = (
    XPATH_BITCOIN_STATITICS + "/section/div/div[1]/table/tbody/tr[3]/td/div/text()"
)
XPATH_TRADING_VOLUME = (
    XPATH_BITCOIN_STATITICS + "/section/div/div[1]/table/tbody/tr[4]/td/span/text()"
)
XPATH_VOLUME_MARKET_CAP = (
    XPATH_BITCOIN_STATITICS + "/section/div/div[1]/table/tbody/tr[5]/td/text()"
)
XPATH_MARKET_DOMINANCE = (
    XPATH_BITCOIN_STATITICS + "/section/div/div[1]/table/tbody/tr[6]/td/span/text()"
)
XPATH_MARKET_RANK = (
    XPATH_BITCOIN_STATITICS + "/section/div/div[1]/table/tbody/tr[7]/td/text()"
)
XPATH_CIRCULATING_SUPPLY = "//div[3]/table/tbody/tr[1]/td/text()"
XPATH_TOTAL_SUPPLY = "//div[3]/table/tbody/tr[2]/td/text()"
XPATH_MAX_SUPPLY = "//div[3]/table/tbody/tr[3]/td/text()"

XPATH_NODES = [
    XPATH_BITCOIN_PRICE,
    XPATH_PRICE_CHANGE,
    XPATH_LOW_HIGH_24H,
    XPATH_TRADING_VOLUME,
    XPATH_VOLUME_MARKET_CAP,
    XPATH_MARKET_DOMINANCE,
    XPATH_MARKET_RANK,
    XPATH_CIRCULATING_SUPPLY,
    XPATH_TOTAL_SUPPLY,
    XPATH_MAX_SUPPLY,
]

VALUES_LIST = [
    "Bitcoin price",
    "Price Change",
    "24h Low / 24h High",
    "Trading Volume",
    "Volume / Market Cap",
    "Market Dominance",
    "Market Rank",
    "Circulating Supply",
    "Total Supply",
    "Max Supply",
]
