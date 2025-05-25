# TheHive Installation

Steps to install TheHive...

sudo apt install openjdk-11-jdk -y

wget -qO -  https://downloads.apache.org/cassandra/KEYS | sudo gpg --dearmor  -o  /usr/share/keyrings/cassandra-archive.gpg 
    echo "deb [signed-by=/usr/share/keyrings/cassandra-archive.gpg] https://debian.cassandra.apache.org 40x main" |  sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
    sudo apt update
    sudo apt install cassandra 
    sudo mkdir -p /opt/thp/thehive/files 
    chown -R thehive:thehive /opt/thp/thehive/files
    wget -O- https://raw.githubusercontent.com/StrangeBeeCorp/Security/main/PGP%20keys/packages.key | sudo gpg --dearmor -o /usr/share/keyrings/strangebee-archive-keyring.gpg
    echo 'deb [arch=all signed-by=/usr/share/keyrings/strangebee-archive-keyring.gpg] https://deb.strangebee.com thehive-5.4 main' |sudo tee -a /etc/apt/sources.list.d/strangebee.list
    sudo apt-get update
    sudo apt-get install -y thehive
