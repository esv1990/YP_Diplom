
# Елистратов Сергей, 14-я когорта, Инженер по тестированию плюс - Дипломный проект.

import sender_stand_request


def test_positive_assert_order_creation():
    new_response = sender_stand_request.post_new_order()  # сохраняем ответ при создании нового заказа
    track_id = new_response.json()['track']  # сохраняем полученный трек в переменную
    response = sender_stand_request.get_info_track(track_id)  # сохраняем результат запроса на получение инфы по треку
    assert response.status_code == 200 #Проверяем что код ответа равен 200
