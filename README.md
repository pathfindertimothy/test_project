# Description
- This project contains two automation tests
    - One for automating taskwarrior tasks
    - The second is for automating API endpoints
- The test is based on python, pytest and taskwarrrior packages

### Folder structure
- `func_api`: This folder contains file which contains api functions to call for each test
- `func_tasks`: This folder contains file which contains taskwarrior function for each test
- `payload`: This folder contains file for the resquest payload
- `tests`: This folder contains files for test cases
- `tests`: This folder contains the test files to run
- `report`: This folder contains report in html format

## To set up the project locally

### The following packages needs to be present or installed before running the test locally
- python3
- pytest: `https://pypi.org/project/pytest/`
- python-dotenv: `https://pypi.org/project/python-dotenv/`
- taskwarriror: `https://taskwarrior.org/download/`
- pytest-html: `https://pypi.org/project/pytest-html/`

### To run tests
- Clone the project to your local system
- Install the packages listed above
- Navigate to the root folder and run: 
    - `pytest`
        - This will run all the test using pytest and display the total number of test passed
    - `pytest -v`
        - This will run all test using pytest and display all the test passed line by line
    - `pytest --html=report/report.html --self-contained-html`
        - This will run all test and generates an html report in the report folder

## Note: GitHub Actions
- A github action was set to run the tests in the pipeline automatically each time there is a push to the main branch
- To run the tests using this action manually, navigate to the repository
- Click on `Actions`at the top menu to navigate to the `All workflows` page
- Click on any of the workflow
- Click on `build`
- Click on `Re-run all jobs` or `Re-run this job` button to open the run panel
- Click on `Re-run jobs` to run the job
- Then click on `build` to view job statuses

## Future improvement
- Security testing sholud be performed to test the security of the endpoints
- Performance testing should be performed to test the resilience of the system
    - load testing
    - reliability testing
- Password and secrets should be stored in a .env file to be used during create, update and login user request
- Navigate test of endpoints should be performed
- Validation of response data structure should be performed
- Boundary values should be tested - all edge cases
- Test should be implemented in class for easy reuseability and sharing fixtures
- All API endpoints should be tested