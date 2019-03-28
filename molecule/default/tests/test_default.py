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
    s = host.service('php-fpm')
    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    assert host.socket("unix:///var/run/php-fpm/php-fpm.sock").is_listening
