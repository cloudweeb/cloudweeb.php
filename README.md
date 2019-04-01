Ansible Role PHP
=========

[![Build Status](https://travis-ci.com/cloudweeb/cloudweeb.php.svg?branch=master)](https://travis-ci.com/cloudweeb/cloudweeb.php)

Ansible role to install PHP, inspired from [geerlingguy.php](https://github.com/geerlingguy/ansible-role-php) role

Requirements
------------

None

Role Variables
--------------

```YAML
php_version: 7.2              # set PHP version that want to be installed, by default it is not set
php_web_server_enabled: true  # Set true when You have web server installed on server
php_fpm_enabled: false        # Set true when You want to enable PHP-FPM

php_remi_repo_enabled: true   # Enable REMI repo on RHEL OS only
php_sury_repo_enabled: true   # Enable Sury repo on Debian OSs only

php_extra_packages: []        # List of additional PHP packages that you want to install

#php.ini configuration list
php_ini_disable_functions: []
php_ini_expose_php: 'Off'
php_ini_max_execution_time: '30'
php_ini_max_input_time: '60'
php_ini_max_input_vars: '2500'
php_ini_memory_limit: '128M'
php_ini_date_timezone: Asia/Jakarta

# PHP FPM configuration list
php_fpm_listen: '127.0.0.1:9000'
php_fpm_pm: dynamic                   # PHP FPM process manager (dynamic, static, ondemand)
php_fpm_pm_max_children: '50'         # The max number of child processes to be created
php_fpm_pm_start_servers: '5'
php_fpm_pm_min_spare_servers: '5'
php_fpm_pm_max_spare_servers: '20'
php_fpm_pm_max_requests: '4000'       # The number of requests each child process should execute before respawning
php_fpm_pm_process_idle_timeout: 10s  # The number of seconds after which an idle process will be killed

php_fpm_pools:                # List of php-fpm pools that will be set
    # php-fpm pool name
  - name: www
    # php-fpm pool filename
    filename: www.conf
    # php-fpm pool listen address
    listen: /var/run/php-fpm/php-fpm.sock
    # php-fpm pool allowed connect ip
    listen_allowed_clients: '127.0.0.1'
    # additional php-fpm pool environment variables
    env_vars: |
      env[HOSTNAME] = $HOSTNAME
      env[PATH] = /usr/local/bin:/usr/bin:/bin
      env[TMP] = /tmp
      env[TMPDIR] = /tmp
      env[TEMP] = /tmp
    # additional php-fpm pool php config
    extra_php_ini: |
      php_admin_value[error_log] = /var/log/php-fpm/www-error.log
      php_admin_flag[log_errors] = on
      php_admin_value[memory_limit] = 128M

php_web_server_daemon: httpd  # the name of the web server service (httpd, apache2 or nginx)
php_fpm_daemon: php-fpm       # the name of php-fpm service (php-fpm, php7.2-fpm, php5.6-fpm, etc)

php_base_packages:            # php base packages that will be installed
  - php
  - php-cli
  - php-common
  - php-fpm

php_conf_file:                # php.ini file location
  - /etc/php.ini

php_fpm_user: apache          # default php-fpm user
php_fpm_group: apache         # default php-fpm group

php_fpm_listen_owner: nobody  # default php-fpm listen owner
php_fpm_listen_group: nobody  # default php-fpm listen group

php_fpm_pool_conf_path: /etc/php-fpm.d  # php-fpm config dir
```

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      vars:
        php_web_server_enabled: false
        php_fpm_enabled: true

        php_fpm_pools:
          - name: www
            filename: www.conf
            listen: /var/run/php-fpm/php-fpm.sock
            listen_allowed_clients: '127.0.0.1'
            env_vars: |
              env[HOSTNAME] = $HOSTNAME
              env[PATH] = /usr/local/bin:/usr/bin:/bin
              env[TMP] = /tmp
              env[TMPDIR] = /tmp
              env[TEMP] = /tmp

      roles:
        - role: cloudweeb.php

License
-------

BSD/MIT

Author Information
------------------

Agnesius Santo Naibaho
