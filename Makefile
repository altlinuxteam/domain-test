.PHONY: vagrantup test

all: vagrantup test

vagrantup: Vagrantfile
	vagrant up

test:
	ansible-playbook -i hosts.ini main.yml

