<div align="center">
<h2>⚜️ Component Design Description</h2>
</div>

### **High Level System Architecture**

The healthcheck system architecture ensures the continuous monitoring and reliability of services by integrating a Healthcheck Service. The Healthcheck Service sends periodic "PING" messages through Kafka, which are monitored by a Consumer that listens for responses. The system employs a Watchdog to track message timestamps and quickly identify delays or failures, triggering automatic recovery processes like retries and connection restarts.

### **Class Daigram**

![Health Check Class Daigram](<Diagrams/Images/ClassDiagram.png>)

### **Flow Architecture**

![Health Check Flow Architecture](<Diagrams/Images/FlowDiagram.png>)

---

### **Environment Configuration**

The following .env file contains the necessary environment settings for development and deployment.
```
ENVIRONMENT=
KAFKA_HOST=
KAFKA_PORT=
KAFKA_PASSWORD=
KAFKA_CA_FILE_PATH=
KAFKA_CERT_FILE_PATH=
KAFKA_KEY_FILE_PATH=
KAFKA_HEALTHCHECK_TOPIC=
```