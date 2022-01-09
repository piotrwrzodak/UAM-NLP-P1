import json
import requests


def get_data():
    resp = requests.get(url="https://justjoin.it/api/offers")
    data = resp.json()

    with open('data/raw_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

