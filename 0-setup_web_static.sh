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



# implementing a script that sets up webservers for deployment
package { 'nginx':
  ensure   => 'present',
  provider => 'apt',
} ->
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => 'directory',
} ->
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
} ->
file { '/data/web_static/releases/test/index.html':
  ensure => 'present',
  content => "Testing, testing!!!",
} ->
file { '/data/':
  owner => $new_owner,
  group => $new_group,
} ->
file_line { 'add_hbnb_static_location':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  line   => '    location /hbnb_static/ {\n        alias /data/web_static/current/;\n    }',
  after  => 'error_page 404 /404.html;',
  match  => '^error_page 404 /404\.html;$',
} ->
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
} ->

exec { 'nginx restart':
  path => '/etc/init.d/'
}
