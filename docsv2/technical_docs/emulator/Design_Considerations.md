<div align="center">
<h2> 📊 Design Considerations </h2>
</div>

### Design Constraints

#### Hardware Limitations
- **Minimum Requirements**: The emultor requires a minimum of 4 GiB of RAM. A stable network connection is essential for communicating with external APIs.

#### Operating System Requirements
- **Supported Platforms**: The code is written in Python, which allows it to compile and run on all operating systems.

### SOUP (Software of Unknown Provenance) Usage

| **SOUP Component**      | **Version** | **Scope**            | **Description**                                                | **Risk Mitigation Strategy**                                     |
|-------------------------|-------------|----------------------|----------------------------------------------------------------|------------------------------------------------------------------|
| httpx                   | 0.23.0      | HTTP Client          | Library for making HTTP requests, supports async and sync      | Regular updates, adherence to secure HTTP communication          |
| loguru                  | 0.7.0       | Logging              | Simple and powerful logging library for Python                 | Regular updates, adherence to logging                            |
| aiokafka                | 0.8.0       | Messaging            | Asynchronous Kafka client for Python                           | Regular updates, secure configuration, adherence to Kafka        |
| scipy                   | 1.10.1      | Scientific Computing | Library for scientific and numerical computations              | Regular updates, secure configuration, validation of data inputs |
| pooch                   | 1.7.0       | Data Management      | Library for managing downloads of data files                   | Regular updates, adherence to secure data handling               |
| fastapi                 | 0.95.1      | Web Framework        | High-performance web framework for building APIs               | Regular updates, adherence to API security                       |
| gunicorn                | 20.1.0      | Web Server           | WSGI HTTP Server for running Python web applications           | Regular updates, secure deployment                               |
| uvicorn                 | 0.22.0      | ASGI Server          | Lightning-fast ASGI server for running async web apps          | Regular updates, secure configuration                            |
| faker                   | 18.9.0      | Testing/Data Gen     | Library for generating fake data for testing                   | Regular updates, secure data generation                          |
| orjson                  | 3.9.1       | JSON Handling        | Fast JSON parser and serializer                                | Regular updates, adherence to JSON handling                      |
| more-itertools          | 9.1.0       | Utilities            | Advanced collection of iterable utilities                      | Regular updates, secure coding                                   |
| python-dotenv           | 1.0.0       | Configuration        | Library for managing environment variables from .env files     | Regular updates, adherence to secure configuration               |
| cryptography            | 43.0.1      | Security             | Library for cryptographic operations                           | Regular updates, adherence to secure encryption                  |
| hl7                     | 0.4.5       | HL7 Processing       | Library for parsing and handling HL7 messages                  | Regular updates, adherence to HL7 message handling               |
| pytest-mock             | 3.10.0      | Testing              | Plugin for mocking in pytest                                   | Regular updates, adherence to secure testing                     |
| behave                  | 1.2.6       | Testing              | Behavior-driven development testing framework                  | Regular updates, adherence to testing                            |
| pytest                  | 7.1.3       | Testing              | Testing framework for unit and functional testing              | Regular updates, adherence to secure testing                     |
| respx                   | 0.20.0      | Testing/Mocking      | HTTP mock library for testing requests made via httpx          | Regular updates, adherence to testing                            |
| coverage                | 7.2.2       | Code Coverage        | Code coverage measurement tool                                 | Regular updates, adherence to testing and code quality           |
| pylint                  | 2.15.4      | Linting              | Static code analysis tool                                      | Regular updates, adherence to Python coding                      |
| reformat-gherkin        | 3.0.1       | Formatting           | Formatter for Gherkin feature files                            | Regular updates, adherence to consistent formatting              |
| exceptiongroup          | 1.0.0-rc.9  | Error Handling       | Exception handling utilities                                   | Regular updates, secure error handling                           |
| isort                   | 5.10.1      | Import Management    | Sorting and organizing imports                                 | Regular updates, adherence to consistent import                  |
| flake8                  | 6.0.0       | Linting              | Linter for Python code                                         | Regular updates, adherence to Python coding                      |
| flake8-simplify         | 0.19.3      | Linting              | Plugin for simplifying Python code using Flake8                | Regular updates, adherence to coding                             |
| flake8-comprehensions   | 3.10.0      | Linting              | Plugin for detecting unnecessary comprehensions                | Regular updates, adherence to coding                             |
| pytest-asyncio          | 0.21.0      | Testing              | Async testing support for pytest                               | Regular updates, adherence to async testing                      |
| freezegun               | 1.2.2       | Testing              | Mock datetime for testing                                      | Regular updates, adherence to secure testing                     |
| ipdb                    | 0.13.11     | Debugging            | Interactive debugging tool for Python                          | Regular updates, adherence to secure debugging                   |
| polyfactory             | 2.9.0       | Test Data Gen        | Library for generating test data using Pydantic models         | Regular updates, adherence to testing                            |
| ruff                    | 0.5.0       | Linting              | Fast Python linter                                             | Regular updates, adherence to Python coding                      |