#!/usr/bin/env bash

apt-get update
apt-get install -y apache2
if ! [ -L /var/www ]; then
  rm -rf /var/www
  ln -fs /vagrant /var/www
fi
touch /var/www/index.html
echo '<html><head></head><body>Hello, World!</body></html>' >> /var/www/index.html
service apache2 reset
