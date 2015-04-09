#!/bin/sh

Vagrant.configure('2') do |config|
  config.vm.box = "precise64"
  config.vm.box_url = 'http://files.vagrantup.com/precise64.box'

  script = <<-SCRIPT
    debconf-set-selections <<< 'mysql-server mysql-server/root_password password MySuperPassword'
    debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password MySuperPassword'

    apt-get -y update
    apt-get -y install mysql-server
    sed -in '/^bind-address/d' /etc/mysql/my.cnf
    service mysql restart

    mysql -uroot -pMySuperPassword -e "DROP DATABASE IF EXISTS thanatos"
    mysql -uroot -pMySuperPassword -e "CREATE DATABASE thanatos"

    mysql -uroot -pMySuperPassword -e "GRANT USAGE ON *.* TO vagrant@'%'"
    mysql -uroot -pMySuperPassword -e "DROP USER vagrant@'%'"

    mysql -uroot -pMySuperPassword -e "CREATE USER vagrant@'%' IDENTIFIED BY 'vagrant'"
    mysql -uroot -pMySuperPassword -e "GRANT ALL PRIVILEGES ON evecomments.* TO vagrant@'%' WITH GRANT OPTION"
  SCRIPT

  config.vm.provision :shell, :inline => script

  config.vm.network "forwarded_port", guest: 3306, host: 3306
end