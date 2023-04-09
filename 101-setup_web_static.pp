# implementing a script that sets up webservers for deployment
package { 'nginx':
  ensure   => 'present',
  provider => 'apt',
} ->
file { '/data':
  ensure  => 'directory'
} ->

file { '/data/web_static':
  ensure => 'directory'
} ->

file { '/data/web_static/releases':
  ensure => 'directory'
} ->

file { '/data/web_static/releases/test':
  ensure => 'directory'
} ->

file { '/data/web_static/shared':
  ensure => 'directory'
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
