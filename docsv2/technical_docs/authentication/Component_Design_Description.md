# Component Design Description

The authentication microservice architecture is defined using the following elements:

- **Views**: Each entity has it's own view, thourgh which the web microservice communicates with it. This is defined using DRF endpoints and contain no business logic which is then redirected to the corresponding **serializer**. Their purpose is to sanitize the request input (done by the framework) and cache the responses on redis, which is done with an internal python library.
- **Serializers**: The serializer elements responsibility is for implementing the business logic of each endpoint, calling when necessary the **models** and **event streams** to retreive and insert data to the database. Serializers convert complex data types like Django model instances into JSON for API responses and vice versa for data validation in incoming requests. They ensure data consistency, enforce validation rules, and simplify API interactions.
- **Models**: As they generally are, they are defined to interact directly with the database. Models define the structure and behavior of the data used by the service. They represent database tables and provide an abstraction layer for data manipulation through Django's ORM (Object-Relational Mapping).
- **Event streams**: They are used to create or modify objects on the database. Unlike FastAPI, Django lacks flexibility in implementing event streams to handle object modifications directly. As a workaround, Django signals were used, as they are emitted whenever an object is modified.

Using the previous 4 components the full architecture is defined like so:

![C4 Authentication components diagram](<../images/C4_diagram/C3 Authentication.svg>)