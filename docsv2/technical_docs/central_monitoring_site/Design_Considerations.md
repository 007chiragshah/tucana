<div align="center">
<h1>Central Monitoring Site</h1>
<h2> 📈 Design Considerations </h2>
</div>

### Design Constraints

#### Hardware Limitations

- **Minimum Requirements**: The solution requires at least one 24 inches diagonal size display, running with a resolution of 1920x1080. It also requires a mouse and keyboard for interactibility, and run in a chrome/chromium browser.

#### Operating System Requirements

- **Cross-Platform Compatibility**: The code is written in Javascript/Typescript, which allows it to compile and run on all operating systems.

#### Performance Requirements

- **Network MTU**: The minimum MTU range for the network should be 1000 or higher.
- **Data Latency**: Given that this solution is for medical systems, data latency should not exceed 1 second.

#### Security Constraints

- **Compliance**: The implementation is compliant with the applicable requirements specified in IEC 62366-1:2020 standard
- **HIPAA Compliance**: The implementation must be HIPAA compliant.

### Data Management

- **HTTPS**: Non-realtime data such as patient information, beds data, and group management shall be only communicated through secure channels on a secure HTTPS connection with validated hosts.
- **WSS**: realtime data such as vitals and alerts shall only be communicated through secure channels on a secure WSS connection with a validated host.

### SOUP (Software of Unknown Provenance) Usage

| **SOUP Component**    | **Version**     | **Scope** | **Description**                                                       | **Risk Mitigation Strategy**                                      |
| --------------------- | --------------- | --------- | --------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Javascript            | ECMAScript 2015 |           | Programming language for web applications                             | Secure configuration and best programming practices               |
| Typescript            | 5.0.4           |           | Programming Language for typed web applications (based on Javascript) | Secure configuration and best programming practices               |
| React                 | 18.2.0          |           | Library for web user interfaces                                       | Regular updates, secure configuration                             |
| Node.JS               | 18.20.4         |           | Runtime Environment for Javascript Web Applications                   | Regular updates, secure configuration, best programming practices |
| Next.JS               | 14.2.15         |           | Web framework for web applications                                    | Regular updates, secure configuration, best programming practices |
| Material UI           | 5.15.14         |           | Component Library for React Projects                                  | Regular updates, secure configuration                             |
| Material UI X         | 7.21.0          |           | Component Library for React Projects                                  | Regular updates, secure configuration                             |
| Moment                | 2.30.1          |           | Library for accurate date and time transformations                    | Regular updates, secure configuration                             |
| Moment-Timezone       | 0.5.43          |           | Library for accurate timezone transformations                         | Regular updates, secure configuration                             |
| UUID (JS)             | 9.0.0           |           | Library for generating unique identifiers                             | Regular updates, secure configuration                             |
| Axios                 | 1.7.4           |           | Library for managing API communications                               | Regular updates, secure configuration                             |
| Formik                | 2.2.9           |           | Library for form construction and handling                            | Regular updates, secure configuration                             |
| Emotion               | 11.10.6         |           | Library for UI styling                                                | Regular updates, secure configuration                             |
| React Query           | 4.35.0          |           | Library for managing queries and mutations for API data               | Regular updates, secure configuration                             |
| SciChart              | 3.1.329         |           | Library for displaying realtime, high volume graphs                   | Regular updates, secure configuration                             |
| React-i18next         | 15.0.2          |           | Library for internationalization                                      | Regular updates, secure configuration                             |
| Storybook             | 7.5.2           | test      | Frontend workshop for UI development and testing                      | Secure configuration, testing best practices                      |
| React Testing Library | 13.2.0          | test      | React testing framework                                               | Secure configuration, testing best practices                      |
