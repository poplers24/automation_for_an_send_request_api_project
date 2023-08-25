from utils.http_method import Http_methods
from requests import Request, Session
import requests

"""Методы для тестирования Send request API"""

base_url = "https://send-request.me" # Базовый url

class Send_request_api():

    """Запрос списка компаний"""
    @staticmethod
    def get_list_companies(endpoint, base_url=base_url):
        get_url = base_url + endpoint
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Запрос списка компаний с параметрами"""
    @staticmethod
    def get_companies_with_query_parameters(endpoint, *params, base_url=base_url):
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

    """Запрос компании по id"""
    @staticmethod
    def get_company_by_id(endpiont, id, base_url=base_url):
        get_url = base_url + endpiont + id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def get_company_by_id_add_headers(endpiont, id, add_header, base_url=base_url):
        get_url = base_url + endpiont + id
        print(get_url)
        additional_headers = add_header
        result_get = Http_methods.get(get_url, additional_headers=additional_headers)
        print(result_get.text)
        return result_get





