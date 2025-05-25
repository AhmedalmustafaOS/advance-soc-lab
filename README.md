# SOAR Lab Deployment Project (Manual Install - APT)

This repository contains documentation and configuration for a full open-source SOC Lab environment manually installed without Docker. It integrates the following components:


# Components (Updated)
**TheHive** – Case and incident response platform.

**Cortex** – Enrichment engine for observables.

**Synapse** – Optional enrichment pipeline.

**Wazuh** – EDR and log forwarding.

**MISP** – Threat intelligence platform (feeds to TheHive/Cortex).

**QRadar CE** – SIEM solution.

**Cassandra** – Database backend for TheHive.

**Elasticsearch** – Search engine used by TheHive & Cortex.
- **Windows & Linux & ubntuo server endpoints** (to generate and forward security events)
- **Python for automation**
---

## ✅ Installation Method
All components in this lab are installed manually using `apt install` or from official repositories and virtualbox (Qradar SIEM, Wazuh). No Docker or containerization was used.

Tested environment: **Kali Linux + RHEL 8.7 + Windows 10 + Windows Server 2022 (Virtualized)**

---

## 📂 Project Structure

```
Main Project Folder/
│
├── 1-config/                 
│   ├── cortex/               
│   ├── thehive/             
│   ├── synapse/             
│   ├── wazuh/               
│   ├── misp/                # MISP configuration
│   ├── cassandra.yml        
│   └── elasticsearch/       
│
├── 2-install/               
│   ├── cortex/              
│   ├── thehive/             
│   ├── synapse/             
│   ├── wazuh/               
│   ├── misp/                # MISP installation
│   ├── qradar-ce/           
│   ├── cassandra.yml        
│   └── elasticsearch/       
│
├── 3-endpoint/              
│   ├── windows-10/
│   ├── windows-server/
│   ├── rhel/
│   └── kali-linux/
│
└── 4-script/ python 
|
├── architecture.png             # Network/system architecture diagram
└── README.md                    # Main documentation (this file)

---

## 🔧 Setup Summary (Manual)
### 1. Install Java 11:
```bash
sudo apt install openjdk-11-jdk -y
```





**Install wazuh :**

I install on Virtualbox(ova) easy install

🛡️ Wazuh XDR Integration
I installed on Virtualbox (ova) easy installl.
Wazuh has been integrated into the SOC Lab as an open-source Extended Detection and Response (XDR) platform. This addition enhances endpoint visibility and threat detection across the lab environment, working in tandem with our SIEM. Below are the key aspects of the Wazuh integration:
Open-Source XDR Platform: Wazuh serves as a unified EDR/XDR solution that complements the SIEM. As a free, open-source platform, it provides advanced threat detection and security monitoring on endpoints. Wazuh continuously analyzes endpoint activity (e.g. log data, file integrity changes, suspicious behaviors) and detects potential threats in real time. This enables the lab to leverage enterprise-grade endpoint protection and analytics without additional licensing costs.
Endpoint Agents (Windows10 & windows server 2019 & Linux): We deploy the Wazuh agent on all lab endpoints, including the Windows 10 machine and the Kali Linux machine and windows server. These lightweight agents run on each endpoint to collect security telemetry and enforce host-based monitoring. The agents send host logs, events, and alerts to the Wazuh XDR platform for analysis. By having Wazuh agents on both Windows and Linux, the lab ensures full coverage of endpoint data sources, allowing detection of malware, suspicious processes, file integrity anomalies, and other security issues across the different operating systems.
Integration with IBM QRadar SIEM: The Wazuh XDR platform is connected to IBM QRadar SIEM to enrich our centralized analytics. Wazuh is configured to forward its security events and alerts to QRadar (via Syslog or the QRadar API). This means any threat detected by Wazuh on an endpoint is automatically sent to the SIEM for correlation and deeper analysis. By feeding QRadar with Wazuh’s analyzed endpoint data, we enhance the SIEM’s view with advanced host-based analytics. QRadar can ingest Wazuh alerts (using its OSSEC/Wazuh log parsing support) and incorporate them into its offense correlation engine, resulting in more comprehensive threat detection and a unified security monitoring strategy across the SOC Lab.




## 🔗 Integration Workflow
- QRadar sends offenses → TheHive via Synapse
- TheHive sends observables → Cortex for analysis
- Cortex fetches enrichments → MISP threat intel

----------------------------------------------------------------
🖥️ Log Sources Used
- **Windows 10 Workstation** using Wincollect 10 → QRadar
- **Windows Server 2022** using WinCollect 10 → QRadar
- **Kali Linux (Attacker Simulator)** using rSyslog → QRadar
 **Kali Linux (ubntuo)** using rSyslog → QRadar
- **Windows 10 Workstation** using wazuh agent → Wazuh server
- **Windows Server 2022** using wazuh agent → Wazuh server 
These log sources provide real-world telemetry and were used to simulate login failures, file changes, and port scans and any attack .

---

## ✅ How to Use This Project
1. Clone the repository
2. Place your real config files under thehive/, cortex/, misp/, /synapse, /wazuh, /Qradar CE
3. Use the included scripts/init_thehive_user.sh to set up your first admin account
4. Customize and test integrations

---

## 📌 Notes
- Replace all dummy secrets in .conf files
- Ensure services (thehive, cortex, elasticsearch) are running
- Configure TheHive → Cortex integration from UI (or config)
- Use MISP API key in Cortex analyzers if needed

---

## 📝 License
This project is for educational and research purposes.
Based on open-source tools licensed under AGPLv3 and others.

---

## 🙌 Credits
Lab designed and tested manually on bare metal (Kali Linux) and virtualized RHEL, Windows and MACos for .
Created by Ahmedalmustafa Babiker.

---

📣 Ready for publishing on GitHub and LinkedIn as a practical SOC Automation project.

