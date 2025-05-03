import requests


class Notify:

    def __init__(self):
        self.__base_url = 'https://webhook.site'

    def send_event(self, data):
        requests.post(
            url=f'{self.__base_url}/3d06239d-8da0-4491-b443-14ce7812b363',
            json=data
        )
