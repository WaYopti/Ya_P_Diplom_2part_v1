# Ковалев Иван, 16-я когорта - Финальный проект (2 часть). Инженер по тестированию плюс.
import requests
import main_code
from config import URL, TRACK_ID


def test_get_order_by_track():
    create_order_response = main_code.create_order()
    track_id = str(create_order_response["track"])
    response = requests.get(URL + TRACK_ID + track_id)
    assert response.status_code == 200