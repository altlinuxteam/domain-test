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
make images
```

Then you may deploy the Vagrant virtual machines and run integration
tests or experiment on Samba configuration:

```
cd ..
make vagrantup
make test
```

