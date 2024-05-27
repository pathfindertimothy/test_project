# Description
- This project contains two automation tests
    - One for automating taskwarrior tasks
    - The second is for automating API endpoints
- The test is based on python, pytest and taskwarrrior packages

## Project set up locally

### Folder structure
- `func_api`: This folder contains file which contains api functions to call for each test
- `func_tasks`: This folder contains file which contains taskwarrior function for each test
- `payload`: This folder contains file for the resquest payload
- `tests`: This folder contains files for test cases
- `tests`: This folder contains the test files to run

### The following packages needs to be present or installed before runing the test locally
- python3
- pytest: `https://pypi.org/project/pytest/`
- python-dotenv: `https://pypi.org/project/python-dotenv/`
- taskwarriror: `https://taskwarrior.org/download/`

### To run tests
- Clone the project to your local system
- Install the packages listed above
- Navigate to the root folder and run: 
    - `pytest`
        - This will run all the test using pytest and display the total number of test passed
    - `pytest -v`
        - This will run all test using pytest and displayed all the test passed line by line

## Future improvement
- Security testing sholud be performed to test the security of the endpoints
- Performance testing should be performed to test the resilience of the system
    - load testing
    - reliability testing
- Password should be stored in env file during create, update and login user request
- Navigate test of endpoints should be performed
- Validation of response data structure should be performed
- Boundary values should be tested
- Test should be implemented in class for easy reuseability and sharing fixtures