
import pytest
import allure
from time import sleep

from src.schemas.schemas import Schemas
from utils.api import Send_request_api
from utils.checking import Checking

class TestGetCompaniesList:

    valid_status_list = ["ACTIVE", "CLOSED", "BANKRUPT"]
    inv_values_list_for_limit_and_offset = ["-1", "ABC"]

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
    def test_companies_enable_ssl(self):

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


    """Проверяем фильтрацию компаний по query-параметру status=ACTIVE/CLOSED/BANKRUPT"""

    @allure.description("Test get list companies with param company_status - ACTIVE/CLOSED/BANKRUPT")
    @pytest.mark.parametrize("status", valid_status_list)
    def test_companies_with_status(self, status):

        print(" Метод GET.CompaniesWithStatusActive")
        result_get = Send_request_api.get_list_with_query_parameters(
            "/api/companies/",
            f"status={status}", "limit=10")
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaCompanyList)
        Checking.check_company_status(result_get, status)
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


    """Негативный тест - получить список компаний с некорректными значениеми параметра offset - ABC/-1"""
    @pytest.mark.parametrize("value", inv_values_list_for_limit_and_offset)
    def test_companies_with_inv_query_offset(self, value):
        if value == "-1":
            pytest.xfail(reason="Gives an error on the status code - 200, expected - 422")

        print(" Метод GET.CompaniesWithStrQueryOffset")
        result_get = Send_request_api.get_list_with_query_parameters("/api/companies/", f"offset={value}")
        Checking.check_status_code(result_get, 422)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, Schemas.SchemaHttpValidationError)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")