<div align="center">
  <br>
  <img alt="rkc" src="https://user-images.githubusercontent.com/108890369/223312587-5c6326cc-5cf8-457d-9bb0-0a90f12190e5.png" height="100">
  <h1>RKC</h1>
  <h3>Handle Kafka messages and process them</h3>
  </br>
</div>

## 🎯 Objectives

This app is designed to handle Kafka messages and process them in a concurrent way. It utilizes Flume as a Multi-Producer Multi-Consumer (MPMC) channel to manage concurrent message processing. The application is structured into different modules:

 - Consumer: Responsible for consuming Kafka messages.
 - Processor: Contains various processors for handling Kafka messages, must implement the Processor trait.
 - Utils: Provides utility functions and structs for the application, such as parsing each message.

  
1. [Introduction](Introduction.md)

2. [Design Considerations](Design_Considerations.md)

3. [Component Design Description](Component_Design_Description.md)

4. [Workflow And Algorithms](Workflow_and_Algorithms.md)

5. [Configuration & Execution](../../../cloud/platforms/rkc/README.md)