# Analysis and design proposal

The purpose of this document is to have an initial design of the architecture for the new SDK project that needs to be implemented. On the following text there is an outline of the general design of the solution, pending issues to resolve before implementation, SOUP items and a plan on how the implementation is going to be done, including epics, quality standards and a more in depth architecture design.

## General design

This sections broadly explains the architecture of the SDK to implement. Here is the C4 component diagram of the proposed solution:

![C4 Component diagram](<C4 Component diagram - Android SDK.svg>)

The idea of the SDK is to have a base "Client" facade that the other team will interact with in order to communicate with Central Server.

Internally there need to be a separation between the handling of the Central Server API and the realtime communication, since they essentially use different protocols of communication, one using REST and the other websockets. For this reason there are 2 handlers defined: API Handler and Realtime Handler.

In addition to the handlers there is the Storage component, which will be needed to communicate with the API since the access and refresh tokens must be implemented somewhere. It could perfectly be part of the API handler but it is defined as another component because of responsibility separation and because the scope of this component could vary depending on the implementation.

### Pending implementation decisions

At the moment there are 2 pending questions which will impact the implementation process of the SDK, although they wont affect the general architecture too much. The questions are the following:

- **Is the websocket connection going to be maintained by the SDK or the application?**
    - For context, this refers to a limitation of Android on handling continous processes. In order to keep the websocket connection alive with the server a [Service](https://developer.android.com/develop/background-work/services) needs to be implemented.
    - This question refers to whose resposible for maintaining this Service, as this can affect the scope of this project.
    - Implementing the Service inside the SDK library increases the scope, but has the upside being easier to use by the Android App.
    - Leaving the implementation of this Service for the app gives the other team more flexibility on the use of this library at the cost of higher complexity on their side.
    - Both options are feasable and depends only on whose team will be responsible for maintaining this.
- **How is the authentication token going to be stored? In-memory or using Android provided keystore?**
    - For context, this relates to how the token is going to be stored inside the SDK which can me implemented in 2 ways:
        - Either by using a variable which will only last for as long the client instance is kept on memory.
        - Or by using [Android keystore](https://developer.android.com/privacy-and-security/keystore) which will persist for as long as the token is not expired.
    - This question is similar to the previous one in the sense that the response will have an impact on the scope of implementation of each team.
    - By storing the token in-memory the implementation time is reduced, but it will limit the use of the SDK (Maybe even return the authentication token so that the storage is handled by the client app)
    - By storing it keystore it will increase the scope of the library, but will make the implementation easier for the client app since the authentication can be all handled internally.

## SOUP analysis

Based on the design proposed before there are a list of SOUP items that will be needed for the implementation of the SDK:

- HTTP client:
    - In order for the SDK to communicate with the Central Server API an HTTP client is needed.
- Websocket client:
    - This SOUP item is needed to communicate with the realtime microservice.
    - This could be the same library as the HTTP client if it supports it, otherwise it will be a separate item.
- Dependency injection:
    - This item is needed for both easier implementation and encapsulation of the SDK classes, to avoid missuse of the library.
- Android/Kotlin/Gradle:
    - This items will obviously be part of the app that uses the library since it is the base of any Android app, but it may be needed to add it as a SOUP item of the SDK too since it is used to package the library. 

## Implementation plan

The following section outlines a plan for the implementation of the designed solution.

### Epics

Here is a list of separate epics that can be independently implemented to separate the problem into smaller chunks:

1. **Project setup**: 
    - This task consist on setting up the project unit test and dependency injection.
    - When setting up the project we should configure the base defined on the [Code quality and standards](#code-quality-and-standards) section.
2. **Interface implementation**:
    - This task consist on implementing the base interfaces without any logic, so that we can have an outline of the functionalities to continue with the rest of the task, even if the library still does not work.
    - The interfaces and classes that must be implemented are the ones defined on the [Detailed design implementation](#detailed-design-implementation) section.
3. **Implement sibel playground app**: 
    - In order for us to know the library works correctly, we need an Android application that uses it so we can test it. 
    - It should be very basic since it is only a test app, but it needs to use all parts of the SDK.
    - Depending on the [decision](#pending-implementation-decisions) of whose going to be responsible for the Android service, we may need to implement the service regardless on the playground if decided that is not going to be part of the SDK, so we have a more accurate representation of the library usage.
    - This task depends on the interface implementation (1).
4. **Implement authentication API and token storage**:
    - This has to be implemented before any other endpoints since all others will use the authentication/token.
    - The interfaces that need to be implemented are the ones described on the [Detailed design implementation](#detailed-design-implementation) section
    - It should also include a process for refreshing token, either manual or automatic.
    - This task depends on the interface implementation (1).
5. **Implement the rest of APIs**:
    - After implementing the auth API handler, the other endpoints can be implemented. 
    - This can be subdivided on group to implement the endpoints in small increments.
    - This task depends on the auth api implementation (3).
6. **Implement the websocket handler**:
    - This task involves implementing the websocket connection and parsing of events received.
    - Depending on the [decision](#pending-implementation-decisions) of whose going to be responsible for the Android service, this may include the implementation of said service.
    - This task depends on the auth api implementation (3).

### Code quality and standards

For this new project since it is going to be used by another team it has to follow stricter quality and standards:

- **Static analysis**: As any other project, this project should include a linter and/or static code analyzer to standarize the way we write new code.
- **Test engine**: We should implement unit/integration tests for all defined APIs and the realtime events and flows.
- **Automatic Kdoc generation**: Since this code is going to be used by another team we should generate documentation on the usage of the SDK. The easies way to know how to use the code is adding Kdoc ([Kotlin documentation](https://kotlinlang.org/docs/kotlin-doc.html#property-name)) to the interfaces since it can me autogenerated, and sits directly with the code that is being used.

### Detailed design implementation

This section shows the definition of all interfaces and classes needed to implement the SDK on the following class diagram:

![Class diagram (Structure)](<Android SDK - Class diagram (Structure).svg>)

On the previous diagram we see the base structure of the the API and realtime handlers. As said before the Client is the base class that the client would interact with, which is hidden behind interfaces. There is one interface for each API grouping, and one for the realtime handler.

Here the BaseApi class is used to contain all the base methods that will be used by all endpoint handlers, like sending request, parsing data, handling errors, etc.

The storage class is used to save the authentication and refresh tokens, which will be used by all endpoints.

![Class diagram (Models)](<Android SDK - Class diagram (Models).svg>)

This second diagram contains all the models used to parse the output of all endpoints and realtime events. Specifically for all realtime events they inherit from the same class since they all have attributes in common, specifically the event type which is used to determine and parse the correct type of event.

All events incomming from the PM are explicitly defined since they all have different payloads. For all events comming from the Central Server backend use generally the same payload, only varying the kind of entity being processed which depends on event type too.
