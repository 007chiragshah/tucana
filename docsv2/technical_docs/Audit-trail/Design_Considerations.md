<div align="center">
<h1>Audit Trail</h1>
<h2> 📈 Design Considerations </h2>
</div>

### Design Constraints

#### Hardware Limitations
- **Minimum Requirements**: The solution requires a minimum of 256 Mib of RAM and 100m CPU as this microservice runs on the k8s container we can scale up or down based on the usage of the system currently Central Server infra is only running 1 instance of Audit Trail service.

#### Operating System Requirements
- **Cross-Platform Compatibility**: The code is written in python, which allows it to compile and run on all operating systems. For a cluster instance central server hosted container is running on Linux os 3.11.9-bookworm docker image. 

#### Performance Requirements
- **Data Latency**: Given that this microservice is for logging perpose data latency will not be a concerned here as all the messages are stored in queue untill it's get consumed.


#### Security Constraints
- **Authentication**: Only authorized user will be able to access the audit trail Apis to get the logs based on entity id.


### Data Management

- **PostgreSQL**: All the events are stored in PostgreSQL for audit purpose to provide forensic evidance of each important event.  
- **Kafka**: Stream patient data, vital information, physiological alerts, technical alerts, Authentication infromation, session details and all critical events to the following microservices.

###  SOUP (Software of Unknown Provenance) Usage

| **SOUP Component**             | **Version**       | **Scope** | **Description**                                      | **Risk Mitigation Strategy**                            |
|--------------------------------|-------------------|-----------|-----------------------------------------------------|--------------------------------------------------------|
| ruff                           | ^0.4.9           | Linter    | A fast Python linter for code analysis             | Regular updates to ensure compliance with standards    |
| factory-boy                    | ^3.3.0           | Testing   | Factory patterns for test data generation          | Keep up-to-date to avoid compatibility issues          |
| pytest-asyncio                 | ^0.21.1          | Testing   | Support for asyncio in pytest                      | Regular updates to maintain compatibility              |
| pytest-mock                    | ^3.10.0          | Testing   | Mocking support in pytest                          | Ensure proper mocking and testing coverage             |
| behave                         | ^1.2.6           | Testing   | Behavior-driven development framework              | Update regularly for compatibility and bug fixes       |
| pytest                         | ^7.1.3           | Testing   | Testing framework for Python                       | Regular updates for new features and bug fixes         |
| respx                          | ^0.20.0          | Testing   | Mock HTTPX responses                               | Maintain to ensure accurate testing                    |
| coverage                       | ^7.1.0           | Testing   | Code coverage measurement                          | Regular updates to ensure accurate reporting           |
| pylint                         | ^2.15.4          | Linter    | Code analysis tool                                 | Stay updated for improved analysis                     |
| reformat-gherkin               | ^3.0.1           | Tooling   | Reformatter for Gherkin syntax                    | Keep updated to ensure Gherkin syntax consistency      |
| exceptiongroup                 | ^1.0.0-rc.9      | Utility   | Exception grouping utility for Python             | Monitor for updates to avoid bugs                      |
| isort                          | ^5.10.1          | Linter    | Sorts Python imports                              | Regular updates to adhere to import style guidelines   |
| flake8                         | ^6.0.0           | Linter    | Python style guide enforcement                    | Regular updates to enforce coding standards            |
| flake8-simplify                | ^0.19.3          | Linter    | Plugin for Flake8 to simplify Python code         | Keep updated for better suggestions                   |
| flake8-comprehensions          | ^3.10.0          | Linter    | Plugin for Flake8 to enhance comprehension usage  | Regular updates to improve code readability            |
| freezegun                      | ^1.2.2           | Testing   | Mock the passage of time                          | Regular updates for accurate time-related testing      |