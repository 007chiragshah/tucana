<div align="center">
<h1>Central Hub Installation</h1>
<h2> 📑Prerequisite </h2>
</div>

## Server Requirement

- The installation of the Central Hub requires the following hardware, operating system specifications, certification and supporting software.
- All virtual machines (VMs) must utilize Trusted Platform Modules (TPM) for hardware-level security and Secure Boot to ensure that only trusted, signed software can run.
- Administrative permissions are required on the destination systems. Additionally, Anti-Virus software should be installed before deploying the Central Hub Desktop application.
- If not already in place, this document recommends Comodo AV software.

## Minimum Hardware Requirements

### Hardware requirement for the Central Hub Desktop (User Interface)

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


### Hardware requirement for the Central Hub Server

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

- On the Central Hub Server, you need to create a total of 5 virtual machines (VMs): one for the Control Plane, three for the worker nodes, and one for the load balancer. The VMs can be created using any of the following tools:
   - Proxmox
   - VMWare
   - VirtualBox
 
### VM Requiremnt for Kubernetes cluster

| Requirement  | Control Plane Node | Worker Nodes (3 Nodes) | Load Balancer Node |
| ------------- | ------------- | ------------- | ------------- |
| CPU  | 2 CPU Cores  | 8 CPU Cores  | 2 CPU Cores  |
| RAM  | 4GB  | 8GB  | 4GB  |
| OS Disk  | 50GB  | 50GB  | 50GB  |
| Data Disk  | None  | 300GB | None |
| Operating System  | Linux (Ubuntu 22.04) | Linux (Ubuntu 22.04)| Linux (Ubuntu 22.04)|

- While Installing the VMs need to make sure that we enable the disk encryption for the OS disk to support the data security.
  ![disk_enc](https://github.com/user-attachments/assets/2f41d3a9-9ca3-445d-b1a5-63e4d05b3ee9)

### VM Preparation
1. Users of all the VMs should be same
2. There should be no password policy in place, allowing the user to execute sudo commands without needing a password. You can achieve that using below command.
```
echo "$USER ALL=(ALL) NOPASSWD:ALL" | sudo tee -a /etc/sudoers
```
3. A single pair of SSH keys (Private and Public) should be created, with the same public key deployed on all nodes, enabling SSH access to all VMs using the same private key. You can generate the keys using below command.
```
ssh-keygen -t rsa
```
4. Once you login to VM check the disk size using below command it should show the OS disk as mentioned above aroung 50GB.
```
df -Th
```
5. If it is not showing aroung 50GB then need to manually resizing of the volume on each node using below commands.
- First check the LVM
  ```
  lvdisplay
  ```
  ![lvm](https://github.com/user-attachments/assets/6f311dec-9ed9-4bf7-b714-6158572bfbab)
- Manually extend the volume
  ```
  lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
  ```
- Resize the file system using below command
  ```
  resize2fs /dev/mapper/ubuntu-vg-ubuntu-lv
  ```
- Check the size again.
6. Mount DATA disk on all worker VMs as /opt/local-path-provisioner/ using below commands.
- Run below command to identify the disk.
  ```
  lsblk
  ```
- Partition the Disk (if needed):
  ```
  sudo fdisk /dev/[your-disk]
  Press n for a new partition, select the type, and follow prompts.
  Press w to write changes and exit
  ```
- Create a Filesystem:
  ```
  sudo mkfs.ext4 /dev/[your-partition] (e.g., /dev/sdb1)
  ```
- Create a Mount Point:
  ```
  sudo mkdir -p /opt/local-path-provisioner/
  ```
- Mount the Disk:
  ```
  sudo mount /dev/[your-partition] /opt/local-path-provisioner/
  ```
- Configure Mount at Boot (Optional):
  ```
  sudo nano /etc/fstab
  **Add a line like:**
  /dev/[your-partition] /opt/local-path-provisioner/ ext4 defaults 0 2

  Note - eplace [your-partition] (e.g., /dev/sdb1) and save
  ```
- Verify Mount:
  ```
  df -h to check if /opt/local-path-provisioner/
  ```

### Things to do Before Installation
1. Need to register the domain, in our case on AWS and route the DNS to the Load Balancer VM IP and with that domain name.
2. Need to create the SSL/TLS certificate with the below commands and need to use that cert and priv key for LB_Ingres Private (named - privkey.pem) and Public Key (named - fullchain.pem).
```
docker run -it --entrypoint=/bin/sh --rm -v "$(pwd)/letsencrypt:/etc/letsencrypt" -v "$(pwd)/lib/letsencrypt:/var/lib/letsencrypt" certbot/certbot
**In Shell**
certbot certonly --manual --preferred-challenges dns -d "*.<domain>" --agree-tos --email example@example.com
```
3. Then need to create Patient Monitor certificates as named below with the openssl commands
- intermediateCA.crt
- consumerLeaf1.key
- consumerLeaf1.crt
```
openssl genrsa -out ca.key 2048
openssl req -x509 -new -nodes -key ca.key -sha256 -days 3650 -out intermediateCA.crt
openssl genrsa -out consumerLeaf1.key 2048
openssl req -new -key consumerLeaf1.key -out server.csr
openssl x509 -req -in server.csr -CA intermediateCA.crt -CAkey ca.key -CAcreateserial -outconsumerLeaf1.crt -days 365 -sha256
```
4. Need to create one env file with the given [.env](.env) example.
5. Now need to make sure that these files .env, consumerLeaf1.crt, consumerLeaf1.key, fullchain.pem, intermediateCA.crt, privkey.pem, and Vmkeys are in the current working directory from where you are running the installation.