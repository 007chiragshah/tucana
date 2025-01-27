  <div align="center">
<h1>Central Hub Infrastructure</h1>
<h2> 🏛️ System Architecture </h2>
</div>

## High-Level System Architecture

<div align="center">
<img alt="k8s_infra" src="Images/Infrastructure_K8s_Infra.drawio.png">
</div>

  ### Control Plane Node:

  - The control plane is responsible for container orchestration, making global decisions (e.g., scheduling), detecting/responding to cluster events, and maintaining the state of a cluster.
  - The Kubernetes control plane consists of several components, each responsible for a specific task (as explained below). These components work together to ensure that each Kubernetes cluster’s state matches 
    the pre-defined desired state.

  1. **Kube-API server**

  <div align="center">
  <img alt="kube-api-server" src="Images/Infrastructure_Kube-API-Server.png">
  </div>

  - The kube-API server acts as the central communication hub for users, components, and the Kubernetes cluster. When using tools like kubectl, it communicates via HTTP REST APIs, while internal components such 
    as the scheduler and controllers use gRPC for interactions. The API server ensures secure communication through TLS, validating data for API objects, managing API requests, and authenticating and 
    authorizing users. It also coordinates processes between the control plane and worker node components, ensuring smooth cluster operations.
  - Additionally, the API server exclusively interacts with etcd to store and retrieve cluster state information. It features a built-in bastion apiserver proxy, which enables external access to ClusterIP 
    services, providing a secure way to interact with the cluster's internal resources. This design allows the API server to serve as a robust and secure gateway for managing the Kubernetes ecosystem.


  2. **ETCD**:
  <div align="center">
  <img alt="ETCD" src="Images/Infrastructure_etcd.png">
  </div>
  
  - etcd is a distributed key-value store designed to securely store Kubernetes cluster data, such as pod information, states, and namespaces. It is accessible only by the Kubernetes API server to ensure 
    security. Kubernetes interacts with etcd through its key-value API using gRPC, storing all objects in the /registry directory in key-value format.
  - The Kubernetes API server leverages etcd's watch feature to track changes to object states, enabling real-time updates and coordination. As the only StatefulSet component in the control plane, etcd serves a 
    as a reliable and robust database for managing Kubernetes cluster data.


  3. **kube-scheduler**:

  - The kube-scheduler selects the best worker node for a pod based on its requirements, such as CPU, memory, affinity, leveraging etcd to store critical scheduling data. It filters nodes, scores them using 
    plugins, and binds the pod to the highest-scoring node, ensuring efficient and priority-based pod management while supporting custom plugins.

  4. **kube-controller-manager**:

  <div align="center">
  <img alt="Kubernetes-control-manager" src="Images/Infrastructure_Kubernetes-control-manager.png">
  </div>

  - The kube-controller-manager manages various controllers to maintain the cluster's desired state. For instance, it ensures deployments specified in a YAML manifest, such as replicas, volume mounts, and 
    configmaps, remain consistent.
  - Key controllers include:
     - Deployment Controllers: Manage multiple replicas of containerized applications.
     - Replication Controllers: Ensure a fixed number of pod replicas are running, replacing failed pods automatically.
     - StatefulSet Controllers: Provide persistent storage, unique network identities, and controlled scaling for stateful applications.
     - DaemonSet Controllers: Ensure specific pods run on every node or selected nodes based on labels.

  5. **cloud-controller-manager**

  <div align="center">
  <img alt="cloud-controller-manager" src="Images/Infrastructure_cloud-controller-manager.png">
  </div>

  - The cloud controller manager bridges Cloud Platform APIs and the Kubernetes cluster, enabling seamless integration between Kubernetes and cloud providers via plugins. It allows core Kubernetes components to 
    function independently while supporting cloud-specific functionality.
  - As in our setup Central Hub uses on-premise setup so CCM is not required for on-prem setup.

  6. **Promtail agent**:

  - On the Controlplane node Central Hub uses a promtail agent to collect logs and forward them to Loki for centralized log management. Promtail is responsible for discovering log sources, attaching metadata 
    (such as pod name, namespace, and labels), and forwarding logs to Loki. It can collect logs from system components like the kube-apiserver, kube-scheduler, and kube-controller-manager.


  ### Worker Nodes:
 
  - Worker nodes are critical components in a Kubernetes architecture because they help in running containerized applications.
  - Worker nodes are the primary execution units in a Kubernetes cluster where the actual workloads run. Each worker node can host multiple pods, each containing one or more containers running inside them. 
    Every worker node consists of three components responsible for scheduling and managing these pods:

  1. **Kubelet**:

  <div align="center">
  <img alt="kubelet" src="Images/Infrastructure_kubelet.png">
  </div>

  - The kubelet is a vital Kubernetes component running on every node, responsible for node registration with the API server and managing pods based on the podSpec. It creates, modifies, and deletes containers, 
    handles probes (liveliness, readiness, and startup), mounts volumes, and reports node and pod status to the API server.
  - It accepts podSpec from sources like files, HTTP endpoints, and servers, leveraging the container runtime to pull images and run containers. During control plane bootstrapping, the kubelet starts the API 
    server, scheduler, and controller manager as static pods, ensuring pods remain desired.

 2. **kube-proxy**:

  <div align="center">
  <img alt="kubeproxy" src="Images/Infrastructure_kubeproxy.png">
  </div>

  - Kube-proxy is a key component in Kubernetes that implements Services for exposing pods to traffic. It works in conjunction with Kubernetes Service and Endpoint objects, where Services expose pods, and 
    Endpoints store their IP addresses and ports. Kube-proxy creates network rules to route traffic to the correct pods under a Service object, supporting protocols like UDP, TCP, and SCTP.
  - Running as a daemonset on every node, Kube-proxy interacts with the API server to retrieve details about Services and their associated pod IPs and ports. It monitors changes to services and endpoints, 
    updating routing rules accordingly. Kube-proxy operates in different modes, including IPTables, IPVS, Userspace, and Kernelspace. In IPTables mode, it manages traffic through IPtable rules, randomly 
    selecting a backend pod for load balancing.
 
 3. **Container runtime**:

  <div align="center">
  <img alt="container-runtime-architecture" src="Images/Infrastructure_container-runtime-architecture.png">
  </div>

  - Just like the Java Runtime (JRE) is needed to run Java programs, a container runtime is essential for running containers. It handles tasks like pulling images from registries, allocating resources, 
    isolating containers, and managing their lifecycle on a host.
  - Kubernetes communicates with container runtimes through the Container Runtime Interface (CRI), which defines APIs for container creation, starting, stopping, and deletion, as well as managing images and 
    networks. The Open Container Initiative (OCI) establishes standards for container formats and runtimes. Kubernetes supports multiple CRI-compliant runtimes, such as CRI-O, Docker Engine, and containerd. The 
    kubelet agent interacts with the container runtime using CRI APIs to manage containers and report container information to the control plane.

 4. **Postgres SQL**:

  - Central Hub uses Postgres in our infra as a database to store the data of different central-hub applications with AES-256 encryption algorithm.
  - In our infra Central Hub uses kubegres to manage Postgres, as kubegres is a Kubernetes operator who manages the deployment, scaling, etc of Postgres.
  - We used Postgres in our infra because of its advanced features supporting SQL and JSON, able to manage structured and unstructured data, providing strong security with encrypted data by using AES-256 
    encryption algorithm.

 5. **Kafka**:

  <div align="center">
  <img alt="kafka" src="Images/Infrastructure_kafka.drawio.png">
  </div>
  
  - Central Hub uses Kafka in our infra for collecting and storing real-time data from different sources like alerts, event authentication, technical alerts, SDC events, etc.
  - Kafka is a distributed event platform that uses producers to send messages to different topics, where consumers can read that message by subscribing to the relevant topics. Central Hub uses a zookeeper to 
    manage Kafka cluster state and its high availability.
  - Central Hub uses **Strimzi Operator** in our infra for managing the Apache Kafka on Kubernetes where strimzi is a Kubernetes operator which simplifies the deployment and management of the Kafka.
  - We used Kafka as it is known for high throughput with real-time data stream and fault tolerance. It makes sure of data reliability low latency communication and ease of integration.

 6. **Redis**:

  - We used Redis in our infra for caching, session management, and storing the user state of our different central hub applications.
  - We choose Redis because it provides features like high performance as an in-memory data store, supports complex data structure, is faster and more scalable for caching, flexible. It supports pub/sub 
    messaging, ensuring fast, scalable, and reliable performance.

 7. **Monitoring**:

  - Central Hub uses different dashboards like the Kubernetes dashboard, Grafana Dashboard, and Loki Dashboard for different monitoring purposes.
    - **Kubernetes Dashboard**:
      - We used the Kubernetes dashboard in our infra setup to monitor the health, cluster state, logs, and performance of all the Kubernetes resources like pods, jobs, deployment, replicaset, services, etc. 
    - **Loki Dashboard**:
      - Central Hub uses the Loki dashboard to display the audit-related logs and pod-related logs.
    - **Grafana Dashboard**:
      - Central Hub uses the Grafana dashboard to show color-coded visualization of the different alerts coming from the Prometheus with the different views of the current alert. its status, also with the table 
        format.
     
 8. **Ingres Loadbalancer**:

  ```mermaid 
  graph LR
    A[Client]-->B(Ingress-managed Load Balancer);
    B-->C{Ingress};
    subgraph Cluster
        C-->D[routing rules];
        D-->E[Service];
        E-->F[Pod];
        E-->G[Pod];
    end
  ```
  
  - We used Ingres load balancer in our infra setup to route the traffic to appropriate backend services based on the routing rules we have provided such as URL path, HTTP, https, hostname, etc.
  - We choose ingres as a load balancer because it offers centralized traffic management, path-based routing, and SSL termination. we can use the same ingress load balancer for different applications with 
    single yaml file just with the routing rules.


 9. **Istio**:

  - Central Hub uses istio in our infra to encrypt the communication between service to service by enabling the mTLS (mutual TLS) protocol, where authentication is required from both ends which makes 
    communication more secure.
  - We used istio for this because it provides great features like advanced traffic management, secured communication using mTLS protocol, supports both Kubernetes and VM-based environments, more flexibility 
    for large-scale and multi-node clusters.
  
 10. **Kubernetes Objects**:

 - **Deployment**:
   - We are installing our central-hub application as deployment manages the desired state of application replicas which provides **high availability**, also with replicas, it is easy to 
     scale up/down the application, Also with deployment, It is easy to roll back to the old version or roll out our new version of the application.

 - **Pod**:
   - A Pod is the smallest deployable unit in Kubernetes, representing a single instance of a running process. It can contain one or more tightly coupled containers that share the same network namespace, 
     storage volumes, and configuration.

 - **Static Pod**:
   - A pod directly managed by the kubelet, defined via static configuration files on a node. Static pods are not part of a Deployment or ReplicaSet and are typically used for critical control plane 
     components.

 - **Service Account**:
   - We used Service Account in Kubernetes as an identity used by processes running inside pods to interact with the Kubernetes API. It provides an authenticated and authorized way for pods to access r 
     resources in the cluster.

 - **Secret**:
   - We used secrets in our infra to store sensitive information like passwords, keys, certificates, and  tokens in an encryption form, which is used by the pods or a service to access the credentials or other 
     sensitive data without exposing it in plain text. By using this we can **secure** our sensitive data.
   - Secret are encrypting data with **base64 encryption** algorithm.
     
 - **Configmap**:
   - We used configmap to store non-sensitive data in a key-value pair in a plaintext format as it is later used by the application and retrieve configuration settings like database URLs, environment 
     variables, or feature flags, making it easier to manage and update configurations without modifying the application.

 - **Cluster role and role binding**:
   - Central Hub uses cluster role and role binding to restrict the access of service accounts to limited resources with limited rights.
   - Where A ClusterRole is a set of permissions that can be applied across the entire cluster, granting access to resources like nodes, namespaces, or persistent volumes. ClusterRoles are often used for 
     cluster-wide access or in cases where the same role needs to be applied to multiple namespaces and A RoleBinding is used to bind a Role or ClusterRole to a user, service account, or group, granting them 
     the specified permissions within a particular namespace (RoleBinding) or across the entire cluster (ClusterRoleBinding).

 - **StatefulSet**:
   - Central Hub uses statefulset for the PostgreSQL in our setup as statefulset is used when you want to manage the state of any application also It ensures stable, unique identities and persistent storage 
     for each pod, which is useful for databases and distributed systems.

 - **Namespace**:
   - Central Hub uses different namespaces in our setup to isolate the different resources for the central-hub application Central Hub uses central-hub namespace, for the k8s dashboard Central Hub uses a 
     dashboard namespace, for ingress-nginx Central Hub, uses Ingres-nginx namespace, etc.
