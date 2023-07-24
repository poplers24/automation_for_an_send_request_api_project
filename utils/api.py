from utils.http_method import Http_methods

"""Методы для тестирования Send request API"""

base_url = "https://send-request.me" # Базовый url

class Send_request_api():

    """Запрос списка компаний"""
    @staticmethod
    def get_companies():

        get_resource = '/api/companies/'
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

