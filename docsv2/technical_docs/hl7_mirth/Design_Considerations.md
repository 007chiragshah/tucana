<div align="center">
<h1>HL7 & Mirth Gateway</h1>
<h2> 📈 Design Considerations </h2>
</div>

### Design Constraints

#### Hardware Limitations
- **Minimum Requirements**: The solution requires a minimum of 4 GiB of RAM. Additionally, a network port is necessary to communicate with the healthcare provider's EHR system.

#### Operating System Requirements
- **Cross-Platform Compatibility**: Mirth utilizes the TCP protocol, enabling it to operate seamlessly across different platforms.

#### Security Constraints
- **HIPAA Compliance**:  While Mirth Connect or HL7 itself is not inherently HIPAA-compliant, it provides the tools necessary to create HIPAA-compliant workflows.It is not a software or system but a framework. Whether an implementation of HL7 is HIPAA-compliant depends on the safeguards employed during data exchange


### Data Management

- **Patient**: Patient micro service is one of the component in Central Server which is responsible for to transform Patient & Device data including Alerts to the underlying services. Here Patient service is calling mirth endpoint to get the patient data from healthcare provider's EHR
- **Kafka**: Stream patient's vital data to Mirth connect from the following microservices as output data for healthcare provider's EHR system.

###  SOUP (Software of Unknown Provenance) Usage

| **SOUP Component**                     | **Version**        | **Description**                                                  | 
|----------------------------------------|--------------------|--------------|
| Mirth Connect                     | 4.5.0              | NexGen Healthcare tool which supports HL7 & FHIR standarad                              | 


