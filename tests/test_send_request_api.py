import json

import pytest

from utils.api import Send_request_api
from utils.checking import Checking
import allure

"""Проверка запроса списка компаний, компаний и параметров запросов"""
# @allure.epic("Test get company list")
class Test_get_companies_list():

    # body response schema
    schema_companyList = {
            "type": "object",
            "properties": {
                "data": {
                    "type": "array",
                    "items":
                        {
                            "type": "object",
                            "properties": {
                                "company_id": {
                                    "type": "integer"
                                },
                                "company_name": {
                                    "type": "string"
                                },
                                "company_address": {
                                    "type": "string"
                                },
                                "company_status": {
                                    "type": "string",
                                    "enum": ["ACTIVE", "CLOSED", "BANKRUPT"]
                                },
                                "description": {
                                    "type": "string"
                                },
                                "description_lang": {
                                    "type": "array",
                                    "items":
                                        {
                                            "type": "object",
                                            "properties": {
                                                "translation_lang": {
                                                    "type": "string"
                                                },
                                                "translation": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "translation_lang",
                                                "translation"
                                            ]
                                        }

                                }
                            },
                            "required": [
                                "company_id",
                                "company_name",
                                "company_address",
                                "company_status"
                            ]
                        }

                },
                "meta": {
                    "type": "object",
                    "properties": {
                        "limit": {
                            "type": "integer"
                        },
                        "offset": {
                            "type": "integer"
                        },
                        "total": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "total"
                    ]
                }
            },
            "required": [
                "data",
                "meta"
            ]
        }
    schema_company = {
        "type": "object",
        "properties": {
            "company_id": {
                "type": "integer"
            },
            "company_name": {
                "type": "string"
            },
            "company_address": {
                "type": "string"
            },
            "company_status": {
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "description_lang": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "translation_lang": {
                            "type": "string"
                        },
                        "translation": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "translation_lang",
                        "translation"
                    ]
                }
            }
        },
        "required": [
            "company_id",
            "company_name",
            "company_address",
            "company_status",
        ]
    }
    schema_httpValidationError = {
        "type": "object",
        "properties": {
            "detail": {
                "type": "array",
                "items":
                    {
                        "type": "object",
                        "properties": {
                            "loc": {
                                "type": "array",
                                "items": {
                                    "type": [
                                        "string",
                                        "integer"
                                    ]
                                }
                            },
                            "msg": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "loc",
                            "msg",
                            "type"
                        ]
                    }

            }
        },
        "required": [
            "detail"
        ]
    }

    """ Дефолтный запрос списка компаний"""
    @allure.description("Test get list companies default request")
    def test_companies_default_request(self):

        print(" Метод GET.CompaniesDefaultRequest")
        result_get = Send_request_api.get_list_companies("/api/companies/")
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, self.schema_companyList)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")
        Checking.check_number_object(result_get, 3)

    """Отправляем запрос по незащищенному протоколу HTTP"""
    @allure.description("Test companies eneble ssl")
    def test_companies_eneble_ssl(self):
        print(" Метод GET.CompaniesEnableSSL")
        result_get = Send_request_api.get_list_companies("/api/companies/", "http://send-request.me")
        Checking.check_redirect(result_get)
        Checking.check_header(result_get, "Connection", "keep-alive")
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, self.schema_companyList)

    """Проверяем корректность работы uqery-параметров limit и offset"""
    @allure.description("Test get list companies with params limit and offset")
    def test_companies_with_limit_and_offset(self):
        print(" Метод GET.CompaniesWithLimitAndOffset")
        result_get = Send_request_api.get_companies_with_query_parameters("/api/companies/", "limit=5", "offset=2")
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, self.schema_companyList)
        Checking.check_number_object(result_get, 5)
        Checking.check_list_start_company_id(result_get, 3)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")

    """Проверяем фильтрацию компаний по query-параметру status=ACTIVE"""
    @allure.description("Test get list companies with param company_status - ACTIVE")
    def test_companies_with_status_active(self):
        print(" Метод GET.CompaniesWithStatusActive")
        result_get = Send_request_api.get_companies_with_query_parameters("/api/companies/", "status=ACTIVE",
                                                                          "limit=10")
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, self.schema_companyList)
        Checking.check_company_status(result_get, 'ACTIVE')
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")

    """Проверяем фильтрацию компаний по query-параметру status=CLOSED"""
    @allure.description("Test get list companies with param company_status - CLOSED")
    def test_companies_with_status_closed(self):
        print(" Метод GET.CompaniesWithStatusClosed")
        result_get = Send_request_api.get_companies_with_query_parameters("/api/companies/", "status=CLOSED",
                                                                          "limit=10")
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, self.schema_companyList)
        Checking.check_company_status(result_get, 'CLOSED')
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")

    """Проверяем фильтрацию компаний по query-параметру status=BANKRUPT"""
    @allure.description("Test get list companies with param company_status - BANKRUPT")
    def test_companies_with_status_bankrupt(self):
        print(" Метод GET.CompaniesWithStatusBankrupt")
        result_get = Send_request_api.get_companies_with_query_parameters("/api/companies/", "status=BANKRUPT",
                                                                          "limit=10")
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, self.schema_companyList)
        Checking.check_company_status(result_get, 'BANKRUPT')
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")

    """Негативный тест - получить список компаний с невалидным значением параметра status=ABC"""
    def test_companies_with_inv_query_status(self):
        print(" Метод GET.CompaniesWithInvQueryStatus")
        result_get = Send_request_api.get_companies_with_query_parameters("/api/companies/", "status=ABC")
        Checking.check_status_code(result_get, 422)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, self.schema_httpValidationError)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")

    """Негативный тест - получить список компаний с отрицательным значением параметра limit=-1"""
    @pytest.mark.xfail(reason="gives an error on the status code - 200, expected - 422")
    def test_companies_with_inv_query_limit(self):
        print(" Метод GET.CompaniesWithInvQueryStatus")
        result_get = Send_request_api.get_companies_with_query_parameters("/api/companies/", "limit=-1")
        Checking.check_status_code(result_get, 422)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, self.schema_httpValidationError)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")

    """Негативный тест - получить список компаний с невалидным значением параметра limit=ABC"""
    def test_companies_with_str_query_limit(self):
        print(" Метод GET.CompaniesWithStrQueryLimit")
        result_get = Send_request_api.get_companies_with_query_parameters("/api/companies/", "limit=ABC")
        Checking.check_status_code(result_get, 422)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, self.schema_httpValidationError)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")

    """Негативный тест - получить список компаний с невалидным значением параметра limit=-1"""
    def test_companies_with_inv_query_offset(self):
        print(" Метод GET.CompaniesWithInvQueryOffset")
        result_get = Send_request_api.get_companies_with_query_parameters("/api/companies/", "offset=-1")
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get)
        Checking.check_schema(result_get, self.schema_companyList)
        Checking.check_list_start_company_id(result_get, 1)
        Checking.check_number_object(result_get, 3)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")



