<div align="center">
<img alt="SDC" src="../images/centrla_hub_logo.png">
<h1>Central Hub Infrastructure</h1>
<h2> 🎯 Introduction </h2>
</div>

### Purpose

The purpose of this Infrastructure document is to provide a detailed description of the Central hub Infra, design decisions, design detailed understanding. This document will offer a clear and thorough understanding  to end user that how our infrasturcture is designed to provide high availability, reliability and seamless operation. Additionally it's also explains the functionality and interaction of it's various components to provide robust and efficient system.

### Scope

The infrastructure is designed for robust and scalable for deploying, managing, and maintaining applications, ensuring high availability, reliability, and secure communication.This infrastructure includes different tools like docker, kubernetes, ansible, helm chart, terraform, grafana, loki etc for seamless operation, deployment, upgrade/downgrade, monitoring and scalability.

The scope of the infrastructure includes:

- High Availability and Scalability
- Easy Deployment
- Data Security and Encryption
- Backup and Disaster Recovery
- Logging and Monitoring

### System Overview

The infrastructure is the reason for running and managing applications in a secure, scalable, and reliable environment. It is designed such a way to provide high performance, smooth operation, and seamless communication between different components.

The infrastructure is consist of one master node, three worker nodes, and one load balancer node.
1. Master Node: The Master node is responsible for container orchestration, maintaining cluster state, scheduling pods, maitaining replication count.
2. Worker Node: These are the nodes on which we are running the different applications container and each node is managed by the master node.
3. Load Balancer Node: This node Will used to distribute the traffic, provides HTTP/HTTPS based routing.

