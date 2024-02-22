
Feature: Authorize device endpoint
    As a consumer, I want an endpoint able to authorize devices

    Background:
        Given a request url "/api/v1/auth/device"

    Scenario: Authorize a device success
        When the request sends "GET"
        Then the response status is "HTTP_200_OK"
        And the response property "data.expiresIn" is equal to "600"
        And the response property "data.interval" is equal to "5"
        And the response property "data.userCode" matches regular expression "^\w\w\w\w-\w\w\w\w$"
        And the response property "data.deviceCode" matches regular expression "^[\w-]+$"
        And the response property "data.verificationURI" matches regular expression "^(http|https):\/\/([\w.-]+)(\.[\w.-]+)+([\/\w\.-]*)*\/?"
