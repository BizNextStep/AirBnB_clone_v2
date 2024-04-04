# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Create necessary directories
file { '/data':
  ensure => 'directory',
}

file { '/data/web_static':
  ensure => 'directory',
}

file { '/data/web_static/releases':
  ensure => 'directory',
}

file { '/data/web_static/shared':
  ensure => 'directory',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  content => '<html><head></head><body>Holberton School</body></html>',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => true,
}

# Set ownership of /data folder to ubuntu user and group recursively
exec { 'chown_data_folder':
  command => 'chown -R ubuntu:ubuntu /data',
  path    => '/usr/bin',
  onlyif  => '/usr/bin/test "$(stat -c "%U:%G" /data)" != "ubuntu:ubuntu"',
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current;
    }

    location / {
        try_files \$uri \$uri/ =404;
    }
}
",
  notify  => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure => 'running',
  enable => true,
  require => File['/etc/nginx/sites-available/default'],
}

