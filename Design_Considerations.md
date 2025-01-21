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

#### **For kubernetes cluster**

| Requirement  | Control Plane Node | Worker Nodes (3 Nodes) | Load Balancer Node |
| ------------- | ------------- | ------------- | ------------- |
| CPU  | 2 CPU Cores  | 8 CPU Cores  | 2 CPU Cores  |
| RAM  | 4GB  | 8GB  | 4GB  |
| OS Disk  | 100GB  | 100GB  | 30GB  |
| Data Disk  | None  | 300GB | None |
| Operating System  | Linux (Ubuntu 22.04) | Linux (Ubuntu 22.04)| Linux (Ubuntu 22.04)|

#### Infrastructure Component Considerations

In this section we will provide a brief introduction of key components of the infrastructure.

1. **Docker**:

- We are using docker in our infra as a docker runtime and also we are transforming our code into a Docker image, and when we need to set up the Central Hub deployment, we simply download the latest image and 
  run a Docker container with it to deploy the entire infrastructure.
- We used docker as a runtime in our infrastructure because of it's ease of use, also it's provides a complete set of tools for container management, including Docker compose we can manage the multicontainer 
  applications within a single configuration file. Additionally, Docker has ability to create multistage Dockerfiles which helps us to build light weight Docker images by seperating the build environment from 
  the runtime environment. This reduce the image size and improves the performance.

2. **Rancher**:

- We are using Rancher in our infra for creating and managing the kubernetes cluster of one master node, three worker nodes, and one load balancer.
- We used Rancher in our infra for kubernetes cluster because of it's user friendly interface, ability to handle multi-cluster environment, ease of use and simplified application deployement making it ideal 
  choice for our infrastructure.

3. **Kubernetes Cluster**:
- We are using kubernetes cluster of one controlplane node, three worker nodes, and one load balancer node, for deploying and managing our different centralhub application with high reliability and availability    with seamless deployment and management of the application.
- We used kubernetes as a orchastration tool as it's provides features like multi-node support, High availability, advance orchastration features like canary deployment and rolling updates etc, resource 
  efficiency, ease to scale the application etc.

4. **Postgres SQL**:
- We are using postgres in our infra as a database to store the data of different central-hub applications with AES-256 encryption algorithm.
- In our infra we are using kubegres to manage the posrgres, as kubegres is a kuberntes operator who manages the deployment, scaling etc of the postgres.
- We used postgres in our infra because of its advanced features like supports SQL and JSON, able to manage structured and unstructured data, provides strong security with encrypted data by using AES-256 
  encryption algorithm. 

5. **Kafka**:
- We are using kafka in our infra for collecting and storing real time data from the different sources like alerts, event-authentication, technical alerts, sdc events etc.
- Kafka is a distributed event platform which uses producers to sent messages to different topics, where consumer can read that message by subscribing the relevant topics. We are using zookeepr for managing 
  kafka cluster state and its high availability.
- We are using **Strimzi Operator** in our infra for managing the apache kafka on the kubernetes where strimzi is a kubernetes operator which simplifies the deployment and management of the kafka.
- We used kafka as it is known for high throughput with real time data stream, fault tolerance. It make sures of data reliability and low letency communication and easy to integrate.

6. **Ansible**:
- We are using ansible for the automation and deploying our whole infrastructure on multiple nodes by deviding into five main task, which further broken down to smaller sub-task, where all the tasks are consist 
  of simple yaml files.
- We used ansible for automation in our infra as it is a powerful agentless automation tool means it doesn't required to installation on the target machines so it's reduce its complexity also it uses a simple 
  yaml file consist of different tasks. It simplifies automation with its modular structure where task, variable and value are in seperate files which provides easy management and reusability. It is defining the 
  desired states which makes sure of idempotency and reduce the errors.

7. **Helm Chart**
- We are using helm chart in our infra to deploying and managing the different central-hub applications.
- Advantage of using helm chart is it simplifies the kuberntes resource management by automating dependency handling and resource creating like with helmchart we do not have to create different resource like 
  service, deployment, pods, replicaset unlike kubernetes cluster as all these things automatically taken care by the helm chart by using the templates, charts and values.yaml files. It enables the easy 
  deployment, upgrades and rollback with version control.

8. **Istio**:
- We are using istio in our infra to encrypt the communication between service to service by enabling the mTLS (mutual TLS) protocol, where authentication required from both the end which makes communication 
  more secured.
- We used istio for this becaue it provides a great features like advanced traffice management, secured communication using mTLS protocol, supports both kubernetes and VM-based environment, more flexible for 
  large scale and multi node cluster.

9. **Redis**:
- We used redis in our infra for caching, session management, storing user state of our different central hub applications.
- We used redis because it provides features like high performance as an in memory data store, supports complex data structure, faster and more scalable for caching, flexible.

10. **Monitoring**:
- In our infra we are using different monitoring tools for the different monitoring as mentioned below:
- **Kubernetes Dashboard**: We are using kubernetes dashboard for monitoring the kubernetes cluster, different resources state, resource performance monitoring, checking logs etc.
- **Loki Dashboard**: We are using loki dashboard to display the audit related logs and pod related logs.
- **Grafana Dashboard**: We are using Grafana dashboard to show color coded visulisation of the different alerts coming from the prometheus with the different views of the current alert. its status, also with 
  the table formate.
