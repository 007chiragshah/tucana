<div align="center">
<h1>SDC Gateway</h1>
<h2> 📈 Design Considerations </h2>
</div>

### Design Constraints

#### Hardware Limitations
- **Minimum Requirements**: The solution requires a minimum of 4 GiB of RAM. Additionally, a network port is necessary to communicate with the patient monitor.

#### Operating System Requirements
- **Cross-Platform Compatibility**: The code is written in Java, which allows it to compile and run on all operating systems.

#### Performance Requirements
- **Network MTU**: The minimum MTU range for the network should be 1000 or higher.
- **Data Latency**: Given that this solution is for medical systems, data latency should not exceed 1 second.
- **Quality of Service (QoS)**: The hospital network should implement QoS to prioritize SDC messages.

#### Security Constraints
- **Compliance**: The implementation is compliant with the IEEE 11073 SDC standard and the IEC 62304 standard.
- **HIPAA Compliance**: The SDC Gateway must be HIPAA compliant, and data encryption at rest is mandatory.


### Data Management

- **Redis**: The dissemination of patient monitor devices to the follower instances takes place via Redis using its publish-subscribe (PUB/SUB).
- **Kafka**: Stream patient data, vital information, physiological alerts, technical alerts, and all critical events to the following microservices as input data for UI representation.

###  SOUP (Software of Unknown Provenance) Usage

| **SOUP Component**                     | **Version**        | **Scope**    | **Description**                                                  | **Risk Mitigation Strategy**                                     |
|----------------------------------------|--------------------|--------------|-------------------------------------------------------------------|------------------------------------------------------------------|
| org.somda.sdc:glue                     | 4.0.0              |              | Glue code for SDC integration                                     | Regular updates, adherence to SDC standards                      |
| org.bouncycastle:bcprov-jdk18on       | 1.78.1             |              | Bouncy Castle Provider for JDK 1.8                               | Regular updates, secure configuration                            |
| org.apache.logging.log4j:log4j-core    | 2.19.0             |              | Log4j core library for logging                                   | Regular updates, secure configuration, logging best practices    |
| commons-cli:commons-cli                | 1.4                |              | Apache Commons CLI library for command-line argument parsing     | Regular updates, secure configuration                            |
| io.reactivex.rxjava3:rxjava            | 3.0.4              |              | Reactive Extensions for the JVM                                  | Regular updates, adherence to reactive programming best practices |
| org.slf4j:slf4j-reload4j               | 2.0.9              | test         | SLF4J binding for Reload4j                                        | Regular updates, secure configuration                            |
| io.lettuce:lettuce-core                | 6.2.7.RELEASE      |              | Advanced Redis client for thread-safe sync, async, and reactive usage | Regular updates, secure configuration                            |
| org.apache.kafka:kafka-clients         | 3.7.1              |              | Apache Kafka client library                                      | Regular updates, secure configuration, monitoring                |
| com.google.code.gson:gson              | 2.10.1             |              | Google Gson library for JSON serialization and deserialization   | Regular updates, secure configuration                            |
| com.google.inject:guice               | 6.0.0              |              | Google Guice library for dependency injection                     | Regular updates, secure configuration                            |
| org.slf4j:slf4j-simple                 | 2.0.9              |              | Simple implementation of SLF4J                                    | Regular updates, secure configuration                            |
| com.google.guava:guava                 | 32.0.1-jre         |              | Google Guava library for Java core libraries                     | Regular updates, secure configuration                            |
| org.eclipse.jetty:jetty-util           | 12.0.12            |              | Eclipse Jetty utility classes                                    | Regular updates, secure configuration                            |
| org.eclipse.jetty:jetty-server         | 12.0.12            |              | Eclipse Jetty server component                                   | Regular updates, secure configuration                            |
| org.eclipse.jetty:jetty-http           | 12.0.12            |              | Eclipse Jetty HTTP component                                     | Regular updates, secure configuration                            |
| org.junit.jupiter:junit-jupiter        | 5.10.0             | test         | JUnit 5 testing framework                                        | Regular updates, secure configuration, testing best practices    |
| org.mockito:mockito-core               | 5.6.0              | test         | Mockito core library for mocking in tests                        | Regular updates, secure configuration, testing best practices    |
| com.auth0:java-jwt                     | 4.4.0              |              | Java library for JSON Web Tokens (JWTs)                         | Regular updates, secure configuration                            |

