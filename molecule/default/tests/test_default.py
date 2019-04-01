import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_service(host):
    if host.system_info.distribution == 'debian':
        phpfpm = 'php7.2-fpm'
    elif host.system_info.distribution == 'centos':
        phpfpm = 'php-fpm'

    s = host.service(phpfpm)
    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    assert host.socket("tcp://127.0.0.1:9101").is_listening
