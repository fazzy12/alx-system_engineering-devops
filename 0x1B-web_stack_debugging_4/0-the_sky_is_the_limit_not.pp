# 0-the_sky_is_the_limit_not.pp

# Ensure Nginx service is installed and running
package { 'nginx':
  ensure => 'installed',
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}

# Adjust Nginx configuration
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('path_to_nginx_template/nginx.conf.erb'),
  notify  => Service['nginx'],
}
