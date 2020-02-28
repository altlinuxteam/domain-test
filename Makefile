.PHONY: vagrantup destroy test

test:
	ansible-playbook -i hosts.ini main.yml

vagrantup: Vagrantfile
	vagrant up

destroy:
	vagrant destroy -f

all: vagrantup test

