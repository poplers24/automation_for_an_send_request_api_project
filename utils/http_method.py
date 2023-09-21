import requests
import allure
from utils.logger import Logger

"""Список HTTP методов"""

class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url, additional_headers=None):
        # with allure.step('GET'):
        Logger.add_request(url, method="GET")

        if additional_headers is None:
            additional_headers = {}

        all_headers = {**Http_methods.headers, **additional_headers}

        result = requests.get(url, headers=all_headers, cookies=Http_methods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def post(url, body):
        # with allure.step('POST'):
        Logger.add_request(url, method="POST")
        result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def put(url, body):
        # with allure.step('PUT'):
        Logger.add_request(url, method="PUT")
        result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def delete(url, body=None):
        # with allure.step('DELETE'):
        Logger.add_request(url, method="DELETE")
        result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
        Logger.add_response(result)
        return result