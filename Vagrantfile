# -*- mode: ruby -*-
# vi: set ft=ruby ts=2 sw=2 expandtab:

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.network :forwarded_port, guest: 5000, host: 5000
  config.vm.provision "shell", inline: <<-SHELL
   sudo apt-get update
   sudo apt-get -y install build-essential
   sudo apt-get -y install tcl8.5

        sudo apt-get install libcurl4-gnutls-dev libexpat1-dev gettext \
  libz-dev libssl-dev
        sudo apt-get -y install git
        sudo apt-get -y install python-pip

        git clone https://github.com/stefanaygul/vagrantflask.git /home/vagrant/vagrantflask
        sudo sh -c "echo FLASK_APP=/home/vagrant/vagrantflask/stef.py >> /etc/environment"
        sudo pip install virtualenv
        sudo apt-get install -y python-virtualenv
        sudo pip install Flask
        export FLASK_APP=/home/vagrant/vagrantflask/stef.py
        flask run

  SHELL
end
