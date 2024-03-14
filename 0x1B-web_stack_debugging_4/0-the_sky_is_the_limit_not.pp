# Script that fixes the server error using nginx

#Increase ULIMIT nuumber
exec { 'fix-for-nginx':
command => 'sed -i  "s/15/4096/" "/etc/default/nginx"',
path	=> ['/usr/local/bin:/bin'],
}

# Restarting Nginx
exec { 'nginx-restart':
command => '/etc/init.d/nginx restart',
path	=> ['/etc/init.d'],
}
