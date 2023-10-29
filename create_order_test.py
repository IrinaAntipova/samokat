import sender_stand_request
import data

def test_create_order():
    # Выполнить запрос на создание заказа.
    response_create_order = sender_stand_request.post_new_order(data.order_body)
    # Сохранить номер трека заказа.
    track = response_create_order.json()["track"]
    # Выполнить запрос на получения заказа по треку заказа.
    response_get_order = sender_stand_request.get_order_by_track(track)
    # Проверить, что код ответа равен 200.
    assert response_get_order.status_code == 200

