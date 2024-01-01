# Puppet manifest to fix the Apache 500 error

# Ensure correct permissions for the Apache configuration file
file { '/etc/apache2/apache2.conf':
  ensure => 'file',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0644',
}

# Ensure correct permissions for the web root directory
file { '/var/www/html':
  ensure => 'directory',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

# Restart Apache to apply the changes
service { 'apache2':
  ensure  => 'running',
  enable  => 'true',
  require => File['/etc/apache2/apache2.conf', '/var/www/html'],
}
