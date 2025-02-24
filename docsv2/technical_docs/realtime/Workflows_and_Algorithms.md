# Workflow and algorithms

Since the realtime service works as a proxy it has only two flows. One flow is for establishing the connection with the service, and the other one is maintaining said connection.  

## Connect to realtime service

This is the only flow of the microservice triggered by the user. This flow involves connecting to the websocket for the first time, but also the configuration of the message message filtering. 

The filtering is configured by the client by sending messages to the realtime service including all the criteria needed, then this criteria is sent to another thread that handles the messages incomming from the event bus.

The exact flow is described in the following diagram:

![Connect to realtime service - Activity diagram](<../images/activity_diagrams/realtime/Connect to realtime service.svg>)

## Event bus consumer

This is the main loop of the application which is constantly running on background. 

It listens for the messages from Kafka and sends them to each of the connected devices depending on the criteria defined for each open connection. This filtering criteria is determined in another thread, which was described on the previous flow, this flow is only responsible for actually filtering the messages.

The exact flow is described in the following diagram:

![Event bus consumer - Activity diagram](<../images/activity_diagrams/realtime/Event bus consumer.svg>)