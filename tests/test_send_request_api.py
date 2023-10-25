import json
import pytest
import allure
from time import sleep

from src.schemas.schemas import Schemas
from utils.api import Send_request_api
from utils.checking import Checking
from src.pydantic_schemas.schemas import CompanyError


"""Проверка запроса списка компаний, компаний и параметров запросов"""
# @allure.epic("Test get company list")
class Test_get_companies_list():


    """Companies"""

    """ Дефолтный запрос списка компаний"""
    @allure.description("Test get list companies default request")
    def test_companies_default_request(self):

        print(" Метод GET.CompaniesDefaultRequest")
        result_get = Send_request_api.get_list("/api/companies/")
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_quantity_object(result_get, 3)
        Checking.check_schema(result_get, Schemas.SchemaCompanyList)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Отправляем запрос по незащищенному протоколу HTTP"""
    @allure.description("Test companies eneble ssl")
    def test_companies_eneble_ssl(self):

        print(" Метод GET.CompaniesEnableSSL")
        result_get = Send_request_api.get_list("/api/companies/", "http://send-request.me")
        Checking.check_redirect(result_get)
        Checking.check_header(result_get, "Connection", "keep-alive")
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_schema(result_get, Schemas.SchemaCompanyList)


    """Проверяем корректность работы query-параметров limit и offset"""
    @allure.description("Test get list companies with params limit and offset")
    def test_companies_with_limit_and_offset(self):

        print(" Метод GET.CompaniesWithLimitAndOffset")
        result_get = Send_request_api.get_list_with_query_parameters("/api/companies/", "limit=5", "offset=2")
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaCompanyList)
        Checking.check_quantity_object(result_get, 5)
        Checking.check_list_start_id(result_get, "company_id", 3)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Проверяем фильтрацию компаний по query-параметру status=ACTIVE"""
    @allure.description("Test get list companies with param company_status - ACTIVE")
    def test_companies_with_status_active(self):

        print(" Метод GET.CompaniesWithStatusActive")
        result_get = Send_request_api.get_list_with_query_parameters("/api/companies/", "status=ACTIVE",
                                                                          "limit=10")
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaCompanyList)
        Checking.check_company_status(result_get, 'ACTIVE')
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Проверяем фильтрацию компаний по query-параметру status=CLOSED"""
    @allure.description("Test get list companies with param company_status - CLOSED")
    def test_companies_with_status_closed(self):

        print(" Метод GET.CompaniesWithStatusClosed")
        result_get = Send_request_api.get_list_with_query_parameters("/api/companies/", "status=CLOSED",
                                                                          "limit=10")
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaCompanyList)
        Checking.check_company_status(result_get, 'CLOSED')
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Проверяем фильтрацию компаний по query-параметру status=BANKRUPT"""
    @allure.description("Test get list companies with param company_status - BANKRUPT")
    def test_companies_with_status_bankrupt(self):

        print(" Метод GET.CompaniesWithStatusBankrupt")
        result_get = Send_request_api.get_list_with_query_parameters("/api/companies/", "status=BANKRUPT",
                                                                          "limit=10")
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaCompanyList)
        Checking.check_company_status(result_get, 'BANKRUPT')
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Негативный тест - получить список компаний с невалидным значением параметра status=ABC"""
    def test_companies_with_inv_query_status(self):

        print(" Метод GET.CompaniesWithInvQueryStatus")
        result_get = Send_request_api.get_list_with_query_parameters("/api/companies/", "status=ABC")
        Checking.check_status_code(result_get, 422)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaHttpValidationError)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Негативный тест - получить список компаний с отрицательным значением параметра limit=-1"""
    @pytest.mark.xfail(reason="gives an error on the status code - 200, expected - 422")
    def test_companies_with_inv_query_limit(self):

        print(" Метод GET.CompaniesWithInvQueryStatus")
        result_get = Send_request_api.get_list_with_query_parameters("/api/companies/", "limit=-1")
        Checking.check_status_code(result_get, 422)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaHttpValidationError)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Негативный тест - получить список компаний с невалидным значением параметра limit=ABC"""
    def test_companies_with_str_query_limit(self):

        print(" Метод GET.CompaniesWithStrQueryLimit")
        result_get = Send_request_api.get_list_with_query_parameters("/api/companies/", "limit=ABC")
        Checking.check_status_code(result_get, 422)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaHttpValidationError)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Негативный тест - получить список компаний с отрицатльеным значением параметра offset=-1"""
    def test_companies_with_inv_query_offset(self):

        print(" Метод GET.CompaniesWithInvQueryOffset")
        result_get = Send_request_api.get_list_with_query_parameters("/api/companies/", "offset=-1")
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaCompanyList)
        Checking.check_list_start_id(result_get, "company_id", 1)
        Checking.check_quantity_object(result_get, 3)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Негативный тест - получить список компаний с невалидным значением параметра offset=ABC"""
    def test_companies_with_str_query_offset(self):

        print(" Метод GET.CompaniesWithStrQueryOffset")
        result_get = Send_request_api.get_list_with_query_parameters("/api/companies/", "offset=ABC")
        Checking.check_status_code(result_get, 422)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaHttpValidationError)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Получить информацию по ID компании"""
    def test_company_by_id(self):

        print(" Метод GET.CompanyById")
        result_get = Send_request_api.get_by_id("/api/companies/", "1")
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_id_in_response(result_get, 'company_id')
        Checking.check_schema(result_get, Schemas.SchemaCompany)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Негативный тест - получить информацию по несуществующему ID компании"""
    def test_company_by_none_id(self):

        print(" Метод GET.CompanyByNoneId")
        result_get = Send_request_api.get_by_id("/api/companies/", "8")
        Checking.check_status_code(result_get, 404)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaError)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Получаем компанию по ID, с выбором поддерживаемого языка"""
    def test_company_by_id_lang(self):
        add_header = {"Accept-Language": "RU"}

        print(" Метод GET.CompanyByIdLangRU")
        result_get = Send_request_api.get_by_id_and_additional_header("/api/companies/", "1", add_header)
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_id_in_response(result_get, 'company_id')
        Checking.check_schema(result_get, Schemas.SchemaCompany)
        Checking.check_language_in_response_body(result_get, 'ru')
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Получить компанию по ID, с выбором неподдерживаемого языка"""
    def test_company_by_id_inv_lang(self):
        add_header = {"Accept-Language": "AM"}

        print(" Метод GET.CompanyByIdInvLang")
        result_get = Send_request_api.get_by_id_and_additional_header("/api/companies/", "1", add_header)
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_id_in_response(result_get, 'company_id')
        Checking.check_schema(result_get, Schemas.SchemaCompany)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Users"""

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


    """Получение токена. Вход с логином длиной 7 символов и валидным паролем и запрос ифнормации с полученным токеном"""
    @pytest.mark.xfail(reason="the token field is not received in the response body, which does not correspond to the schema")
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


    #ISSUES
    #В каждом эндпоинте заложена ошибка


    """Получить список компаний, с фильтрацией limit, offset, status"""
    @pytest.mark.xfail(reason="Filtering by status parameter is not applied")
    def test_issues_companies_with_query(self):

        print("Метод GET.IssuesCompanyesWithQuery")
        # Получаем user_id для последующей проверки offset
        result_get = Send_request_api.get_list_with_query_parameters("/api/companies/", "limit=10")
        get_id_to_check = result_get.json()['data'][1]['company_id']

        result_get = Send_request_api.get_list_with_query_parameters('/api/issues/companies', 'limit=1', 'offset=1', 'status=ACTIVE')
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_list_start_id(result_get, 'company_id', get_id_to_check)
        Checking.check_company_status(result_get, "ACTIVE")
        Checking.check_schema(result_get, Schemas.SchemaCompanyList)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Получить компанию по ID"""
    @pytest.mark.xfail(reason='Problem during response, more than 5 seconds')
    def test_issues_company_by_id(self):

        print("Метод GET.IssuesCompanyByID")
        result_get = Send_request_api.get_by_id('/api/issues/companies/', '3')
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaCompany)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")


    """Получить информацию по user"""
    @pytest.mark.xfail(reason="Invalid status code, missing fields in the response body")
    def test_issues_get_user_by_id(self):

        json_new_user = {
            "first_name": "Petr",
            "last_name": "Smirnov",
            "company_id": 3
        }

        print("Метод POST.IssuesGetUserById")
        # Создаем пользователя
        result_post = Send_request_api.create_new_user("/api/users/", json_new_user)
        Checking.check_status_code(result_post, 201)
        Checking.check_time_response(result_post)
        Checking.check_schema(result_post, Schemas.SchemaResponseUser)
        Checking.check_header(result_post, "Content-Type", "application/json")
        Checking.check_header(result_post, "Connection", "keep-alive")

        # Получаем user_id
        user_id = str(result_post.json()['user_id'])

        print("Метод GET.IssuesGetUserById")
        # Запрашиваем user
        result_get = Send_request_api.get_by_id('/api/issues/users/', user_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaResponseUser)
        Checking.check_user_json_req_and_res(result_post.text, result_get.text)
        Checking.check_id_in_response(result_get, 'user_id')
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")




































