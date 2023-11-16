import pytest
import allure
from time import sleep

from src.schemas.schemas import Schemas
from utils.api import Send_request_api
from utils.checking import Checking

class TestGetCompanyById:

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