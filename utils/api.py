from utils.http_method import Http_methods
import requests

"""Методы для тестирования Send request API"""

base_url = "https://send-request.me" # Базовый url
base_url_http = "http://send-request.me"

class Send_request_api():

    """Запрос списка компаний"""
    @staticmethod
    def get_companies(base_url=base_url):
        get_resource = '/api/companies/'
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def get_companies_ssl():

        get_resource = "/api/companies/"
        get_url = base_url_http + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

