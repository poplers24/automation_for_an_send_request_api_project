import allure
from jsonschema import validate
import requests
import json

"""Schema Send request"""
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
schema_usersList = {
  "type": "object",
  "properties": {
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
    },
    "data": {
      "type": "array",
      "items":{
          "type": "object",
          "properties": {
            "first_name": {
              "type": ["string", "null"]
            },
            "last_name": {
              "type": "string"
            },
            "company_id": {
              "type": ["string", "null"]
            },
            "user_id": {
              "type": "integer"
            }
          },
          "required": [
            "last_name",
            "user_id"
          ]
        }
    }
  },
  "required": [
    "meta",
    "data"
  ]
}
schema_responseUser = {
  "type": "object",
  "properties": {
    "first_name": {
      "type": "string"
    },
    "last_name": {
      "type": "string"
    },
    "company_id": {
      "type": "integer"
    },
    "user_id": {
      "type": "integer"
    }
  },
  "required": [
    "last_name",
    "user_id"
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
schema_meResponse = {
    "type": "object",
    "properties": {
        "token": {
            "type": "string"
        },
        "user_name": {
            "type": "string"
        },
        "email_address": {
            "type": "string",
            "format": "email"
        },
        "valid_till": {
            "type": "string",
            "format": "date-time"
        }
    },
    "required": [
        "token",
        "user_name",
        "email_address",
        "valid_till"
    ]
}

"""Методы для проверки ответов запросов"""
class Checking():


    """Метод для проверки статус кода"""

    # @allure.step
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, f"Статус код ответа {result.status_code} - " \
                                                  f"не соответствует ожидаемому {status_code}"
        print(f"Статус код ответа соответствует ожидаемому - {result.status_code}")


    """Метод для проверки времени ответа"""

    # @allure.step
    @staticmethod
    def check_time_response(result):
        expected_time = 0.5
        assert expected_time > result.elapsed.total_seconds(), f"Время ответа {result.elapsed.total_seconds()} - " \
                                                               f"больше ожидаемого {expected_time}"
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
        assert result.headers[header] == value, f"Значение {header}: {result.headers[header]}, что не соответствует ожидаемому {value}"
        print(f'Заголовок "{header}" корректный - {result.headers[header]}')


    """Метод проверки количества объектов в теле ответа"""

    # @allure.step
    @staticmethod
    def check_number_object(result, number):
        assert len(result.json()['data']) == number, f"Количество объектов в теле ответа {len(result.json()['data'])}, что не соответствует ожидаемому {number}"
        print(f"Количество объектов в теле ответа корректное - {len(result.json()['data'])}")


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
    def check_list_start_company_id(result, expected_start_id):
        start_company_id = result.json()['data'][0]['company_id']
        assert start_company_id == expected_start_id, f"The first company on the list company_id = {start_company_id}," \
                                                      f"which is not what is expected - {expected_start_id}"
        print(f"У первой компании ожидаемый company_id = {start_company_id}")

    """Метод проверки статуса компании"""
    @staticmethod
    def check_company_status(result, expected_status):
        data = result.json()['data']
        for i in data:
            assert i['company_status'] == expected_status, f"Company status {i['company_status']} is not expected {expected_status}"
        print(f"В data присутствуют компании только со статусом {expected_status}")


