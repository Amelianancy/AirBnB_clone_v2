#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static

apt upgrade -y
apt-get install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Testing, testing!!!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/  /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/error_page 404 \/404\.html;/i \    location \/hbnb_static\/ {\n        alias \/data\/web_static\/current\/;\n    }' /etc/nginx/sites-enabled/default
service nginx restart
