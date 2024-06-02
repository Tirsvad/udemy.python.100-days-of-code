import os

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_FROM = os.getenv("EMAIL_FROM")
PASSWORD = os.getenv("PASSWORD")
EMAIL_SEND_TO = os.getenv("EMAIL_SEND_TO")

PRODUCT_END_POINT = "https://www.amazon.com/dp/B075CYMYK6/ref=twister_B0CZ9G83PC"
HEADERS = {
    "User-Agent": "Chrome/119.0.0.0",
    "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7"
}
PARAMS = {
    "_encoding": "UTF8",
    "psc": "1"
}
