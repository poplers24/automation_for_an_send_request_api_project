import pytest
import allure
from time import sleep

from src.schemas.schemas import Schemas
from utils.api import Send_request_api
from utils.checking import Checking

class TestIssues:
    # В каждом эндпоинте заложена ошибка

    """Получить список компаний, с фильтрацией limit, offset, status"""

    @pytest.mark.xfail(reason="Filtering by status parameter is not applied")
    def test_issues_companies_with_query(self):
        print("Метод GET.IssuesCompanyesWithQuery")
        # Получаем user_id для последующей проверки offset
        result_get = Send_request_api.get_list_with_query_parameters("/api/companies/", "limit=10")
        get_id_to_check = result_get.json()['data'][1]['company_id']

        result_get = Send_request_api.get_list_with_query_parameters('/api/issues/companies', 'limit=1', 'offset=1',
                                                                     'status=ACTIVE')
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