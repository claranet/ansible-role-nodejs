# Ansible role - nodejs
[![Maintainer](https://img.shields.io/badge/maintained%20by-claranet-e00000?style=flat-square)](https://www.claranet.fr/)
[![License](https://img.shields.io/github/license/claranet/ansible-role-nodejs?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/claranet/ansible-role-nodejs?style=flat-square)](https://github.com/claranet/ansible-role-nodejs/releases)
[![Status](https://img.shields.io/github/actions/workflow/status/claranet/ansible-role-nodejs/molecule.yml?style=flat-square&label=tests&branch=main)](https://github.com/claranet/ansible-role-nodejs/actions?query=workflow%3A%22Ansible+Molecule%22)
[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D2.10-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)
[![Ansible Galaxy](https://img.shields.io/badge/ansible-galaxy-black.svg?style=flat-square&logo=ansible)](https://galaxy.ansible.com/claranet/nodejs)


> :star: Star us on GitHub — it motivates us a lot!

Install and configure NodeJS

## :warning: Requirements

Ansible >= 2.10

## :zap: Installation

```bash
ansible-galaxy install claranet.nodejs
```

## :gear: Role variables

Variable                          | Default value | Required | Description
----------------------------------|---------------|----------|---------------------------------------------------------------------
nodejs_version                    | **undef**     | true     | version of nodejs to install. It can be short : "16" or long : "16.11"
nodejs_npm                        | **{}**      | false    | list of npm packages to install
nodejs_uses_debian_repository     | **false**     | false    | Whether to use the Debian repository or not. It will intall from debian file package by default
nodejs_proxy_settings_https_proxy | **''**      | false    | proxy to use to get https links. Ex: https://proxy:3128
nodejs_proxy_settings_http_proxy  | **''**      | false    | proxy to use to get http links. Ex: https://proxy:3128

If using the short nodejs_version (ex: 16), it will use the NodeSource repository.

If using the short nodejs_version (ex: 16) AND nodejs_uses_debian_repository is true, it will use the Debian Repository.

If using the long nodejs version, it will download the package from NodeSource and install it with dpkg (not all packages are available directly from the repository).


## :arrows_counterclockwise: Dependencies

N/A

## :pencil2: Example Playbook

* Install using deb files

```yaml
---
- name: Install NodeJS With deb files
  hosts: all
  vars:
    nodejs_version: "16.17.1"
    nodejs_npm:
      coffeescript: {}
      chance:
        version: "1.1.3"
      enzyme:
        state: absent
    nodejs_proxy_settings_https_proxy: "https://proxy:3128"
    nodejs_proxy_settings_http_proxy: "https://proxy:3128"
  roles:
    - claranet.nodejs
```

* Install using apt repository

```yaml
---
- name: Install NodeJS With deb files
  hosts: all
  vars:
    nodejs_version: "16"
    nodejs_uses_debian_repository: true
    nodejs_npm:
      coffeescript: {}
      chance:
        version: "1.1.3"
      enzyme:
        state: absent
    nodejs_proxy_settings_https_proxy: "https://proxy:3128"
    nodejs_proxy_settings_http_proxy: "https://proxy:3128"
  roles:
    - claranet.nodejs
```

## :closed_lock_with_key: [Hardening](HARDENING.md)

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
