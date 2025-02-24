<div align="center">
<h2> 🎯 Introduction </h2>
</div>

### Purpose

The purpose of the Software Design Document for the Web Gateway is to provide a comprehensive overview of the software architecture, design decisions, components, and interfaces of the Web Gateway. This document serves as a guide for developers, testers, and stakeholders in understanding the system's design and its role in managing communications between the Central Hub User Interface and the underlying platform microservices. 

The Web Gateway acts as a bridge to facilitate secure and efficient interaction with microservices responsible for patient management, bed management, group management, device handling, configuration management, and more. By providing REST API endpoints, the Web Gateway ensures seamless communication and data exchange across various system components. This document aims to support development, testing, integration, and maintenance of the Web Gateway to ensure consistent and reliable service delivery.

### Scope

The Web Gateway is designed to be the communication interface between the Central Hub User Interface (UI) and platform microservices. It ensures a smooth flow of data for core operations such as patient management, bed management, user authentication, device management, and configuration management. The system relies on the following core services:

- **Authentication**: Facilitates secure login, password management, and session management.
- **Patient**: Manages patient information.
- **Bed**: Oversees bed-related data (assignment, creation, deletion).
- **Bed Group**: Manages groups of beds, including assignment and updates.
- **Device**: Facilitates interaction with devices (monitor assignments, updates).
- **Audit Trail**: Retrieves the audit data.
- **Config**: Manage EHR integration configuration.

The Web Gateway is built to support the following features:

- Bidirectional communication between the UI and platform microservices.
- Secure, authenticated access to various resources.
- Real-time data retrieval and updates for patient, bed, device, and configuration management.
- Consistent communication between services to enable high-quality monitoring and control.
- System health checks to ensure continuous and reliable operation.

### System Overview

The Web Gateway is a software component that provides communication between the Central Hub User Interface and platform microservices. It acts as an intermediary, managing API requests for various services, including user authentication, patient information, bed assignments, group management, device management, configuration management, and audit trails.

Key operations within the Web Gateway include:

1. **Authentication**: Manages user login, token-based session handling, and password changes.
2. **Patient Management**: Facilitates operations for creating, updating, retrieving, and deleting patient data.
3. **Bed and Bed Group Management**: Manages information about individual beds, bed groups, and their assignment to specific patients or locations.
4. **Device Management**: Coordinates device assignments and manages device-related data such as normal vitals ranges and sensor details.
5. **Config Management**: Enables retrieval and updating of EHR integration configuration settings.
6. **System Health Monitoring**: Ensures the system is running properly and provides a "Healthy" status confirmation.

The Web Gateway ensures the following:

- **Efficient Data Transfer**: Enables secure and consistent data exchanges between the user interface and platform services.
- **Real-Time Updates**: Provides real-time updates for all resource states (patients, beds, devices, configurations).
- **Interoperability**: Ensures that various components within the system can communicate effectively, regardless of differences in underlying technologies.
- **Health Monitoring**: Provides a mechanism to verify system health.

### Definitions and Abbreviations

| Abbreviation          | Definition                                                                 |
|-----------------------|---------------------------------------------------------------------------|
| Web Gateway           | The communication interface between the Central Hub UI and platform microservices |
| CMS                   | Central Monitoring System (refers to the Central Hub User Interface)     |
| REST API              | Representational State Transfer Application Programming Interface        |
| EHR                   | Electronic Health Record                                                 |