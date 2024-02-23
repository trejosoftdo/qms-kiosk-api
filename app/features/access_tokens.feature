
Feature: Access tokens endpoint
    As a consumer, I want an endpoint able to get access tokens for devices

    Background:
      Given a device and user code have been obtained for scope "read_categories"
      And a request url "/api/v1/auth/tokens"


    Scenario: Get access tokens pending
        Given "VALID" request json payload
        When the request sends "POST"
        Then the response status is "HTTP_400_BAD_REQUEST"
        And the response property "code" is equal to "authorization_pending"
        And the response property "type" is equal to "VALIDATION_ERROR"
        And the response property "message" is equal to "The authorization request is still pending"


    Scenario: Get access tokens success
        Given the device has been authorized
        And "VALID" request json payload
        When the request sends "POST"
        Then the response status is "HTTP_200_OK"
        And the response property "data.expiresIn" is equal to "300"
        And the response property "data.refreshExpiresIn" matches regular expression "1\d\d\d"
        And the response property "data.accessToken" matches regular expression "^[a-zA-Z0-9_=]+\.[a-zA-Z0-9_=]+\.[a-zA-Z0-9_\-\+\/=]*"
        And the response property "data.refreshToken" matches regular expression "^[a-zA-Z0-9_=]+\.[a-zA-Z0-9_=]+\.[a-zA-Z0-9_\-\+\/=]*"


    Scenario: Get access tokens validation errors
        Given "INVALID" request json payload
        When the request sends "POST"
        Then the response status is "HTTP_400_BAD_REQUEST"
        And the response property "code" is equal to "BAD_REQUEST"
        And the response property "type" is equal to "VALIDATION_ERROR"
        And the response property "message" is equal to "field required (body.deviceCode)"
