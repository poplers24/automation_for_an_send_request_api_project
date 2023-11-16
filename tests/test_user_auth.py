import pytest
import allure
from time import sleep

from src.schemas.schemas import Schemas
from utils.api import Send_request_api
from utils.checking import Checking

class TestUserAuth:
    """Получение токена. Вход с логином длиной 7 символов и валидным паролем и запрос ифнормации с полученным токеном"""

    @pytest.mark.xfail(
        reason="the token field is not received in the response body, which does not correspond to the schema")
    def test_auth_login_length_7_valid_pass_and_get_user(self):
        json_body = {
            "login": "Kirill7",
            "password": "qwerty12345"
        }

        print("Метод POST.AuthLogin7ValidPassGetUser")
        # Авторизация
        result_post = Send_request_api.authorize("/api/auth/authorize", json_body)
        Checking.check_status_code(result_post, 200)
        Checking.check_time_response(result_post)
        Checking.check_schema(result_post, Schemas.SchemaAuthorize)
        Checking.check_header(result_post, "Content-Type", "application/json")
        Checking.check_header(result_post, "Connection", "keep-alive")

        # Получаем токен
        token = result_post.json()['token']
        add_header = {'x-token': token}

        # Запрашиваем информацию по токену
        result_get = Send_request_api.get_user_with_token('/api/auth/me', add_header)
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaMeResponse)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")

    """Вход с логином длиной 1 символ и валидным паролем"""

    def test_auth_login_length_1_valid_pass(self):
        json_body = {
            "login": "K",
            "password": "qwerty12345"
        }

        print("Метод POST.AuthLiginLenght1ValidPass")
        result_post = Send_request_api.authorize("/api/auth/authorize", json_body)
        Checking.check_status_code(result_post, 422)
        Checking.check_time_response(result_post)
        Checking.check_schema(result_post, Schemas.SchemaHttpValidationError)
        Checking.check_header(result_post, "Content-Type", "application/json")
        Checking.check_header(result_post, "Connection", "keep-alive")

    """Вход с логином длиной 2 символа и валидным паролем"""

    def test_auth_login_length_2_valid_pass(self):
        json_body = {
            "login": "Ki",
            "password": "qwerty12345"
        }

        print("Метод POST.AuthLiginLenght2ValidPass")
        result_post = Send_request_api.authorize("/api/auth/authorize", json_body)
        Checking.check_status_code(result_post, 422)
        Checking.check_time_response(result_post)
        Checking.check_schema(result_post, Schemas.SchemaHttpValidationError)
        Checking.check_header(result_post, "Content-Type", "application/json")
        Checking.check_header(result_post, "Connection", "keep-alive")

    """Вход с пустым логином и валидным паролем"""

    def test_auth_login_length_0_valid_pass(self):
        json_body = {
            "login": "",
            "password": "qwerty12345"
        }

        print("Метод POST.AuthLiginLenght0ValidPass")
        result_post = Send_request_api.authorize("/api/auth/authorize", json_body)
        Checking.check_status_code(result_post, 422)
        Checking.check_time_response(result_post)
        Checking.check_schema(result_post, Schemas.SchemaHttpValidationError)
        Checking.check_header(result_post, "Content-Type", "application/json")
        Checking.check_header(result_post, "Connection", "keep-alive")

    """Вход без поля логин с валидным паролем"""

    def test_auth_no_field_login_valid_pass(self):
        json_body = {
            "password": "qwerty12345"
        }

        print("Метод POST.AuthNoFieldValidPass")
        result_post = Send_request_api.authorize("/api/auth/authorize", json_body)
        Checking.check_status_code(result_post, 422)
        Checking.check_time_response(result_post)
        Checking.check_schema(result_post, Schemas.SchemaHttpValidationError)
        Checking.check_header(result_post, "Content-Type", "application/json")
        Checking.check_header(result_post, "Connection", "keep-alive")

    """Вход с логином без пароля"""

    def test_auth_valid_login_no_field_pass(self):
        json_body = {
            "login": "Kirill7"
        }

        print("Метод POST.AuthValidLoginNoFieldPass")
        result_post = Send_request_api.authorize("/api/auth/authorize", json_body)
        Checking.check_status_code(result_post, 422)
        Checking.check_time_response(result_post)
        Checking.check_schema(result_post, Schemas.SchemaHttpValidationError)
        Checking.check_header(result_post, "Content-Type", "application/json")
        Checking.check_header(result_post, "Connection", "keep-alive")

    """Вход с логином и неправильным паролем"""

    def test_auth_valid_login_not_correct_pass(self):
        json_body = {
            "login": "Kirill7",
            "password": "qwerty1234"
        }

        print("Метод POST.AuthValidLoginNotCorrectPass")
        result_post = Send_request_api.authorize("/api/auth/authorize", json_body)
        Checking.check_status_code(result_post, 403)
        Checking.check_time_response(result_post)
        Checking.check_schema(result_post, Schemas.SchemaError)
        Checking.check_header(result_post, "Content-Type", "application/json")
        Checking.check_header(result_post, "Connection", "keep-alive")

    """Вход с логином и пустым паролем"""

    def test_auth_valid_login_pass_0(self):
        json_body = {
            "login": "Kirill7",
            "password": ""
        }

        print("Метод POST.AuthValidLoginPass0")
        result_post = Send_request_api.authorize("/api/auth/authorize", json_body)
        Checking.check_status_code(result_post, 403)
        Checking.check_time_response(result_post)
        Checking.check_schema(result_post, Schemas.SchemaError)
        Checking.check_header(result_post, "Content-Type", "application/json")
        Checking.check_header(result_post, "Connection", "keep-alive")

    """Запрос информации по user с невалидным(несуществующим) token"""

    def test_get_user_not_valid_token(self):
        json_body = {
            "login": "Kir",
            "password": "qwerty12345"
        }

        print("Метод POST.GetUserNotValidToken")
        # Авторизация
        result_post = Send_request_api.authorize("/api/auth/authorize", json_body)
        Checking.check_status_code(result_post, 200)
        Checking.check_time_response(result_post)
        Checking.check_schema(result_post, Schemas.SchemaAuthorize)
        Checking.check_header(result_post, "Content-Type", "application/json")
        Checking.check_header(result_post, "Connection", "keep-alive")

        # Получаем токен
        token = result_post.json()['token']
        # Изменяем токен
        token_incorrect = token[0:-10] + "qwerty3BB"
        print(token_incorrect)

        print("Метод GET.GetUserNotValidToken")
        # Запрашиваем информацию по user
        add_header = {'x-token': token_incorrect}
        result_get = Send_request_api.get_user_with_token('/api/auth/me', add_header)
        Checking.check_status_code(result_get, 403)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaError)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")

    """Запрос информации по user с истекшим token"""

    def test_get_user_expired_token(self):
        json_body = {
            "login": "Kir",
            "password": "qwerty12345",
            "timeout": 3
        }

        print("Метод POST.GetUserExpiredToken")
        # Авторизация
        result_post = Send_request_api.authorize("/api/auth/authorize", json_body)
        Checking.check_status_code(result_post, 200)
        Checking.check_time_response(result_post)
        Checking.check_schema(result_post, Schemas.SchemaAuthorize)
        Checking.check_header(result_post, "Content-Type", "application/json")
        Checking.check_header(result_post, "Connection", "keep-alive")

        # Получаем токен
        token = result_post.json()['token']

        print("Метод GET.GetUserExpiredToken")
        sleep(5)
        add_header = {'x-token': token}
        result_get = Send_request_api.get_user_with_token('/api/auth/me', add_header)
        Checking.check_status_code(result_get, 403)
        # Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaError)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")

    """Запрос информации по user без token"""

    def test_get_user_no_token(self):
        print("Метод GET.GetUserNoToken")
        add_header = {}
        result_get = Send_request_api.get_user_with_token('/api/auth/me', add_header)
        Checking.check_status_code(result_get, 401)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaError)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")