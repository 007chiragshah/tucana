<div align="center">
<h1>Central Hub Infrastructure</h1>
<h2> ⚜️ Detailed Design </h2>
</div>

### Kafka Cluster:

<div align="center">
<img alt="kafka_arch" src="Images/kafka_arch.png">
</div>

- We are using kafka in our infra for collecting and storing real time data from the different sources like alerts, event-autheProducers and Consumers Work Independently:ntication, technical alerts, sdc events etc.
- Kafka is a distributed event streaming platform designed to handle high-throughput, fault-tolerant, and low-latency messaging. Here's a simplified overview of how it works:

    * **Topic**: Data is organized into categories called topics. Producers write messages to these topics, and consumers read them.
    * **Producers**: Producers are applications that send data (events) to Kafka topics. They push messages in a serialized format.
    * **Consumers**: Consumers are applications that subscribe to topics and read messages. They can read at their own pace, and Kafka retains messages for a configurable time.
    * **Partitions**: Topics are divided into partitions for scalability. Each partition can reside on a different Kafka broker, allowing for parallel processing.
    * **Brokers**: Kafka runs on a cluster of servers called brokers. Each broker stores partitioned data and manages its replication for fault tolerance.
    * **Replication**: Kafka replicates partitions across brokers to ensure data availability in case of failures.
    * **Consumer Group**: Consumers can belong to consumer groups for load balancing. Each partition is processed by only one consumer in a group, enabling horizontal scalability.
    * **Producers and Consumers Work Independently**: Producers and consumers work asynchronously. Producers can write messages without waiting for consumers to process them.

#### Workflow Example:

- A producer sends a message (e.g., a log entry) to a Kafka topic.
- The message is stored in a partition on one or more brokers.
- A consumer subscribes to the topic, retrieves the message, and processes it (e.g., storing it in a database).
