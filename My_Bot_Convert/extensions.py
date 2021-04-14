import requests
import json
from config import keys, API_KEY

class ConvertionException(Exception):
    pass

class Converter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException('одинаковые валюты!')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать{base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество{amount}')

        r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&base={quote_ticker}&symbols={base_ticker}')
        total_base = json.loads(r.content)['rates'][base_ticker]*amount
        return total_base