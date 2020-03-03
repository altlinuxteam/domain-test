.PHONY: vagrantup destroy test images

test:
	ansible-playbook -i hosts.ini main.yml

vagrantup: Vagrantfile
	vagrant up

destroy:
	vagrant destroy -f

images: alt-packer/Makefile
	cd alt-packer; make image target=alt-server headless=false BASE_VERSION=9 TARGET_VERSION=9 VM_TYPE=vbox
	cd alt-packer; make image target=alt-workstation headless=false BASE_VERSION=9 TARGET_VERSION=9 VM_TYPE=vbox

all: vagrantup test

