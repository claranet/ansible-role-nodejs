import os


def test_nodejs_is_installed(host):
    nodejs_package = host.package("nodejs")
    assert nodejs_package.is_installed
    assert nodejs_package.version.startswith('16')
