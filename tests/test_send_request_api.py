import json

from utils.api import Send_request_api
from utils.checking import Checking

"""Проверка запроса списка компаний, компаний и параметров запросов"""
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
    def test_companies_default_request(self):

        print(" Метод GET.CompaniesDefaultRequest")
        result_get = Send_request_api.get_companies()
        Checking.check_status_code(result_get, 200)
        Checking.check_time_response(result_get, 0.5)
        Checking.check_schema(result_get, self.schema_companyList)
        Checking.check_header(result_get, "Content-Type", "application/json")
        Checking.check_header(result_get, "Connection", "keep-alive")
        Checking.check_number_object(result_get, 3)

    def test_companies_eneble_ssl(self):
        base_url_http = "http://send-request.me"

        print(" Метод GET.CompaniesEnableSSL")
        result_get = Send_request_api.get_companies(base_url_http)
        Checking.check_redirect(result_get)
        Checking.check_header(result_get, "Connection", "keep-alive")
        Checking.check_time_response(result_get, 0.5)
        Checking.check_status_code(result_get, 200)


