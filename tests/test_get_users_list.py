import pytest
import allure
from time import sleep

from src.schemas.schemas import Schemas
from utils.api import Send_request_api
from utils.checking import Checking

class TestGetUsersList:

    """Получить список пользователей, с query-параметром limit и offset"""
    def test_users_with_limit_and_offset(self):

        print(" Метод GET.UsersWithLimit&Offset")

        # Получаем user_id для последующей проверки offset
        result_get = Send_request_api.get_list_with_query_parameters("/api/users/", "limit=10")
        get_id_to_check = result_get.json()['data'][5]['user_id']

        # сам тест
        result_get = Send_request_api.get_list_with_query_parameters("/api/users/", "limit=10", "offset=5")
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_quantity_object(result_get, 10)
        Checking.check_list_start_id(result_get, "user_id", get_id_to_check)
        Checking.check_schema(result_get, Schemas.SchemaUsersList)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Получить список users, с невалидным параметром limit (отрицательное число)"""
    # @pytest.mark.xfail(reason="gives an error on the status code - 200, expected - 422")
    # def test_users_with_inv_limit(self):
    #
    #     print("Метод GET.UsersWithInvLimit")
    #     result_get = Send_request_api.get_list_with_query_parameters("/api/users/", "limit=-5")
    #     Checking.check_status_code(result_get, 422)
    #     Checking.check_time_response(result_get)
    #     Checking.check_schema(result_get, Schemas.SchemaHttpValidationError)
    #     Checking.check_header(result_get, "Content-Type", "application/json")
    #     Checking.check_header(result_get, "Connection", "keep-alive")


    """Получить список пользователей, с невалидным query-параметром limit(строка вместо числа)"""
    def test_users_with_str_limit(self):

        print("Метод GET.UsersWithStrLimit")
        result_get = Send_request_api.get_list_with_query_parameters("/api/users/", "limit=abc")
        Checking.check_status_code(result_get, 422)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaHttpValidationError)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Наименование: Получить список пользователей, по незащищенному протоколу http"""
    def test_users_enable_ssl(self):

        print("Метод GET.UsersEnableSSL")
        result_get = Send_request_api.get_list("/api/users/", "http://send-request.me")
        Checking.check_redirect(result_get)
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaUsersList)
        Checking.check_header(result_get, "Connection", "keep-alive")