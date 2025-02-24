<div align="center">
<h1>Audit Trail</h1>
<h2> 🎯 Introduction </h2>
</div>


### Purpose
	
1.	**Regulatory Compliance**:

Meet healthcare regulations like HIPAA (Health Insurance Portability and Accountability Act), GDPR (General Data Protection Regulation), or FDA 21 CFR Part 11 & FDA Cybersecurity in Medical Devices Apendix 1 Section F Event Detection and Logging, which mandate audit trails for sensitive data.

2.	**Data Integrity**:

Maintain a reliable record of who accessed or modified what data and when, ensuring the authenticity and integrity of patient data.

3.	**Security & Accountability**:

Detect and prevent unauthorized access or changes to critical data by keeping track of user actions and system events.

4.	**Forensics & Debugging**:

Facilitate root cause analysis during system failures or data breaches.

5.	**Transparency**:

Build trust among Client by providing a clear, auditable history of system activities.

--
### Scope
Scope

1.	Data Tracking:

Record all create, read, update, delete (CRUD) operations performed on patient data, vital information, Device data, access usage information etc.

2.	User Actions:

Track user logins, logouts, failed login attempts, and role-based access usage, Session Information, Configuration changes, event details.

3.	Service Events:

Log service-level activities such as service restarts, Service failuer using healthcheck, and API usage.



### System Overview

The Audit Trail Microservice is a critical component designed to consume and store data from other microservices, including the Patient Microservice, Device Microservice, and Authentication Microservice. It achieves this by subscribing to events published to Apache Kafka, processing them, and storing event-based data in a PostgreSQL database. Additionally, the service provides an HTTP API endpoint built using the FastAPI framework for retrieving the stored audit trail logs.
Key Responsibilities
* Event Consumption: Listen to event topics in Apache Kafka published by other microservices.
* Data Persistence: Store events in the PostgreSQL database, documenting a chronological sequence of system events.
* Error Handling: Log errors encountered during message handling for analysis while ensuring continued processing of subsequent messages.
* API Access: Provide an HTTP API for retrieving audit trail logs.

An Audit Trail Microservice is an independent, scalable module designed to track and log system and user activities in a Central Server ecosystem.

Core Components:

1.	Secure Storage:

Stores logs in secure data store where it can't be tempared for the Central Sever audit logs are store in PostgresSQL.

2.	Event Streaming:

Central Server Leverages kafka message queues to process and forward events to the storage system.

3.	Monitoring Dashboard:

Offers an interface for authorized users to query and analyze audit trails in real time (i.e Api call , Monitoring tool access).

4.	APIs for Integration:
Central Server Provides RESTful APIs to integrate with other systems for seamless logging.




