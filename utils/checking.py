import allure
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from langdetect import detect
import requests
import json



"""Методы для проверки ответов запросов"""
class Checking():

    """Метод для проверки статус кода"""
    # @allure.step
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, f"Status code response {result.status_code} - " \
                                                  f"does not match expected - {status_code}"
        print(f"Статус код ответа соответствует ожидаемому - {result.status_code}")


    """Метод для проверки времени ответа"""
    # @allure.step
    @staticmethod
    def check_time_response(result):
        expected_time = 0.5
        assert expected_time > result.elapsed.total_seconds(), f"Time response {result.elapsed.total_seconds()} - " \
                                                               f"is longer than expected {expected_time}"
        print(f"Время ответа не превышает 500ms - {result.elapsed.total_seconds()}")


    """Метод проверки соответствия response body schema"""
    # @allure.step
    @staticmethod
    def check_schema(result, schema):
        validate(instance=result.json(), schema=schema)
        print("Тело ответа соответствует schema")


    """Метод проверки заголовков"""
    # @allure.step
    @staticmethod
    def check_header(result, header, value):
        assert result.headers[header] == value, f"Value {header}: {result.headers[header]}, does not match expected - {value}"
        print(f'Заголовок "{header}" корректный - {result.headers[header]}')


    """Метод проверки количества объектов в теле ответа"""
    # @allure.step
    @staticmethod
    def check_quantity_object(result, expected_quantity_object):
        assert len(result.json()['data']) == expected_quantity_object, f"Number of objects in response body - {len(result.json()['data'])}, does not match expected - {expected_quantity_object}"
        print(f"Количество объектов в теле ответа соотвествует ожидаемому - {len(result.json()['data'])}")


    """Метод проверки редиректа и статус кода редиректа"""
    # @allure.step
    @staticmethod
    def check_redirect(result):
        url = ""
        status_code = str(result.history[0])[11:14]
        for i, response in enumerate(result.history, 1):
            url = response.url
        assert url[:5] == "http:", f"Request sent not from http:, link_start = {url}"
        assert status_code == "301", f"Status code is not correct {status_code}"
        print(f"Запрос отправлен по http - {url}")
        print(f"Статус код редиректа корректный - {status_code}")
        print(f"Редирект на {result.url}")

    """Метод проверки, что список начинается с указанного id"""
    # @allure.step
    @staticmethod
    def check_list_start_id(result, property_id, expected_start_id):
        list_start_object = result.json()['data'][0][property_id]
        assert list_start_object == expected_start_id, f"The first object on the list id = {list_start_object}," \
                                                      f"which is not what is expected - {expected_start_id}"
        print(f"У первого объекта списка ожидаемый id = {list_start_object}")

    """Метод проверки статуса компании"""
    @staticmethod
    def check_company_status(result, expected_status):
        data = result.json()['data']
        for i in data:
            assert i['company_status'] == expected_status, f"Company status {i['company_status']} is not expected {expected_status}"
        print(f"В data присутствуют компании только со статусом {expected_status}")

    """Метод проверки соответствия id в url и company_id в response body"""
    @staticmethod
    def check_id_in_response(result, field_name_id):
        url_id = result.url.split('/')[-1]
        id = result.json()[field_name_id]
        assert url_id == str(id), f"company_id = {id} in JSON does not match id in url = {url_id} "
        print(f"В JSON company_id, совпадает с id в URI")

    """Метод проверки соответствия языка в description указанному языку"""
    @staticmethod
    def check_language_in_response_body(result, lang):
        description = detect(result.json()['description'])
        assert description == lang, f"Language in description - {description} does not macth expected - {lang} "
        print(f"Язык в description соответствует ожидаемому - {description}")

    """Проверка соответствия отправленным данным и полученным"""
    @staticmethod
    def check_user_json_req_and_res(result_json_post, result_json_get):
        assert result_json_get == result_json_post, f"User data requested {result_json_get} does not match with user data created {result_json_post}"
        print("User совпадает")




