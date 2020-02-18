.PHONY: all

all:
	ansible-playbook -i hosts.ini main.yml

