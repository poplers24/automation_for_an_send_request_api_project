My practical automation project.

API documentation in swagger https://send-request.me/

Test-cases:

ID: PM-1

Name: Get company list

Name request: test_companies_default_request

Step: send GET request to endpoint /api/companies/

Checks:

1.1. The request was successfully sent.\
1.2. Status code 200.\
1.3. Server response time does not exceed 500ms.\
1.4. There are 3 companies in the "data" (by default).\
1.5. The response body corresponds to the schema.\
1.6. Response header "Content-Type" is "application/json."\
1.7. Response header "Connection" is "keep-alive."




