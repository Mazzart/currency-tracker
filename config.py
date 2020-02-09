import datetime

ENDPOINT = 'https://obmenka24.kiev.ua/ua'
DEFAULT_CURRENCY = 'USD/UAH'
TODAY = f'{datetime.datetime.now().strftime("%A, %d %B")}'
TIMEOUT = 5

# endpoint classes names
NAME = 'currencies__block-name'
BUY = 'currencies__block-buy'
SALE = 'currencies__block-sale'
NUM = 'currencies__block-num'