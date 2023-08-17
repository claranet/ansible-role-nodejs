import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")

# have a look at https://testinfra.readthedocs.io/en/latest/modules.html to see the different possible tests


def test_proxy_is_configured(host):
    assert "https://monproxy:3128" in host.check_output("npm config list")
