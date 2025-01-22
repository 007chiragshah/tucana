<div align="center">
<h1>Central Hub Infrastructure</h1>
<h2> 🏛️ System Architecture </h2>
</div>

## High Level System Architecture

<div align="center">
<img alt="k8s_infra" src="/Images/K8s_Infra.drawio.png">
</div>

  ### **Control Plane Node**:

  - The control plane is responsible for container orchestration, making global decisions (e.g., scheduling), detecting/responding to cluster events, and maintains the state of a cluster.
  - The Kubernetes control plane consists of several components, each responsible for a specific task (as explained below). These components work together to ensure that each Kubernetes cluster’s state matches 
    the pre-defined desired state.

  1. **Kube-API server**

  <div align="center">
  <img alt="Kube-API-Server" src="/Images/Kube-API-Server.png">
  </div>

  - The kube-API server acts as the central communication hub for users, components, and the Kubernetes cluster. When using tools like kubectl, it communicates via HTTP REST APIs, while internal components such 
    as the scheduler and controllers use gRPC for interactions. The API server ensures secure communication through TLS, validating data for API objects, managing API requests, and authenticating and authorizing 
    users. It also coordinates processes between control plane and worker node components, ensuring smooth cluster operations.
  - Additionally, the API server exclusively interacts with etcd to store and retrieve cluster state information. It features a built-in bastion apiserver proxy, which enables external access to ClusterIP 
    services, providing a secure way to interact with the cluster's internal resources. This design allows the API server to serve as a robust and secure gateway for managing the Kubernetes ecosystem.

  2. **ETCD**:
  - ETCD is a distributed key-value store used by Kubernetes to securely store cluster data like pod states and namespaces under the /registry directory. Accessible only by the API server via gRPC, it 
    supports state tracking through its watch feature, making it a critical StatefulSet component for Kubernetes.

  4. **kuber control manager**:
  5. 
