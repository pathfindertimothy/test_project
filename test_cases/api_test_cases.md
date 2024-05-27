# Test scenarios

## API test scenarios
- As a user, if I perform a get request for a product that is not present, I should get an error message that the resource is not present
    - `Given`: I have the required GET request endpoint
    - `And`: I have the required product ID parameter
    - `When`: The request is performed
    - `Then`: The response payload should contain an error message that the resource is not present
- As a user, if I perform a get request for a product or resource that is not present, I should get an error status code of 404 (resource not found) that the resource is not present
    - `Given`: I have the required GET request endpoint
    - `And`: I have the product ID parameter that is not present
    - `When`: The request is performed
    - `Then`: The response payload should contain an error status code of 404
    - `And`: The response payload should contain an error message that the resouce is not present
- As a user, if I perform a request for a product or group of products, I shoud get a response with a time between 200 milliseconds and 1 second
     - `Given`: I have the required GET request endpoint
    - `And`: I have the product ID parameter or necessary parameter
    - `When`: The request is performed
    - `Then`: The response payload with a status of 200 OK
    - `And`: The response time should be between 200 milliseconds and 1 second
- As a user, if I perform a get request for a product with an invalid authentication credentials, I should get an error message with a status code of 401 (Unauthorised)
     - `Given`: I have the required GET request endpoint and product ID Parameter
    - `And`: I have an invalid authentication credentials
    - `When`: The request is performed
    - `Then`: The response should contain an error status code value of 401 (unathorised)
- As a user, if I perform a create product request with an invalid parameter, I should get an error message
     - `Given`: I have the required CREATE request endpoint
    - `And`: I have an invalid request payload parameter
    - `When`: The request is performed
    - `Then`: The response message should contain a clear error message
- As a user, If I perform a create product request with a missing parameter that is required, I should get an error message
     - `Given`: I have the required CREATE request endpoint
    - `And`: I have missing parameters in the request payload
    - `When`: The request is performed
    - `Then`: The response message should contain a clear error message
- As a user, if I perform a create product request with with one of the parameter having a long string more than what the request can handle, I should get an error message
     - `Given`: I have the required CREATE request endpoint
    - `And`: I have missing a long string value in one of the parameter
    - `When`: The request is performed
    - `Then`: The response message should contain a clear error message
- As a user, if I perform a get request for a product, I should get the correct schema or structure in the response payload
    - `Given`: I have the required GET request endpoint
    - `And`: I have the required product ID parameter
    - `When`: The request is performed
    - `Then`: The response payload should contain the correct schema structure
- As a user, if I want to be able to perform delete operation on a product
    - `Given`: I have the required DELETE request endpoint
    - `And`: I have the required product ID parameter
    - `When`: The request is performed
    - `Then`: The response message should contain a message that the product is deleted successfull

- Some other test scenarios
    - As an an admin, I want to be able to create a user
    - As a user, if I login with the wrong credentials, I should get an error
    - As a user, I want to be able to test product filters
    - As an admin, I want to be able to delete a user
    - As a admin, I want to be able to sort and filter users
    - As a user, I want to be able to add a new cart
    - As a user, I want to be able to delete a cart
    - As a user, I want to be able to sort carts
    - As a user, I want to be able to get carts in a specific date range

# Recommendation
- Security testing sholud be performed to test the security of the endpoints
- performance testing should be performed to test the resilience of the system
    - load testing
    - reliability testing
- Password should be stored in env file during create, update and login user request
- All API endpoints should be tested
- See README file for listed recommendation

    