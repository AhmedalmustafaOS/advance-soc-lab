# QRadar Notes

Important notes on installing and configuring QRadar CE...



# QRadar Notes

## Overview
This document contains important notes related to the installation and configuration of IBM QRadar Community Edition (CE) as part of the SOC lab project.

---

## 🛠️ Installation Steps

1. **Download ISO**  
   - Downloaded QRadar CE ISO from the [official IBM website](https://www.ibm.com/products/qradar-siem/community-edition).
   
2. **System Requirements**  
   - Minimum 16 GB RAM  
   - 250 GB Disk  
   - 4 CPUs  
   - Installed on VirtualBox / VMware

3. **Installation Process**  
   - Created a new VM  
   - Mounted the ISO  
   - Followed the installation wizard  
   - Set root password and network configurations

---

## ⚙️ Configuration

### 1. Initial Setup
- Accessed the QRadar UI at: `https://<ip-address>`
- Default login:
  - **Username:** `admin`
  - **Password:** `<set during install>`

### 2. Network Configuration
- Configured static IP for stable access
- Example:
  ```bash
  vi /etc/sysconfig/network-scripts/ifcfg-eth0

