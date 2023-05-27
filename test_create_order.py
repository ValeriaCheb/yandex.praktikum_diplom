import requests
import config
import data


def prepare_order_comment(comment):
    content = data.order_body.copy()
    content['comment'] = comment

    return content


def create_order(content):
    return requests.post(
        config.URL_SERVICE + config.API_METHOD_CREATE_ORDER,
        json=content,
        headers=data.headers
    )


def get_order_info(track):
    return requests.get(
        config.URL_SERVICE + config.API_METHOD_ORDER_INFO,
        params={"t": track},
        headers=data.headers
    )


def assert_status_code_created(response):
    assert response.status_code == 201


def assert_status_code_success(response):
    assert response.status_code == 200


def test_create_order():
    # Создание заказа и проверка возвращаемого статуса
    order = create_order(prepare_order_comment('TEST Comment'))
    assert_status_code_created(order)

    # Получение Track номера заказа
    order_track = order.json()['track']

    # Получение информации по заказу через Track номер и проверка возвращаемого статуса
    order_info_by_track = get_order_info(order_track)
    assert_status_code_success(order_info_by_track)
