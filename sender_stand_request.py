import configuration
import data
import requests



# Функция на создание нового заказа:
def post_new_order(order_body):
    headers = data.headers.copy()
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=order_body,  # тут тело
                         headers=headers)


def get_order_by_track(track):
    payload = {'t': track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                        params=payload,
                        headers=data.headers)