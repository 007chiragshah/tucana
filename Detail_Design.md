<div align="center">
<h1>Central Hub Infrastructure</h1>
<h2> ⚜️ Detailed Design </h2>
</div>


### Rancher:

<div align="center">
<img alt="Rancher_Arch" src="Images/Rancher_Archi.png">
</div>

```mermaid
flowchart LR
    subgraph "RKE2 Server Node"
        direction TB
        RKESupervisorServer["RKE Supervisor*"]
        KubeletServer["kubelet"]
        Etcd["etcd"]
        APIServer["api-server"]
        ControllerManager["controller-manager"]
        CloudControllerManager["cloud-controller-manager"]
        Scheduler["scheduler"]

        RKESupervisorServer --> KubeletServer
        KubeletServer --> APIServer
        APIServer --> Etcd
        APIServer --> ControllerManager
        APIServer --> CloudControllerManager
        APIServer --> Scheduler
        KubeletServer --> StaticPods["Static pods"]
    end

    subgraph "RKE2 Agent Node"
        direction TB
        RKESupervisorAgent["RKE Supervisor"]
        KubeletAgent["kubelet"]
        CRIContainerd["CRI: containerd"]
        ManagedProcesses["Managed processes"]
        
        subgraph "RKE2 K8s Deployments"
            direction TB
            KubeProxy["kube-proxy"]
            CNI["CNI: canal"]
            HelmController["helm-controller"]
            CoreDNS["CoreDNS"]
            MetricServer["metric-server"]
            Ingress["Ingress"]
        end

        subgraph "User-defined workloads"
            direction TB
            ServiceMesh["Service Mesh"]
            OtherApps["Other Apps"]
        end

        RKESupervisorAgent --> KubeletAgent
        KubeletAgent --> CRIContainerd
        KubeletAgent --> ManagedProcesses
        ManagedProcesses --> RKE2K8sDeployments[RKE2 K8s Deployments]
        RKE2K8sDeployments --> KubeProxy
        RKE2K8sDeployments --> CNI
        RKE2K8sDeployments --> HelmController
        RKE2K8sDeployments --> CoreDNS
        RKE2K8sDeployments --> MetricServer
        RKE2K8sDeployments --> Ingress
        ManagedProcesses --> UserDefinedWorkloads[User-defined workloads]
        UserDefinedWorkloads --> ServiceMesh
        UserDefinedWorkloads --> OtherApps
    end
```

- We are using Rancher in our infra for creating and managing the kubernetes cluster of one master node, three worker nodes, and one load balancer.
- Rancher is a complete container management platform for Kubernetes, giving you the tools to successfully run Kubernetes anywhere
- In our setup we are deploying rke2 service using helm chart and installing the service on each node by using ansible, where on master node we are installing the "rke2-server" service, and on the worker nodes 
  we are installing "rke2-agent" service.

**How it works**
- Rancher uses Kubernetes as its core and manages cluster configurations via the Kubernetes API.
- It deploys a lightweight Kubernetes distribution called RKE (Rancher Kubernetes Engine) for creating clusters quickly.
- Rancher works as a centralized platform for managing Kubernetes clusters across diverse environments, whether on-premises, in the cloud, or at the edge.
- Rancher integrates with enterprise-grade tools for authentication, monitoring, logging, and alerting, such as LDAP, Active Directory, Prometheus, and Grafana, providing a comprehensive ecosystem for Kubernetes 
  management. 
### Kafka Cluster:

```mermaid
graph TD
    subgraph Producers
        Producer1["Producer"]
        Producer2["Producer"]
        Producer3["Producer"]
    end

    subgraph "A Topic"
        Partition1["Partition 1"]
        Partition2["Partition 2"]
        Partition3["Partition 3"]
    end

    subgraph Brokers
        Broker0["Broker-0 Server"]
        Broker1["Broker-1 Server"]
        Broker2["Broker-2 Server"]
    end

    subgraph "ZooKeeper Ensemble"
        Node1["Node 1"]
        Node2["Node 2"]
        Node3["Node 3"]
    end

    subgraph "Consumer Group"
        Consumer1["Consumer"]
        Consumer2["Consumer"]
        Consumer3["Consumer"]
    end

    %% Producers to Partitions
    Producer1 --> Partition1
    Producer2 --> Partition2
    Producer3 --> Partition3

    %% Partitions to Brokers
    Partition1 -.-> Broker0
    Partition1 -.-> Broker1
    Partition2 -.-> Broker0
    Partition2 -.-> Broker2
    Partition3 -.-> Broker1
    Partition3 -.-> Broker2

    %% Brokers to ZooKeeper
    Broker0 --> Node1
    Broker1 --> Node2
    Broker2 --> Node3

    %% Partitions to Consumers
    Partition1 --> Consumer1
    Partition2 --> Consumer2
    Partition3 --> Consumer3
```
- We are using kafka in our infra for collecting and storing real time data from the different sources like alerts, event-autheProducers and Consumers Work Independently:ntication, technical alerts, sdc events 
  etc.
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

### Istio:

<div align="center">
<img alt="Istio" src="Images/istio.drawio.png">
</div>

- We are using istio in our infra to encrypt the communication between service to service by enabling the mTLS (mutual TLS) protocol, where authentication required from both the end which makes communication 
  more secured.
- As you can see in the image all the central hub components are communicating with each other using mTLS (mutual TLS) protocol.
- Istio is a powerful service mesh that provides advanced traffic management, security, and observability for microservices architectures. It simplifies the management of communication between services by 
  offering features like load balancing, traffic routing, service discovery, and fault tolerance. Istio enhances security by enabling mTLS (mutual TLS) for service-to-service encryption.

**What is mTLS Protocol**

- mTLS (mutual TLS) is a protocol extension of the standard TLS (Transport Layer Security) protocol. While TLS typically provides encryption and authentication for data transmitted over a network, where mTLS 
  goes a step further by requiring both the client and the server to authenticate each other.

**How it works**

- The server presents a certificate to authenticate itself to the client.
- The client also presents its own certificate to authenticate itself to the server.

- This mutual authentication ensures that both parties are verified, enhancing the security of communication, especially in service-to-service interactions in microservices architectures.


### k8s infra components

| **Name**                                     | **Author/Manufacturer**              | **Version**                              | **Vulnerability (if reported)** | **Usage in Cluster**                      |
|---------------------------------------------|---------------------------------------|------------------------------------------|----------------------------------|------------------------------------------|
| docker.io/library/haproxy:2.7               | Docker Hub                            | 2.7                                      | Not reported                    | Load Balancing                           |
| docker.io/rancher/mirrored-cilium-operator-generic:v1.14.4 | Rancher (mirrored)                   | v1.14.4                                  | Not reported                    | CNI (Container Network Interface) Operator |
| docker.io/rancher/mirrored-cilium-cilium:v1.14.4 | Rancher (mirrored)                   | v1.14.4                                  | Not reported                    | CNI (Networking for Cluster)             |
| docker.io/rancher/hardened-cni-plugins:v1.2.0-build20231009 | Rancher                            | v1.2.0-build20231009                     | Not reported                    | Hardened CNI Plugins for Network Security |
| docker.io/rancher/rke2-cloud-provider:v1.28.2-build20231016 | Rancher                            | v1.28.2-build20231016                    | Not reported                    | Cloud Provider Integration for RKE2      |
| docker.io/rancher/hardened-etcd:v3.5.9-k3s1-build20230802 | Rancher                            | v3.5.9-k3s1-build20230802                | Not reported                    | Cluster State Management (etcd)          |
| docker.io/rancher/klipper-helm:v0.8.2-build20230815 | Rancher                            | v0.8.2-build20230815                     | Not reported                    | Helm Chart Manager                       |
| docker.io/rancher/hardened-kubernetes:v1.29.0-rke2r1-build20231213 | Rancher                            | v1.29.0-rke2r1-build20231213             | Not reported                    | Hardened Kubernetes Core                 |
| docker.io/rancher/hardened-coredns:v1.10.1-build20231009 | Rancher                            | v1.10.1-build20231009                    | Not reported                    | DNS Resolution                           |
| docker.io/rancher/hardened-cluster-autoscaler:v1.8.6-build20231009 | Rancher                            | v1.8.6-build20231009                     | Not reported                    | Cluster Autoscaling                      |
| docker.io/rancher/hardened-k8s-metrics-server:v0.6.3-build20231009 | Rancher                            | v0.6.3-build20231009                     | Not reported                    | Metrics Collection (K8s)                 |
| docker.io/rancher/mirrored-sig-storage-snapshot-controller:v6.2.1 | Rancher (mirrored)                | v6.2.1                                   | Not reported                    | Snapshot Controller for Storage          |
| docker.io/rancher/mirrored-sig-storage-snapshot-validation-webhook:v6.2.2 | Rancher (mirrored)                | v6.2.2                                   | Not reported                    | Storage Snapshot Validation              |
| gcr.io/kubebuilder/kube-rbac-proxy:v0.13.0  | Kubebuilder                           | v0.13.0                                  | Not reported                    | RBAC (Role-Based Access Control) Proxy   |
| docker.io/kubernetesui/dashboard:v2.7.0     | Kubernetes UI                         | v2.7.0                                   | Not reported                    | Web UI for Kubernetes                    |
| docker.io/kubernetesui/metrics-scraper:v1.0.9 | Kubernetes UI                        | v1.0.9                                   | Not reported                    | Scraper for Kubernetes Dashboard Metrics |
| quay.io/strimzi/kafka:0.42.0-kafka-3.7.1    | Strimzi                               | 0.42.0-kafka-3.7.1                       | Not reported                    | Apache Kafka for Data Streaming          |
| quay.io/strimzi/operator:0.42.0             | Strimzi                               | 0.42.0                                   | Not reported                    | Kafka Operator                           |
| docker.io/rancher/local-path-provisioner:v0.0.24 | Rancher                            | v0.0.24                                  | Not reported                    | Local Storage Provisioner                |
| docker.io/reactivetechio/kubegres:1.16      | Reactive Tech IO                      | 1                                        | Not reported                    | PostgreSQL Operator for Kubernetes       |
| registry.k8s.io/ingress-nginx/controller:v1.11.1 | Kubernetes Ingress NGINX            | v1.11.1                                  | Not reported                    | Ingress Controller (NGINX)               |
| registry.k8s.io/ingress-nginx/custom-error-pages:v1.0.1 | Kubernetes Ingress NGINX          | v1.0.1                                   | Not reported                    | Custom Error Pages for NGINX             |
| registry.k8s.io/ingress-nginx/kube-webhook-certgen:v1.4.1 | Kubernetes Ingress NGINX          | v1.4.1                                   | Not reported                    | Webhook Certificate Generator            |
| docker.io/library/busybox:latest           | Docker Hub (library/busybox)          | latest                                   | Not reported                    | Minimal OS Image                         |
| docker.io/library/postgres:14.12           | Docker Hub (library/postgres)         | 14.12                                   | Not reported                    | Database (PostgreSQL)                    |
| docker.io/library/redis:6.2.14-bookworm     | Docker Hub (library/redis)            | 6.2.14-bookworm                          | Not reported                    | In-memory Data Store (Redis)             |
| quay.io/prometheus-operator/prometheus-config-reloader:v0.75.2 | Prometheus Operator               | v0.75.2                                  | Not reported                    | Config Reloading for Prometheus          |
| docker.io/grafana/loki:2.9.3                | Grafana                               | 2.9.3                                   | Not reported                    | Log Aggregation (Loki)                   |
| docker.io/grafana/promtail:2.9.3            | Grafana                               | 2.9.3                                   | Not reported                    | Log Collection (Promtail)                |
| quay.io/kiwigrid/k8s-sidecar:1.27.4         | Kiwigrid                              | 1.27.4                                  | Not reported                    | Sidecar for Monitoring/Logging           |
| docker.io/grafana/grafana:11.1.4            | Grafana                               | 11.1.4                                  | Not reported                    | Monitoring and Visualization Tool        |
| quay.io/prometheus-operator/prometheus-operator:v0.75.2 | Prometheus Operator               | v0.75.2                                  | Not reported                    | Prometheus Operator                      |
| registry.k8s.io/kube-state-metrics/kube-state-metrics:v2.13.0 | Kubernetes State Metrics          | v2.13.0                                  | Not reported                    | Metrics for Kubernetes Objects           |
| quay.io/prometheus/prometheus:v2.54.0       | Prometheus                            | v2.54.0                                 | Not reported                    | Metrics Collection and Monitoring        |
| quay.io/prometheus/node-exporter:v1.8.2     | Prometheus                            | v1.8.2                                  | Not reported                    | Hardware and OS Metrics Exporter         |
| registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20221220-controller-v1.5.1-58-g787ea74b6 | Kubernetes Ingress NGINX          | v20221220-controller-v1.5.1-58-g787ea74b6 | Not reported                    | Certificate Management for Webhooks      |
| quay.io/prometheus/alertmanager:v0.27.0     | Prometheus                            | v0.27.0                                 | Not reported                    | Alert Management for Prometheus          |

