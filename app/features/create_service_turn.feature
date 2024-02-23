
Feature: Create service turn
    As a consumer, I want an endpoint able to be able to create a service turn

    Background:
        Given a request url "/api/v1/services/1/serviceturns"

    Scenario: Create a service success
        Given a device and user code have been obtained for scope "write_serviceturns"
        And the device has been authorized
        And access token has been obtained
        And "VALID" request json payload
        When the request sends "POST"
        Then the response status is "HTTP_200_OK"


    Scenario: Create a service invalid data
        Given a device and user code have been obtained for scope "write_serviceturns"
        And the device has been authorized
        And access token has been obtained
        And "INVALID" request json payload
        When the request sends "POST"
        Then the response status is "HTTP_400_BAD_REQUEST"
        And the response property "code" is equal to "BAD_REQUEST"
        And the response property "type" is equal to "VALIDATION_ERROR"
        And the response property "message" is equal to "field required (body.customerName)"


    Scenario: List category services invalid token
        Given a device and user code have been obtained for scope "write_serviceturns"
        And the device has been authorized
        And access token has been obtained
        And access token is invalid
        And "VALID" request json payload
        When the request sends "POST"
        Then the response status is "HTTP_401_UNAUTHORIZED"


    Scenario: List category services unexpected scope
        Given a device and user code have been obtained for scope "read_serviceturns"
        And the device has been authorized
        And access token has been obtained
        And "VALID" request json payload
        When the request sends "POST"
        Then the response status is "HTTP_403_FORBIDDEN"
