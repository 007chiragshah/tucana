<div align="center">
<h2> 📊 Design Considerations </h2>
</div>

### Design Constraints

#### Hardware Limitations
- **Minimum Requirements**: The test tools requires a minimum of 4 GiB of RAM. A stable network connection is essential for communicating with external APIs.

#### Operating System Requirements
- **Supported Platforms**: The code is written in Python, which allows it to compile and run on all operating systems.

### SOUP (Software of Unknown Provenance) Usage

| **SOUP Component**       | **Version**        | **Scope**         | **Description**                                                      | **Risk Mitigation Strategy**                                                          |
|--------------------------|--------------------|-------------------|----------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| **pytest**               | 7.4.0              | Test              | General-purpose test framework for Python                            | Regular updates, secure configuration, and adherence to testing best practices.       |
| **coverage**             | 7.2.7              | Test              | Tool to measure code coverage during tests                           | Regular updates, secure configuration, and effective use of coverage reports.         |
| **ruff**                 | 0.4.9              | Linting           | Linter and formatter for Python code                                 | Regular updates and adherence to coding and linting standards.                        |
| **reformat-gherkin**     | 3.0.1              | Test              | Reformatter for Gherkin syntax used in BDD                           | Regular updates, secure configuration, testing best practices                         |
| **pylint**               | 2.17.4             | Linting           | Python static code analysis tool for enforcing coding standards      | Regular updates, strict adherence to coding standards, and code quality improvements. |
| **behave**               | 1.2.6              | Test              | Framework for behavior-driven development (BDD)                      | Regular updates, secure configuration                                                 |
| **pytest-mock**          | 3.12.0             | Test              | Plugin for integrating Mock library into Pytest for mocking          | Regular updates, secure configuration, and adherence to testing best practices.       |