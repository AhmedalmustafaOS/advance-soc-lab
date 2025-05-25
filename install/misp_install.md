# MISP Installation

Steps to install MISP...

step by step manual installations  :

 sudo apt-get install -y \
    curl gcc git gnupg-agent make openssl redis-server zip \
    libyara-dev python3-yara python3-redis python3-zmq \
    mariadb-client mariadb-server \
    apache2 apache2-doc apache2-utils libapache2-mod-php7.2 \
    php7.2 php7.2-cli php7.2-mbstring php-pear php7.2-dev \
    php7.2-json php7.2-xml php7.2-mysql php7.2-opcache php7.2-readline \
    python3-dev python3-pip libpq5 libjpeg-dev libfuzzy-dev ruby asciidoctor \
    libxml2-dev libxslt1-dev zlib1g-dev python3-setuptools expect


###install Apache, MariaDB, and PHP packages and dependencies
###Download and install MISP from GitHub 
```bash
    sudo mkdir -p /var/www/MISP
    sudo chown www-data:www-data /var/www/MISP
    sudo -u www-data git clone https://github.com/MISP/MISP.git /var/www/MISP
    cd /var/www/MISP   
    sudo -u www-data git submodule update --init --recursive
    #######Install required Python libraries (PyMISP and others)
    1- install pymisp
    cd /var/www/MISP/PyMISP
    sudo pip3 install .

     2- installl MIXbox
    cd /var/www/MISP/app/files/scripts
        sudo -u www-data git clone https://github.com/CybOXProject/python-cybox.git
    sudo -u www-data git clone https://github.com/STIXProject/python-stix.git
    cd python-cybox && sudo pip3 install .
    cd ../python-stix && sudo pip3 install .
    3- cd /var/www/MISP/app/files/scripts
    sudo -u www-data git clone https://github.com/CybOXProject/mixbox.git
    cd mixbox && sudo pip3 install .
    ###### Installing Composer and Additional PHP Libraries

    cd /var/www/MISP/app
    sudo -u www-data php composer.phar install
    ########## Copy setup file templates
    sudo -u www-data cp /var/www/MISP/app/Config/bootstrap.default.php /var/www/MISP/app/Config/bootstrap.php
    sudo -u www-data cp /var/www/MISP/app/Config/core.default.php /var/www/MISP/app/Config/core.php
    sudo -u www-data cp /var/www/MISP/app##MISP Installation Guide on Kali Linux and Integration with TheHive and Cortex 
step by step manual installations  :
###install Apache, MariaDB, and PHP packages and dependencies
###Download and install MISP from GitHub 
```bash
    sudo mkdir -p /var/www/MISP
    sudo chown www-data:www-data /var/www/MISP
    sudo -u www-data git clone https://github.com/MISP/MISP.git /var/www/MISP
    cd /var/www/MISP   
    sudo -u www-data git submodule update --init --recursive
    #######Install required Python libraries (PyMISP and others)
    1- install pymisp
    cd /var/www/MISP/PyMISP
    sudo pip3 install .

     2- installl MIXbox
    cd /var/www/MISP/app/files/scripts
        sudo -u www-data git clone https://github.com/CybOXProject/python-cybox.git
    sudo -u www-data git clone https://github.com/STIXProject/python-stix.git
    cd python-cybox && sudo pip3 install .
    cd ../python-stix && sudo pip3 install .
    3- cd /var/www/MISP/app/files/scripts
    sudo -u www-data git clone https://github.com/CybOXProject/mixbox.git
    cd mixbox && sudo pip3 install .
    ###### Installing Composer and Additional PHP Libraries

    cd /var/www/MISP/app/Config/config.default.php /var/www/MISP/app/Config/config.php
    sudo -u www-data cp /var/www/MISP/app/Config/database.default.php /var/www/MISP/app/Config/database.php

    
    1- 
    sudo apt-get install -y rng-tools
    sudo rngd -r /dev/urandom
    3- sudo systemctl enable --now mariadb
    sudo a2dismod status          
    sudo a2enmod ssl rewrite headers
    #################Setting up a default MISP location file 
    4- /etc/apache2/sites-available/misp.conf 

    sudo a2dissite 000-default.conf     
    sudo a2ensite misp.conf          
    sudo systemctl reload apache2
    ############## Set up HTTPS (optional but recommended)
    1- sudo openssl req -newkey rsa:4096 -days 365 -nodes -x509 \
    -subj "/C=XX/ST=YourState/L=YourCity/O=YourOrg/OU=OrgUnit/CN=misp.local" \
    -keyout /etc/ssl/private/misp.local.key -out /etc/ssl/private/misp.local.crt
    ########## MariaDB database counter
    1- sudo mysql -u root -p
    2- CREATE DATABASE misp CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    CREATE USER 'misp'@'localhost' IDENTIFIED BY 'yourpassword';
    GRANT ALL PRIVILEGES ON misp.* TO 'misp'@'localhost';
    FLUSH PRIVILEGES;
    EXIT;
    3- mysql -u misp -p misp < /var/www/MISP/INSTALL/MYSQL.sql
    ####### misp-modules ########
    cd /usr/local/src/
    sudo git clone https://github.com/MISP/misp-modules.git
    cd misp-modules
    sudo pip3 install -r REQUIREMENTS.txt
    sudo pip3 install .      ########### Installing and operating units##########
    sudo -u www-data misp-modules -s & 
    sudo systemctl restart apache2

    sudo -u www-data bash /var/www/MISP/app/Console/worker/start.sh
    sudo systemctl restart apache2
    sudo systemctl status apache2  
    sudo systemctl status mariadb 


