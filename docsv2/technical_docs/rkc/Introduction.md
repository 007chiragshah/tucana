<div align="center">
<h2> 🎯 Introduction </h2>
</div>

### Purpose

The purpose of this document is to provide a comprehensive overview of the RKC Platform and its integration with Kafka and Mirth Connect for managing and processing vital patient data. This document outlines the system's architecture, design decisions, components, and workflows, serving as a guide for developers, testers, and stakeholders. The RKC Platform acts as a central hub for consuming, processing, and forwarding vital data to external systems like Mirth Connect, ensuring seamless integration with Electronic Health Records (EHRs). By detailing the system's design and functionality, this document aims to support development, testing, integration, and maintenance, ensuring reliable and efficient service delivery.

### Scope
The RKC Platform is designed to consume vital data from Kafka, process it, and forward it to Mirth Connect for EHR integration. The system handles real-time vital data with ensuring accurate and timely delivery to systems. Key functionalities include:

- **Data Consumption**: Consuming vital data from Kafka  vitals topics.
- **Data Forwarding**: Periodically sending processed data to Mirth Connect via API endpoints.
- **Error Handling**: Managing errors and ensuring system health and logging mechanisms.

### Definitions and Abbreviations

| Abbreviation          | Definition                                                                |
|-----------------------|---------------------------------------------------------------------------|
| Kafka                 | A distributed platform for real-time event streaming and data handling.   |
| CMS                   | Central Monitoring System (refers to the Central Hub User Interface).     |
| Mirth                 | Integration engine for exchanging healthcare data with EHR (e.g. HL7).    |
| EHR                   | Electronic Health Record                                                  |
