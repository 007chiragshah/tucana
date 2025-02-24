# Authentication Microservice

## Security

The Authentication Microservice is responsible for managing user authentication and access control within the system. It provides secure mechanisms for user login, logout, password management, and privilege assignment. Designed with scalability and security in mind, this service ensures that only authorized users can access protected resources.

Key features include:

- User Login – Secure authentication using credentials or external identity providers.
- User Logout – Session termination to prevent unauthorized access.
- Password Management – Support for password changes and recovery mechanisms.
- User Privilege Management – Role-based access control (RBAC) to define user permissions.
- Token-based Authentication – Implementation of JWT for secure access.

This microservice serves as the foundation for enforcing security policies across the system, ensuring that user authentication and authorization are handled efficiently and securely.

## Configuration

Since the authentication microservice does not have a constant demand and primarily consumes CPU when used, it was decided to leverage its resources to also handle the registration of configuration variables. This is essentially a key-value store that other services can query to retrieve configuration values dynamically, allowing us to configure other services (e.g., Mirth) on the fly.

Key features include:

- Create config variable – Adds a key/value configuration variable that can be retrieved by other services.
- List config variables – Lists the existing configuration variables.