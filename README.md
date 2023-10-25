My practical project by API automation.

API documentation in swagger https://send-request.me/

Test-cases:

ID: PM-1

Name: Get company list

Name request: test_companies_default_request

Step: Send GET request to endpoint /api/companies/

Checks:

1. The request was successfully sent
2. Status code 200
3. Server response time does not exceed 500ms
4. There are 3 companies in the "data" (by default)
5. The response body corresponds to the schema
6. Response header "Content-Type" is "application/json"
7. Response header "Connection" is "keep-alive"


ID: PM-2

Name: Obtain a list of companies via an unsecured HTTP protocol

Name request: test_companies_eneble_ssl

Step: Send GET request to endpoint http://send-request.me/api/companies/

Checks:

1. Check that the request is sent via HTTP
2. Verify that the redirect status code is 301
3. Confirm that a redirect to HTTPS has occurred
4. Check the response header "Connection" - "keep-alive"
5. Check the response header "Content-Type" - "application/json"
6. Status code 200
7. Server response time does not exceed 500ms
8. The response body corresponds to the schema


ID: PM-3

Name: Retrieve a list of companies with filtering based on the "limit" and "offset" parameters.

Name request: test_companies_with_limit_and_offset

Step: Send a GET request to the endpoint /api/companies/ with query parameters limit=5, offset=2

Checks:

1. The request was successfully sent
2. Status code 200
3. Server response time does not exceed 500ms
4. There are 5 companies in the data (due to limit=5)
5. Companies with id 1 and id 2 are absent in the data (due to offset=2)
6. The response body corresponds to the schema
7. Response header "Content-Type" - "application/json"
8. Response header "Connection" - "keep-alive"


ID: PM-4

Name: Retrieve a list of companies with filtering based on the 'status' parameter with the value 'ACTIVE'

Name request: test_companies_with_status_active

Step: Send a GET request to the endpoint /api/companies/ with query parameters status=ACTIVE and limit=10

Checks:

1. The request was successfully sent
2. Status code 200
3. Server response time does not exceed 500ms
4. In the data, there are only companies with the status ACTIVE
5. The response body corresponds to the schema
6. Response header "Content-Type" - "application/json"
7. Response header "Connection" - "keep-alive"


ID: PM-5

Name: Retrieve a list of companies with filtering based on the 'status' parameter with the value 'CLOSED'

Name request: test_companies_with_status_closed

Step: Send a GET request to the endpoint /api/companies/ with query parameters status=CLOSED and limit=10

Checks:

1. The request was successfully sent
2. Status code 200
3. Server response time does not exceed 500ms
4. In the data, there are only companies with the status CLOSED
5. The response body corresponds to the schema
6. Response header "Content-Type" - "application/json"
7. Response header "Connection" - "keep-alive"


ID: PM-6

Name: Retrieve a list of companies with filtering based on the 'status' parameter with the value 'BANKRUPT'

Name request: test_companies_with_status_bankrupt

Step: Send a GET request to the endpoint /api/companies/ with query parameters status=BANKRUPT and limit=10

Checks:

1. The request was successfully sent
2. Status code 200
3. Server response time does not exceed 500ms
4. In the data, there are only companies with the status BANKRUPT
5. The response body corresponds to the schema
6. Response header "Content-Type" - "application/json"
7. Response header "Connection" - "keep-alive"


ID: PM-7

Name: Retrieve a list of companies with an invalid query parameter 'status'

Name request: test_companies_with_inv_query_status

Step: Send a GET request to the endpoint /api/companies/ with the query parameter status=ABC

Checks:

1. The request was successfully sent
2. Status code 422
3. Server response time does not exceed 500ms
4. The response body corresponds to the schema
5. Response header "Content-Type" - "application/json"
6. Response header "Connection" - "keep-alive"


ID: PM-8

Name: Retrieve a list of companies with an invalid query parameter 'limit' (negative number)

Name request: test_companies_with_inv_query_limit

Step: Send a GET request to the endpoint /api/companies/ with the query parameter limit=-1

Checks:

1. The request was successfully sent
2. Status code 422
3. Server response time does not exceed 500ms
4. The response body corresponds to the schema
5. Response header "Content-Type" - "application/json"
6. Response header "Connection" - "keep-alive"


ID: PM-9

Name: Retrieve a list of companies with an invalid query parameter 'limit' (string)

Name request: test_companies_with_str_query_limit

Step: Send a GET request to the endpoint /api/companies/ with the query parameter limit=ABC

Checks:

1. The request was successfully sent
2. Status code 422
3. Server response time does not exceed 500ms
4. The response body corresponds to the schema
5. Response header "Content-Type" - "application/json"
6. Response header "Connection" - "keep-alive"


ID: PM-10

Name: Retrieve a list of companies with an invalid query parameter 'offset' (negative number)

Name request: test_companies_with_inv_query_offset

Step: Send a GET request to the endpoint /api/companies/ with the query parameter offset=-1

Checks:

1. The request was successfully sent
2. Status code 422
3. Server response time does not exceed 500ms
4. The list starts with a company with id=1
5. There are 3 companies in the list
6. The response body corresponds to the schema
7. Response header "Content-Type" - "application/json"
8. Response header "Connection" - "keep-alive"


ID: PM-11

Name: Retrieve a list of companies with an invalid query parameter 'offset' (string)

Name request: test_companies_with_str_query_offset

Step: Send a GET request to the endpoint /api/companies/ with the query parameter offset=ABC

Checks:

1. The request was successfully sent
2. Status code 422
3. Server response time does not exceed 500ms
4. The response body corresponds to the schema
5. Response header "Content-Type" - "application/json"
6. Response header "Connection" - "keep-alive"


ID: PM-12

Name: Retrieve information by company ID

Name request: test_company_by_id

Step: Send a GET request to the endpoint /api/companies/1 (with the path parameter company_id=1)

Checks:

1. The request was successfully sent
2. Status code 200
3. Server response time does not exceed 500ms
4. In the JSON, the company_id matches the URI id
5. The response body corresponds to the schema
6. Response header "Content-Type" - "application/json"
7. Response header "Connection" - "keep-alive"


ID: PM-13

Name: Retrieve a company using a non-existent ID

Name request: test_company_by_none_id

Step: Send a GET request to the endpoint /api/companies/8 (with the path parameter company_id = 8)

Checks:

1. The request was successfully sent
2. Status code 404
3. Server response time does not exceed 500ms
4. The response body corresponds to the schema
5. Response header "Content-Type" - "application/json"
6. Response header "Connection" - "keep-alive"


ID: PM-14

Name: Retrieve a company by ID with select the supported language

Name request: test_company_by_id_lang

Step: Send a GET request to the endpoint /api/companies/1 (with the path parameter company_id = 1) and headers 'Accept-Language' with the value RU (key: Accept-Language, value: RU)

Checks:

1. The request was successfully sent
2. Status code 200
3. Server response time does not exceed 500ms
4. In the JSON, the company_id matches the URI id
5. The response body corresponds to the schema
6. The language in the description matches the expected value - ru
7. Response header "Content-Type" - "application/json"
8. Response header "Connection" - "keep-alive"


ID: PM-15

Name: Retrieve a company by ID with the choice of an unsupported language

Name request: test_company_by_id_lang

Step: Send a GET request to the endpoint /api/companies/1 (with the path parameter company_id = 1) and headers 'Accept-Language' with the value AM (key: Accept-Language, value: AM)

Checks:

1. The request was successfully sent
2. Status code 200
3. Server response time does not exceed 500ms
4. In the JSON, the company_id matches the URI id
5. The response body corresponds to the schema
6. Response header "Content-Type" - "application/json"
7. Response header "Connection" - "keep-alive"


ID: PM-16

Name: Retrieve a list of users with query parameters 'limit' and 'offset'

Name request: test_users_with_limit_and_offset

Step: Send a GET request to the endpoint /api/users/ with the query parameters limit=10 and offset=5

Checks:

1. The request was successfully sent
2. Status code 200
3. Server response time does not exceed 500ms
4. The response body corresponds to the schema
5. There are 10 users in the 'data'
6. Response header "Content-Type" - "application/json"
7. Response header "Connection" - "keep-alive"


ID: PM-17 (gives an error on the status code - 200, expected - 422 and gives a complete list of users, the test is commented out)

Name: Retrieve a list of users with an invalid query parameter 'limit' (negative number)

Name request: test_users_with_inv_limit

Step: Send a GET request to the endpoint /api/users/ with the query parameter limit=-5

Checks:

1. The request was successfully sent
2. Status code 422
3. Server response time does not exceed 500ms
4. The response body corresponds to the schema
5. Response header "Content-Type" - "application/json"
6. Response header "Connection" - "keep-alive"


ID: PM-18

Name: Retrieve a list of users with invalid query parameters 'limit' (a string instead of a number)

Name request: test_users_with_str_limit

Step: Send a GET request to the endpoint /api/users/ with the query parameters limit=abc

Checks:

1. The request was successfully sent
2. Status code 422
3. Server response time does not exceed 500ms
4. The response body corresponds to the schema
5. Response header "Content-Type" - "application/json"
6. Response header "Connection" - "keep-alive"


ID: PM-19

Name: Retrieve a list of users using an unsecured http protocol

Name request: test_users_enable_ssl

Step: Send a GET request to the URL http://send-request.me/api/users

Checks:

1. Check that the request is sent via HTTP
2. Verify that the redirect status code is 301
3. Confirm that a redirect to HTTPS has occurred
4. Check the response header "Connection" - "keep-alive"
5. Check the response header "Content-Type" - "application/json"
6. Status code 200
7. Server response time does not exceed 500ms
8. The response body corresponds to the schema


ID: PM-20

Name: Creating, Modifying, and Deleting a User

Name request: test_user_created_update_delete

Step:

1. Send a POST request to the endpoint /api/users/ with the request body: "first_name": "Ivan", "last_name": "Smirnov", "company_id": 1.
2. Send a GET request to the endpoint /api/users/ with the user_id of the created user.
3. Send a PUT request to the endpoint /api/users/ with the request body: "first_name": "Ivan", "last_name": "Smirnov", "company_id": 1.
4. Send a GET request to the endpoint /api/users/ with the user_id of the created user.
5. Send a DELETE request to the endpoint /api/users/ with the user_id of the created user.
6. Send a GET request to the endpoint /api/users/ with the user_id of the created user.

Checks:


