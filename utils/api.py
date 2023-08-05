from utils.http_method import Http_methods
import requests

"""Методы для тестирования Send request API"""

base_url = "https://send-request.me" # Базовый url

class Send_request_api():

    """Запрос списка компаний"""
    @staticmethod
    def get_list_companies(endpoint, base_url=base_url):
        # endpoint = '/api/companies/'
        get_url = base_url + endpoint
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def get_companies_with_query_parameters(endpoint, *params, base_url=base_url):
        get_resource = '/api/companies/'
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


