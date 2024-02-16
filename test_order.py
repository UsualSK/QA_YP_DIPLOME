import request_order
# Кулагин Семен, 13-я когорта — Финальный проект. Инженер по тестированию плюс


def test_get_order_by_track():
    track_number = request_order.get_order_info_by_track()
    assert track_number.status_code == 200