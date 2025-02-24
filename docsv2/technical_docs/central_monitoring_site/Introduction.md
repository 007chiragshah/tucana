<div align="center">
<h1>Central Monitoring Site</h1>
<h2> 🎯 Introduction </h2>
</div>

### Purpose

The purpose of the Software Design Document for the Central Monitoring Site is to provide a detailed description of the system’s software architecture, design decisions, components, and interfaces. This document ensures clarity in the implementation of the Central Monitoring Site, which serves as a centralized web interface to monitor multiple patients. It communicates with the Central Server to obtain realtime and historical information for the current patient sessions being monitored. The document also aims to support developers, testers, and stakeholders in understanding the system’s design to facilitate development, testing, integration, and maintenance.

### Scope

The Central Monitoring Site (CMS) acts as a centralized web application to monitor patients vitals and receive alerts of their current condition and from the sensors status. CMS is built as a Next.JS React app using Typescript following standard secure protocols and relies on the following core libraries

- Material UI: Provides UI components for easily maintainable and customizable interfaces
- SciChart: Displays graphs for realtime metrics
- Axios: Provides communication functionalities to securely connect to Web Gateway API endpoints

The scope of the Central Monitoring Site includes:

- Monitor multiple patient realtime vitals with information provided from a diverse pool of possible sensors
- Alert the medical staff of alerts for both vitals and sensors in realtime as triggered from the Patient Monitor
- Manage display groups and beds to organize which patients are displayed and what information is seen
- Allow a easy access for technical users for EHR integration
- Submit a new patient session for a Patient Monitor that is connected but without a current session

### Definitions and Abbreviations

| Abbreviation   | Definition                              |
| -------------- | --------------------------------------- |
| CMS            | Central Monitoring Site Web Application |
| PM             | Patient Monitor                         |
| Central Server | Central Monitoring System               |
