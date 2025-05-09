import requests


class Notify:

    def __init__(self):
        self.__base_url = 'http://127.0.0.1:5000'

    def send_event(self, data):
        requests.post(
            url=f'{self.__base_url}/order/webhook',
            json=data
        )
