# Component Design Description

The realtime microservice purpose is to handle all realtime events sent by either the Patient Monitors connected, or by the backend microservices.

Here is a simplified C4 Container diagram showing how the realtime microservice interacts with the rest of the system:

![C4 Realtime - Container simplified](<../images/C4_diagram/C4 Realtime - Container diagram symplification.svg>)

As it can be seen on the image, the realtime microservice works as a proxy between the internal Event Bus, which handles all events, and any client connected to it, which can be the Central Server frontend or any external client. 

Internally the realtime microservice architecture is as follows:

![C4 Realtime - Component](<../images/C4_diagram/C3 Realtime.svg>)

As it can be seen on the diagram the realtime architecture uses very few components, which is necessary to reduce the overhead of handling the messages to a minimum so that the delays between a message being sent and being displayed to the user is as small as possible. 

The Vitals Consumer compponent is responsible for handling all new open connections originating from the frontend web service or any other client connected to the Central Server. It is also responsible of handling the configuration messages comming from the client, which in turn determine the filtering of the messages that are being sent back.

The Connection Manager is the responsible for receiving the messages from the event bus and redirecting them to all open connections that match the filtering criteria.

The Metrics Cache Service is responsible for storing the latest vital messages received for each patient and each metric.

Both the health check API and service are needed so that Kubernetes may know when the service is running, and in case of error, re-creating the service.