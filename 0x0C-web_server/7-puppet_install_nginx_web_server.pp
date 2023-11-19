# Puppet manifest to install and configure Nginx web server

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx
file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html;

        server_name _;

        location / {
            return 200 'Hello World!';
        }

        location /redirect_me {
            return 301;
        }

        error_page 404 /404.html;
        location = /404.html {
            return 404 'Ceci n\'est pas une page';
        }
    }
  ",
}

# Enable the default site
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
}

# Restart Nginx service
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
