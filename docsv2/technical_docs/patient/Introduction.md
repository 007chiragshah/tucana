# Patient microservice

The patient microservice purpose is to handle all the data regarding patient data, beds, bed groups, devices, vital ranges, alerts and all relationships between them, which includes encounters, beds and bed group assignment.

It provides an API for the user to interact with, which is mainly use to retrieve information, but can also be used to modify certain entities. Most of the data is generated automatically by consuming messages from the event bus comming from the PM and generating the corresponding entities that are going to be retrieved by the user later on.

Out of all the data handled by this microservice, the information that the user can modify are:
 
 - Beds
 - Bed groups
 - Patient data and encounters (Only when the encounters are started by Central Server)

All other entities are modified automatically based on the events received from the PM.