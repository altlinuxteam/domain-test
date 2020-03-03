# Samba integration testing environment

## Contents

* [Quickstart](#quickstart)
* [Dependencies](#dependencies)
* [Work process](#work-process)

* * *

## Quickstart

```
make all
```

or longer:

```
make vagrantup
make test
```

## Dependencies

* sshpass
* ansible
* vagrant
* virtualbox
* packer

## Work process

Clone the repository with submodules:

```
git clone git@github.com:altlinuxteam/samba-itest.git
cd samba-itest
git submodule update --init --recursive
```

Then build the necessary images for testing:

```
cd alt-packer
make image target=alt-server headless=false BASE_VERSION=9 TARGET_VERSION=9 VM_TYPE=vbox
make image target=alt-workstation headless=false BASE_VERSION=9 TARGET_VERSION=9 VM_TYPE=vbox
```

Then you may deploy the Vagrant virtual machines and run integration
tests or experiment on Samba configuration:

```
cd ..
make vagrantup
make test
```

