Vagrant.configure(2) do |config|
  config.vm.box = "hashicorp/precise32"
  config.vm.provision :shell, path: "bootstrap.sh"
  config.vm.network "private_network", type: "dhcp"
  config.vm.synced_folder "./", "/var/www/html"
end
