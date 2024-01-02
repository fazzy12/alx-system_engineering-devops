# 1-user_limit.pp

# Increase file descriptor limit for holberton user
exec { 'increase_file_limit_for_holberton':
  command => 'echo "holberton soft nofile 65535" >> /etc/security/limits.conf
   && echo "holberton hard nofile 65535" >> /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'grep -q "^holberton" /etc/security/limits.conf',
}

# Reload session to apply new limits
exec { 'reload_session':
  command     => 'su - holberton -c "exec bash"',
  refreshonly => true,
  subscribe   => Exec['increase_file_limit_for_holberton'],
}
