<div align="center">
<h1>Central Hub Infrastructure</h1>
<h2> 🏛️ System Architecture </h2>
</div>

## High Level System Architecture

![k8s_infra](/Images/K8s_Infra.drawio.png)

  ### 1. **Control Plane Node**:

  - The control plane is responsible for container orchestration, making global decisions (e.g., scheduling), detecting/responding to cluster events, and maintains the state of a cluster.
  - The Kubernetes control plane consists of several components, each responsible for a specific task (as explained below). These components work together to ensure that each Kubernetes cluster’s state matches 
    the pre-defined desired state.
    1. **Kube-API server**

    ```mermaid
    graph TD
    A[kube-APIserver] --> B{Control Plane}
    A --> C{Worker Node}
    B --> D[kube scheduler]
    B --> E[etcd]
    C --> F[kube proxy]
    C --> G[Kubelet]
    C --> H[kubectl]
    A --> I[kube controller manager]
    I --> J[apps using k8s SDK]
    I --> K[Monitoring Systems]
    I --> L[Third Party Apps]
    subgraph Control Plane
        D
        E
    end
    subgraph Worker Node
        F
        G
        H
    end
    subgraph Other Components
        I
        J
        K
        L
    end
    ```

