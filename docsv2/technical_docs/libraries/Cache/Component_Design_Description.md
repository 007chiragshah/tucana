<div align="center">
<h2>⚜️ Component Design Description</h2>
</div>

### **High Level System Architecture**

The high-level system architecture consists of a User, an Application Layer, and a Redis-based Caching Layer. The user sends API requests to the application, where the caching layer first checks if the requested data exists in Redis. If cached data is available, it is returned immediately; otherwise, the application processes the request, retrieves the necessary data, and stores the response in Redis for future use.

### **Class Daigram**

![Cache Class Daigram](<Diagrams/Images/ClassDiagram.png>)

### **Flow Architecture**

![Cache Flow Architecture](<Diagrams/Images/FlowDiagram.png>)

---

### **Environment Configuration**

The following .env file contains the necessary environment settings for development and deployment.
```
ENVIRONMENT=
REDIS_HOST=
REDIS_PORT=
REDIS_USERNAME=
REDIS_PASSWORD=
REDIS_CACHE_TTL=
CACHE_ENABLED=
PROJECT_NAME=
```