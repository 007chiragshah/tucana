# Component Design Description

The patient microservice architecture is defined using the following elements:

- **API**: Each entity has it's own api, thourgh which the web microservice communicates with it. This is defined using FastAPI endpoints and contain no business logic which is then redirected to the corresponding **service**. Their purpose is to sanitize the request input (done by the framework) and cache the responses on redis, which is done with an internal python library.
- **Service**: The service elements responsibility is for implementing the business logic of each endpoint, calling when necessary the **repositories** and **event streams** to retreive and insert data to the database.
- **Processors**: They are analogous to the services, but handle  the events received from the event bus (Kafka) instead of endpoints. Unlike the services, they are not defined as a class, but as a collection of subprocesses which contain the business logic for the events. Same as the services, they interact with the **repositories** and **event streams** to modify the data.
- **Repositories**: As they generally are, they are defined to interact directly with the database. They mostly contain methods to retreive information as the insertion and modification of items is handled by the **event streams**, but in rare cases they may modify elements that do not need to be broadcasted to the event bus.
- **Event streams**: They are used to create or modify objects on the database. Their purspose is to modify each elemement and then send a notification to the event bus with the changes made. They are define as a whole to ensure all modifications are notified for both audit purposes and so that the frontend knows when information should be updated.

Using the previous 5 components the full architecture is defined like so:

![C4 Patient components diagram](<../images/C4_diagram/C3 Patient.svg>)