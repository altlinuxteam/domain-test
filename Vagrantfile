# vi: set ft=ruby
# -*- mode: ruby; -*-

NUM_CONTROLLERS=1
NUM_CLIENTS=1

dcs=NUM_CONTROLLERS - 1
cls=NUM_CLIENTS - 1

Vagrant.configure("2") do |config|
  (0..dcs).each_with_index do |n, ndx|
    config.vm.define "dc#{n}" do |dc|
      dc.vm.network "private_network", ip: "10.64.6.%s" % [10+n], netmask: 24, virtualbox__intnet: "intnet"
      dc.vm.box = "BaseALT/alt-server-9-x86_64"
      dc.vm.box_url = "file://./results/vbox-alt-server-9-x86_64.box"
      #dc.vm.box_version = "1.0.0"
      dc.vm.synced_folder ".", "/vagrant", disabled: true
      #dc.vm.box_download_checksum = "db0d0f26575bafd0bb4989dc00d85539e0fd9272c943b373ebbb6d978a3c15ee"
      #dc.vm.box_download_checksum_type = "sha256"
      dc.vm.post_up_message = "Domain controller dc#{n} was successfully started"
    end
  end

  (0..cls).each_with_index do |n, ndx|
    config.vm.define "cl#{n}" do |cl|
      cl.vm.network "private_network", ip: "10.64.6.%s" % [100+n], netmask: 24, virtualbox__intnet: "intnet"
      cl.vm.box = "BaseALT/alt-workstaion-9-x86_64"
      #cl.vm.box_version = "1.0.0"
      cl.vm.box_url = "file://./results/vbox-alt-workstation-9-x86_64.box"
      cl.vm.synced_folder ".", "/vagrant", disabled: true
      cl.vm.post_up_message = "Domain client cl#{n} was successfully started"
    end
  end
end

