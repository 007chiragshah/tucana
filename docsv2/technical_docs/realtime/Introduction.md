# Realtime microservice

The purpose of the realtime service is to provide an interface for the frontend client to receive messages from the event bus (Kafka) that are sent by both the Patient Monitor and the backend microservices. 

It works as a proxy by connecting to Kafka and redirecting all the events to a websocket connection where the frontend service connects. In addition to that it implements the functionality of filtering messages based on multiple criteria like the patients or device whose event belongs to, as well as the code of the metrics being sent. It also implemnts the caching vitals events sent to make sure the user has the lates value of metrics, especially for those metrics that are updated sporadically or have a long period of activation.