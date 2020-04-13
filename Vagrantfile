# vi: set ft=ruby
# -*- mode: ruby; -*-

NUM_CONTROLLERS=1
NUM_CLIENTS=1

dcs=NUM_CONTROLLERS - 1
cls=NUM_CLIENTS - 1

common_settings = Hash.new()
common_settings[:local_boxes] = nil

dc_settings = Hash.new()
dc_settings[:range] = (0..0)
dc_settings[:memory] = 1024
dc_settings[:cpus] = 1
dc_settings[:vm_name] = "ALT Linux Server 9 (p9)"

cl_settings = Hash.new()
cl_settings[:range] = (0..0)
cl_settings[:memory] = 1024
cl_settings[:cpus] = 1
cl_settings[:vm_name] = "ALT Linux Workstation 9 (p9)"

Vagrant.configure("2") do |config|
  (0..dcs).each_with_index do |n, ndx|
    config.vm.define "dc#{n}" do |dc|
      dc.vm.network "private_network", ip: "10.64.6.%s" % [10+n], netmask: 24, virtualbox__intnet: "intnet"
      if common_settings[:local_boxes]
        dc.vm.box_url = "file://./alt-packer/results/vbox-alt-server-9-x86_64.box"
      else
        dc.vm.box = "BaseALT/alt-server-9-amd64"
        dc.vm.box_version = "1.2.0"
      end
      dc.vm.synced_folder ".", "/vagrant", disabled: true
      dc.vm.hostname = "dc#{n}"
      dc.vm.post_up_message = "Domain controller dc#{n} was successfully started"
      #dc.vm.boot_timeout = 1200

      dc.vm.provider :virtualbox do |vb|
        vb.gui = true
        vb.name = dc_settings[:name]
        vb.cpus = dc_settings[:cpus]
        vb.memory = dc_settings[:memory]
        # The --vram option allows VirtualBox to start desktop integration.
        # The default setting of 12MB of video RAM prevents this.
        vb.customize [
          "modifyvm", :id,
          "--clipboard", "bidirectional",
          "--vram", "128"
        ]
      end
    end
  end

  (0..cls).each_with_index do |n, ndx|
    config.vm.define "cl#{n}" do |cl|
      cl.vm.network "private_network", ip: "10.64.6.%s" % [100+n], netmask: 24, virtualbox__intnet: "intnet"
      if common_settings[:local_boxes]
        cl.vm.box_url = "file://./alt-packer/results/vbox-alt-workstation-9-x86_64.box"
      else
        cl.vm.box = "BaseALT/alt-workstation-9-amd64"
        cl.vm.box_version = "1.2.0"
      end
      cl.vm.synced_folder ".", "/vagrant", disabled: true
      cl.vm.hostname = "cl#{n}"
      cl.vm.post_up_message = "Domain client cl#{n} was successfully started"
      #cl.vm.boot_timeout = 1200

      cl.vm.provider :virtualbox do |vb|
        vb.gui = true
        vb.name = cl_settings[:name]
        vb.cpus = cl_settings[:cpus]
        vb.memory = cl_settings[:memory]
        # The --vram option allows VirtualBox to start desktop integration.
        # The default setting of 12MB of video RAM prevents this.
        vb.customize [
          "modifyvm", :id,
          "--clipboard", "bidirectional",
          "--vram", "128"
        ]
      end
    end
  end
end

