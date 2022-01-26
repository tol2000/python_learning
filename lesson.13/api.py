import requests

API_URL = "weather.com"


def fetch(url, params):
    return requests.get(url, params).json()


def get_weather(city):
    return fetch(API_URL, {"city": city})


def get_temp(city):
    weather = get_weather(city)
    return weather["temp"]


# if __name__ == '__main__':
#     fetch = lambda u, p: {"temp": 42}
#     print("Temp:", get_temp("qwe"))
