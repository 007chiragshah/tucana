<div align="center">
<h1>Central Hub Infrastructure</h1>
<h2> 📈 Design Considerations </h2>
</div>

## Design Constraints

### Hardware Limitations

#### **For central hub desktop**

| Requirement  | Central Hub Desktop |
| ------------- | ------------- |
| CPU  | 2.4 GHz dual-core processor  |
| RAM  | 8GB  |
| Hard Drive Capacity  | At least 50 GB of free space |
| External Storage  | None  |
| Network - LAN | 100/1000 Mbps Ethernet  |
| Network - WLAN | 802.11 a/b/g/n/ac (2.4G + 5 GHz)  |
| Other Hardware  | 1 Keyboard  |
|| 1 Mouse  |
|| Up to 4 Full HD (1920 × 1080) 24-inch monitors |
|| Graphic card supporting up to 4 displays |
|| Speaker: Alarm tones (45 to 85 dB), compliant with IEC 60601-1-8 |
| Operating System  | 64-bit Windows 11 (version 23H2)  |
| Supporting Software  | None  |
| System Volume Configuration	| System volume level shall remain at 100% at all times |

#### **For central-hub server**

| Requirement  | Central Hub Server |
| ------------- | ------------- |
| CPU  | 2 x 2.4GHz (12 core)  |
| RAM  | 32GB  |
| Hard Drive Capacity  | 1.5TB SSD  |
| External Storage  | None  |
| Network  | 100/1000 Mbps Ethernet  |
| Other Hardware  | Uninterruptible power supply  |
| Operating System  | Linux  |
| Supporting Software  | None  |

#### **For Kubernetes cluster**

| Requirement  | Control Plane Node | Worker Nodes (3 Nodes) | Load Balancer Node |
| ------------- | ------------- | ------------- | ------------- |
| CPU  | 2 CPU Cores  | 8 CPU Cores  | 2 CPU Cores  |
| RAM  | 4GB  | 8GB  | 4GB  |
| OS Disk  | 100GB  | 100GB  | 30GB  |
| Data Disk  | None  | 300GB | None |
| Operating System  | Linux (Ubuntu 22.04) | Linux (Ubuntu 22.04)| Linux (Ubuntu 22.04)|

### Infrastructure Component Considerations

In this section, we will provide a brief introduction to key components of the infrastructure.

1. **Docker**:
- Central Hub uses docker in the infra as a docker runtime and also we are transforming our code into a Docker image, and when we need to set up the Central Hub deployment, use the latest image 
  and run a Docker container with it to deploy the entire infrastructure.
- Central Hub chose Docker as a runtime in the infrastructure because of its ease of use, also it provides a complete set of tools for container management, including Docker compose we can manage the 
  multi-container applications within a single configuration file. Additionally, Docker can create multistage Dockerfiles which helps us to build lightweight Docker images by separating the build environment 
  from the runtime environment. This reduces the image size and improves the performance.


2. **Rancher**:
- Central Hub uses Rancher in the infra for creating and managing the Kubernetes cluster of one master node, three worker nodes, and one load balancer.
- Central Hub chose Rancher in our infra for Kubernetes cluster because of its user-friendly interface, ability to handle multi-cluster environments, ease of use, and simplified application deployment making 
  it is an ideal choice for our infrastructure.


3. **Kubernetes Cluster**:
- Central Hub uses a Kubernetes cluster of one controlplane node, three worker nodes, and one load balancer node, for deploying and managing our different central hub applications with high reliability and 
  availability    with seamless deployment and management of the application.
- Central Hub used Kubernetes as an orchestration tool as it provides features like multi-node support, High availability, advanced orchestration features like canary deployment and rolling updates, etc, 
  resource efficiency, ease of scaling the application, etc.


4. **Ansible**:
- Central Hub uses Ansible for the automation and deploying our whole infrastructure on multiple nodes by dividing it into five main tasks, which further broken down into smaller sub-tasks, where all the tasks 
  are consist of simple yaml files.
- Central Hub used Ansible for automation in our infra as it is a powerful agentless automation tool, which means it doesn't require installation on the target machines so it reduces its complexity also it uses 
  a simple yaml file consisting of different tasks. It simplifies automation with its modular structure where task, variable, and value are in separate files which provides easy management and reusability. It 
  defines the desired states, ensuring idempotency and reducing errors.


5. **Helm Chart**
- Central Hub uses a helm chart in our infra to deploy and manage the different central-hub applications.
- The advantage of using helmchart is it simplifies the Kubernetes resource management by automating dependency handling and resource creation with a helmchart we do not have to create different resources like 
  service, deployment, pods, or replicasets unlike Kubernetes clusters as all these things are automatically taken care by the helm chart by using the templates, charts, and values.yaml files. It enables easy 
  deployment, upgrades, and rollback with version control.


6. **Istio**:
- Central Hub uses istio in our infra to encrypt the communication between service to service by enabling the mTLS (mutual TLS) protocol, where authentication is required from both ends which makes 
  communication more secure.
- Central Hub used istio for this because it provides great features like advanced traffic management, secured communication using mTLS protocol, supports both Kubernetes and VM-based environments, more 
  flexibility for large-scale and multi-node clusters.


7. **Monitoring**:
- Our infra Central Hub uses different monitoring tools for the different monitoring as mentioned below:
- **Kubernetes Dashboard**: Central Hub uses the Kubernetes dashboard for monitoring the Kubernetes cluster, different resource states, resource performance monitoring, checking logs, etc.
- **Loki**: Central Hub uses Loki to display the audit-related logs and pod-related logs.
- **Grafana Dashboard**: Central Hub uses the Grafana dashboard to show color-coded visualization of the different alerts coming from the Prometheus with the different views of the current alert. its status, as 
   with the table format.
