import requests


BASE_URL = "https://adventofcode.com/2022/day/{}/input"


def get_input_data(day: str):
    url = BASE_URL.format(day)
    print(url)
    return requests.get(BASE_URL.format(day))
