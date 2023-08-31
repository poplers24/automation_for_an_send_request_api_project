from utils.http_method import Http_methods
from requests import Request, Session
import requests

"""Методы для тестирования Send request API"""

base_url = "https://send-request.me" # Базовый url

class Send_request_api():

    """Companies list"""

    # Запрос списка компаний
    @staticmethod
    def get_list(endpoint, base_url=base_url):
        get_url = base_url + endpoint
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    # Запрос списка компаний с параметрами
    @staticmethod
    def get_list_with_query_parameters(endpoint, *params, base_url=base_url):
        get_url = base_url + endpoint + "?"
        for i in params:
            if i == params[-1]:
                get_url += i
            else:
                get_url += i + "&"
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    # Запрос компании по id
    @staticmethod
    def get_by_id(endpiont, id, base_url=base_url):
        get_url = base_url + endpiont + id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    # Запрос компаний по id с доп. заголовками
    @staticmethod
    def get_by_id_and_additional_header(endpiont, id, add_header, base_url=base_url):
        get_url = base_url + endpiont + id
        print(get_url)
        additional_headers = add_header
        result_get = Http_methods.get(get_url, additional_headers=additional_headers)
        print(result_get.text)
        return result_get

    """Users"""


