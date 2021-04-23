exec { 'apt update':
     command  => 'apt-get update',
     path     => /usr/local/bin/:/bin/',
     }

package { 'nginx':
	ensure => 'installed',
	require => Exec['update'],
	}


$str = "add_header X-Served-By ${hostname};"

-> package { 'nginx':
  ensure  => installed,
  require => Exec['update']
}
-> file_line { 'Add redirection, 301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}
-> file_line { 'Add custom HTTP server':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => $str,
}
-> file { '/var/www/html/index.html':
  content => 'Holberton School',
}
-> service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}