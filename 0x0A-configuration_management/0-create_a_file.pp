# 0-create_a_file.pp

# Ensure the /tmp directory exists
file { '/tmp':
  ensure => directory,
}

# Create the /tmp/school file with specified permissions, owner, and content
file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
