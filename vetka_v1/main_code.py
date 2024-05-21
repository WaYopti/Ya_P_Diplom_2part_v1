# Ковалев Иван, 16-я когорта - Финальный проект (2 часть). Инженер по тестированию плюс.

import requests
from config import URL, CREATE_ORDER, TRACK_ID
from data import payload


def create_order():
    response = requests.post(URL + CREATE_ORDER, json=payload)
    return response.json()
