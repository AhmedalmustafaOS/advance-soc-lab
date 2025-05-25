# Wazuh Installation
A.
I an install Wazuh using a pre-configured OVA (Open Virtual Appliance) file, which simplifies deployment on VMware, VirtualBox, or other virtualization platforms.

📥 Download Wazuh OVA (Official All-in-One Virtual Machine)
🔗 Download Link: "https://bit.ly/wazuh-ova"
👉 Wazuh Prebuilt Virtual Machine (OVA)

B. Steps to install manual Wazuh...

Official Documentation URL:
https://documentation.wazuh.com/current/installation-guide/wazuh-indexer/all-in-one-deployment/all-in-one.html
1. . Install Dependencies:
sudo apt update
sudo apt install -y curl apt-transport-https lsb-release gnupg2

3.  Download the Wazuh Installation Assistant:
curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh
curl -sO https://packages.wazuh.com/4.7/config.yml
sudo bash ./wazuh-install.sh --generate-config-files

4.  Run the All-in-One Installer:
sudo bash ./wazuh-install.sh -a
5.  Start Services:
sudo systemctl daemon-reload
sudo systemctl enable wazuh-indexer wazuh-manager wazuh-dashboard
sudo systemctl start wazuh-indexer wazuh-manager wazuh-dashboard

7. Install Wazuh Agent on the VM (Optional):
To monitor the VM itself:
sudo curl -so /etc/apt/keyrings/wazuh.gpg https://packages.wazuh.com/key/GPG-KEY-WAZUH
echo "deb [signed-by=/etc/apt/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | sudo tee /etc/apt/sources.list.d/wazuh.list
sudo apt update
sudo apt install -y wazuh-agent

8. Register the agent with the Wazuh server 
sudo wazuh-agent register -a <VM_IP> -P "SecretPassword"
9. sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
