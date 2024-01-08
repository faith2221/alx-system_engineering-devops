#!/usr/bin/env bash
# Configuring ssh config file using puppet

file_line { 'etc/ssh/ssh_config':
  ensure  => present,
content => "	
	# SSH client configuration
	Host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
