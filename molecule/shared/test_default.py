import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")

# have a look at https://testinfra.readthedocs.io/en/latest/modules.html to see the different possible tests


def test_nodejs_is_installed(host):
    nodejs_package = host.package("nodejs")
    assert nodejs_package.is_installed
    assert nodejs_package.version.startswith('16')
