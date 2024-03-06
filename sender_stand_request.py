import data
import requests
import configuration


# POST запрос на создание заказа

def post_new_order():
    return requests.post(configuration.URL_SERVER + configuration.CREATE_NEW_ORDER,
                         json=data.order_create)


print(post_new_order().status_code)
print(post_new_order().text)


# Запрос на получение заказа по его номеру
def get_info_track(track_id):
    return requests.get(configuration.URL_SERVER + configuration.GET_INFO_BY_TRACK + str(track_id))



