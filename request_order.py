import configuration
import requests
import data


# Функция для создания заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=order_body)


# Функция для запоминания трек-номера
def get_order_track():
    track_response = post_new_order(data.order_body)
    return track_response.json()["track"]


# Функция для получения заказа по трек-номеру
def get_order_info_by_track():
    track = get_order_track()
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER, params={"t": track})
