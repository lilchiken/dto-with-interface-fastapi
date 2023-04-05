import requests
from typing import Union


def response_now(
    token: str,
    location: str
) -> requests.Response:
    """Возвращает Response по url "v1/weather/Now"

    Агрументы:
    token -- Ваш токен на сайте "api.m3o.com"
    location -- место, на которое мы получаем прогноз погоды
    """

    response = requests.post(
        'https://api.m3o.com/v1/weather/Now',
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(token)
        },
        json={
            "location": location
        }
    )
    return response

def response_forecast(
    token: str,
    days: Union[str, int],
    location: str
) -> requests.Response:
    """Возвращает Response по url "v1/weather/Forecast"

    Агрументы:
    token -- Ваш токен на сайте "api.m3o.com"
    days -- на сколько дней нам нужен прогноз погоды
    location -- место, на которое мы получаем прогноз погоды
    """

    response = requests.post(
        'https://api.m3o.com/v1/weather/Forecast',
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(token)
        },
        json={
            "days": int(days),
            "location": location
        }
    )
    return response
