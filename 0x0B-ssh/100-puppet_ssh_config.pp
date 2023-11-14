# Puppet manifest for SSH client configuration

file { '/home/your_username/.ssh/config':
  ensure  => present,
  content => "
    Host your_server_alias
      HostName your_server_ip
      User ubuntu
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
      PreferredAuthentications publickey
  ",
}
