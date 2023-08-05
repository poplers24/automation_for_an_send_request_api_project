import datetime
import os

class Logger():

    # формируем название файла с датой и временем
    file_name = "logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    # Запись данных в файл лога
    @classmethod
    def write_log_to_file(cls, data: str):

        with open(cls.file_name, 'a', encoding="utf-8") as logger_file:
            logger_file.write(data)

    # получения данных по request
    @classmethod
    def add_request(cls, url: str, method: str):

        # помещаем в лог название теста который в данный момент выполняется
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        # формируем строки по request
        data_to_add = "\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += "\n"

        # записываем данные в файл
        cls.write_log_to_file(data_to_add)

    # получение данных по response
    @classmethod
    def add_response(cls, result):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        # формируем строки по response
        data_to_add = f"Response code: {result.status_code}\n"
        data_to_add += f"Response test: {result.text}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        data_to_add += "\n-----\n"

        # записываем данные в файл
        cls.write_log_to_file(data_to_add)


