import pytest
import allure
from time import sleep

from src.schemas.schemas import Schemas
from utils.api import Send_request_api
from utils.checking import Checking

class TestUserCreates:

    """Создание, изменение и удаление пользователя"""
    @pytest.mark.xfail(reason="Response body when deleting user - null, does not match expected - string")
    def test_user_created_update_delete(self):

        json_new_user = {
            "first_name": "Maksim",
            "last_name": "Smirnov",
            "company_id": 3
        }

        json_update_user = {
            "first_name": "Ivan",
            "last_name": "Smirnov",
            "company_id": 1
        }

        print("Метод POST.UserCreate")
        result_post = Send_request_api.create_new_user("/api/users/", json_new_user)
        Checking.check_status_code(result_post, 201)
        Checking.check_time_response(result_post)
        Checking.check_schema(result_post, Schemas.SchemaResponseUser)
        Checking.check_header(result_post, "Content-Type", "application/json")
        Checking.check_header(result_post, "Connection", "keep-alive")

        user_id = str(result_post.json()["user_id"])

        print("Метод GET.GetUserCreated")
        result_get = Send_request_api.get_by_id("/api/users/", user_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaResponseUser)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")
        Checking.check_user_json_req_and_res(result_post.text, result_get.text)

        print("Метод PUT.UserUpdate")
        result_put = Send_request_api.update_user("/api/users/", user_id, json_update_user)
        Checking.check_status_code(result_put, 200)
        Checking.check_time_response(result_put)
        Checking.check_schema(result_put, Schemas.SchemaResponseUser)
        Checking.check_header(result_put, "Content-Type", "application/json")
        Checking.check_header(result_put, "Connection", "keep-alive")

        print("Метод GET.GetUserUpdate")
        result_get = Send_request_api.get_by_id("/api/users/", user_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaResponseUser)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")
        Checking.check_user_json_req_and_res(result_put.text, result_get.text)

        print("Метод DELETE.DeleteCreateUser")
        result_delete = Send_request_api.delete_user("/api/users/", user_id)
        Checking.check_status_code(result_delete, 202)
        Checking.check_time_response(result_delete)
        # Checking.check_schema(reult_delete, Schemas.SchemaDeleteUser) # Response body when deleting user - null, does not match expected - string
        Checking.check_header(result_delete, "Content-Type", "application/json")
        Checking.check_header(result_delete, "Connection", "keep-alive")

        print("Метод GET.GetUserDelete")
        result_get = Send_request_api.get_by_id("/api/users/", user_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaError)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")



    """Создание пользователя с привязкой к несуществующей компании"""
    def test_user_created_id_company_absent(self):

        json_new_user = {
            "first_name": "Petr",
            "last_name": "Stepanov",
            "company_id": 12
        }

        result_post = Send_request_api.create_new_user("/api/users/", json_new_user)
        Checking.check_status_code(result_post, 404)
        Checking.check_time_response(result_post)
        Checking.check_schema(result_post, Schemas.SchemaError)
        Checking.check_header(result_post, "Content-Type", "application/json")
        Checking.check_header(result_post, "Connection", "keep-alive")


    """Создание пользователя в обязательном ключе last_name указываем значение null"""
    def test_user_created_requared_none(self):

        json_new_user = {
            "first_name": "Stepan",
            "last_name": None,
            "company_id": 3
        }

        result_post = Send_request_api.create_new_user("/api/users/", json_new_user)
        Checking.check_status_code(result_post, 422)
        Checking.check_time_response(result_post)
        Checking.check_schema(result_post, Schemas.SchemaHttpValidationError)
        Checking.check_header(result_post, "Content-Type", "application/json")
        Checking.check_header(result_post, "Connection", "keep-alive")


    """Создание пользователя с привязкой к компании со статусом CLOSED"""
    def test_user_created_status_company_closed(self):

        json_new_user = {
            "first_name": "Ivan",
            "last_name": "Ivanov",
            "company_id": 6
        }

        result_post = Send_request_api.create_new_user("/api/users/", json_new_user)
        Checking.check_status_code(result_post, 400)
        Checking.check_time_response(result_post)
        Checking.check_schema(result_post, Schemas.SchemaError)
        Checking.check_header(result_post, "Content-Type", "application/json")
        Checking.check_header(result_post, "Connection", "keep-alive")


    """Создание пользователя без обязательного ключа"""
    def test_user_created_no_requared(self):

        json_new_user = {
            "first_name": "Sergei",
            "company_id": 3
        }

        result_post = Send_request_api.create_new_user("/api/users/", json_new_user)
        Checking.check_status_code(result_post, 422)
        Checking.check_time_response(result_post)
        Checking.check_schema(result_post, Schemas.SchemaHttpValidationError)
        Checking.check_header(result_post, "Content-Type", "application/json")
        Checking.check_header(result_post, "Connection", "keep-alive")


    """Запрос пользователя по несуществующему ID"""
    def test_get_user_by_none_id(self):

        user_id = "55432"

        result_get = Send_request_api.get_by_id("/api/users/", user_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaError)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Обновление созданого пользователя, привязать к несуществующей компании"""
    @pytest.mark.xfail(reason="Response body when deleting user - null, does not match expected - string")
    def test_update_user_none_company(self):

        json_new_user = {
            "first_name": "Viktor",
            "last_name": "Ivanov",
            "company_id": 3
        }

        json_update_user = {
            "first_name": "Viktor",
            "last_name": "Ivanov",
            "company_id": 9
        }

        print("Метод POST.UserCreate")
        result_post = Send_request_api.create_new_user("/api/users/", json_new_user)
        Checking.check_status_code(result_post, 201)
        Checking.check_time_response(result_post)
        Checking.check_schema(result_post, Schemas.SchemaResponseUser)
        Checking.check_header(result_post, "Content-Type", "application/json")
        Checking.check_header(result_post, "Connection", "keep-alive")

        user_id = str(result_post.json()["user_id"])

        print("Метод PUT.UserUpdate")
        result_put = Send_request_api.update_user("/api/users/", user_id, json_update_user)
        Checking.check_status_code(result_put, 404)
        Checking.check_time_response(result_put)
        Checking.check_schema(result_put, Schemas.SchemaError)
        Checking.check_header(result_put, "Content-Type", "application/json")
        Checking.check_header(result_put, "Connection", "keep-alive")

        print("Метод DELETE.DeleteCreateUser")
        result_delete = Send_request_api.delete_user("/api/users/", user_id)
        Checking.check_status_code(result_delete, 202)
        Checking.check_time_response(result_delete)
        # Checking.check_schema(result_delete, Schemas.SchemaDeleteUser) # Response body when deleting user - null, does not match expected - string
        Checking.check_header(result_delete, "Content-Type", "application/json")
        Checking.check_header(result_delete, "Connection", "keep-alive")

        print("Метод GET.GetUserDelete")
        result_get = Send_request_api.get_by_id("/api/users/", user_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaError)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Обновление несуществующего пользователя"""
    def test_update_user_none_user_id(self):

        user_id = "45677"

        json_update_user = {
            "first_name": "Viktor",
            "last_name": "Ivanov",
            "company_id": 9
        }

        print("Метод PUT.UserUpdate")
        result_put = Send_request_api.update_user("/api/users/", user_id, json_update_user)
        Checking.check_status_code(result_put, 404)
        Checking.check_time_response(result_put)
        Checking.check_schema(result_put, Schemas.SchemaError)
        Checking.check_header(result_put, "Content-Type", "application/json")
        Checking.check_header(result_put, "Connection", "keep-alive")


    """Удаление несуществующего пользователя"""
    def test_delete_none_user_id(self):

        user_id = "345666"

        print("Метод DELETE.DeleteCreateUser")
        result_delete = Send_request_api.delete_user("/api/users/", user_id)
        Checking.check_status_code(result_delete, 404)
        Checking.check_time_response(result_delete)
        Checking.check_schema(result_delete, Schemas.SchemaError)
        Checking.check_header(result_delete, "Content-Type", "application/json")
        Checking.check_header(result_delete, "Connection", "keep-alive")