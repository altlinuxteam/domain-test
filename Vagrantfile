# vi: set ft=ruby
# -*- mode: ruby; -*-

NUM_CONTROLLERS=1
NUM_CLIENTS=1

dcs=NUM_CONTROLLERS - 1
cls=NUM_CLIENTS - 1

common_settings = Hash.new()
common_settings[:local_boxes] = nil
common_settings[:branch] = "9"
common_settings[:winbox] = "./boxes/w2008r2.box"

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
        dc.vm.box_url = "file://./alt-packer/results/vbox-alt-server-#{common_settings[:branch]}-x86_64.box"
      else
        dc.vm.box = "BaseALT/alt-server-#{common_settings[:branch]}-amd64"
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
          "--vram", "128",
          "--nictype1", "Am79C973",
          "--nictype2", "Am79C973"
        ]
        vb.customize [
          "setextradata", "global", "GUI/SuppressMessages", "all"
        ]
      end
    end
  end

  (0..cls).each_with_index do |n, ndx|
    config.vm.define "cl#{n}" do |cl|
      cl.vm.network "private_network", ip: "10.64.6.%s" % [100+n], netmask: 24, virtualbox__intnet: "intnet"
      if common_settings[:local_boxes]
        cl.vm.box_url = "file://./alt-packer/results/vbox-alt-workstation-#{common_settings[:branch]}-x86_64.box"
      else
        cl.vm.box = "BaseALT/alt-workstation-#{common_settings[:branch]}-amd64"
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
          "--vram", "128",
          "--nictype1", "Am79C973",
          "--nictype2", "Am79C973"
        ]
        vb.customize [
          "setextradata", "global", "GUI/SuppressMessages", "all"
        ]
      end
    end
  end

  if File.file?(common_settings[:winbox])
    config.vm.define "clw0" do |clw|
      clw.vm.box = "clw0"
      clw.vm.box_url = "file://#{common_settings[:winbox]}"
      clw.vm.network "private_network", ip: "10.64.6.99", netmask: 24, virtualbox__intnet: "intnet"
      clw.vm.network :forwarded_port, guest: 3389, host: 13389, id: "rdp", auto_correct: true
      clw.vm.network :forwarded_port, guest: 22, host: 2333, id: "ssh", auto_correct: true
      clw.vm.synced_folder ".", "/vagrant", disabled: true
      clw.vm.hostname = "clw0"
      clw.vm.post_up_message = "Domain Windows client clw0 was successfully started"
      clw.vm.boot_timeout = 1200
      clw.vm.guest = :windows
      clw.vm.communicator = "winrm"
      clw.winrm.retry_limit = 30
      clw.winrm.retry_delay = 10
      clw.winrm.username = "vagrant"
      clw.winrm.password = "vagrant"
      clw.windows.halt_timeout = 15

      clw.vm.provider :virtualbox do |vb|
        vb.gui = true
        vb.name = "clw0"
        vb.cpus = 1
        vb.memory = 1024
        # The --vram option allows VirtualBox to start desktop integration.
        # The default setting of 12MB of video RAM prevents this.
        vb.customize [
          "modifyvm", :id,
          "--clipboard", "bidirectional",
          "--vram", "128",
          "--nictype1", "82540EM",
          "--nictype2", "82540EM"
        ]
        vb.customize [
          "setextradata", "global", "GUI/SuppressMessages", "all"
        ]
      end
    end
  end
end

