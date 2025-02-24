<div align="center">
<h2> 📊 Design Considerations </h2>
</div>

### Design Constraints

#### Hardware Limitations
- **Minimum Requirements**: The rkc requires a minimum of 4 GiB of RAM. A stable network connection is essential for communicating with external APIs.

#### Operating System Requirements
- **Supported Platforms**: The code is written in Rust, which allows it to compile and run on all operating systems.

### SOUP (Software of Unknown Provenance) Usage

| **SOUP Component**       | **Version**        | **Scope**         | **Description**                                                  | **Risk Mitigation Strategy**                                     |
|---------------------------|--------------------|-------------------|------------------------------------------------------------------|------------------------------------------------------------------|
| sentry                   | 0.32.2             | Logging/Monitoring| Library for error tracking and performance monitoring            | Regular updates, secure configuration, adherence to best practices |
| flume                    | 0.11.0             | Messaging         | Library for inter-thread communication using message passing     | Regular updates, adherence to concurrency best practices         |
| futures                  | 0.3.30             | Async Operations  | Library for asynchronous programming in Rust                     | Regular updates, secure configuration                            |
| tokio                    | 1.36.0             | Async Runtime     | Asynchronous runtime for Rust with full features enabled         | Regular updates, secure configuration, adherence to async best practices |
| rdkafka                  | 0.36.2             | Messaging         | Library for Kafka client implementation with SSL support         | Regular updates, secure configuration, adherence to Kafka best practices |
| tokio-util               | 0.7.10             | Utilities         | Utilities for working with Tokio runtime                         | Regular updates, secure configuration                            |
| tracing                  | 0.1.40             | Logging           | Structured logging and diagnostics framework                     | Regular updates, adherence to logging best practices             |
| tracing-subscriber       | 0.3.18             | Logging           | Subscriber for processing and formatting tracing logs            | Regular updates, secure configuration                            |
| serde_derive             | 1.0.197            | Serialization     | Library for deriving serialization and deserialization traits    | Regular updates, adherence to serialization best practices       |
| uuid                     | 1.7.0              | Utility           | Library for generating and handling UUIDs with v4 feature        | Regular updates, adherence to secure random number generation    |
| chrono                   | 0.4.35             | Time Handling     | Library for date and time manipulation with Serde support        | Regular updates, adherence to time-handling best practices       |
| serde                    | 1.0.197            | Serialization     | Serialization and deserialization framework                      | Regular updates, adherence to serialization best practices       |
| serde_json               | 1.0                | JSON Handling     | Library for JSON serialization and deserialization               | Regular updates, secure configuration                            |
| reqwest                  | 0.11               | HTTP Client       | Library for making HTTP requests with JSON support               | Regular updates, adherence to secure HTTP communication practices |
| dotenvy                  | 0.15.7             | Configuration     | Library for loading environment variables from `.env` files      | Regular updates, adherence to secure configuration practices     |
| config                   | 0.14.0             | Configuration     | Library for handling configuration across multiple formats       | Regular updates, secure configuration                            |
| temp-env                 | 0.3.6              | Test              | Library for managing temporary environment variables during tests| Regular updates, adherence to secure testing practices           |
| test-case                | Latest             | Test              | Library for defining parameterized test cases                    | Regular updates, adherence to testing best practices             |