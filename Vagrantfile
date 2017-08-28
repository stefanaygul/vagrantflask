# -*- mode: ruby -*-
# vi: set ft=ruby ts=2 sw=2 expandtab:
 
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "public_network", ip: "192.168.33.10"
  config.vm.provision "shell", inline: <<-SHELL
   sudo apt-get update
   sudo apt-get -y install build-essential
   sudo apt-get -y install tcl8.5
	
	sudo apt-get install libcurl4-gnutls-dev libexpat1-dev gettext \
  libz-dev libssl-dev
	sudo apt-get -y install git
	sudo apt-get -y install python-pip
	
	git clone https://github.com/stefanaygul/vagrantflask.git
	cd vagrantflask
	sudo pip install virtualenv	
	sudo apt-get install -y python-virtualenv
	sudo pip install Flask
	FLASK_APP=stef.py flask run
 
  SHELL
end

