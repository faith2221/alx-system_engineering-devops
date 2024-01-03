#!/usr/bin/env bash
# Configuring ssh config file

file_line { 'Turn off passwd auth':
  ensure  => 'present'
  path    => '/etc/ssh/ssh_config',
  line    => '   PasswordAuthentication no',
  replace =>  true
