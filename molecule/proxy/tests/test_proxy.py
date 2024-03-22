import os


def test_proxy_is_configured(host):
    assert "https://monproxy:3128" in host.check_output("npm config ls -l")
