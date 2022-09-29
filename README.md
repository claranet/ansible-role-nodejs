# Ansible role - nodejs
[![Maintainer](https://img.shields.io/badge/maintained%20by-claranet-e00000?style=flat-square)](https://www.claranet.fr/)
[![License](https://img.shields.io/github/license/claranet/ansible-role-nodejs?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/claranet/ansible-role-nodejs?style=flat-square)](https://github.com/claranet/ansible-role-nodejs/releases)
[![Status](https://img.shields.io/github/workflow/status/claranet/ansible-role-nodejs/Ansible%20Molecule?style=flat-square&label=tests)](https://github.com/claranet/ansible-role-nodejs/actions?query=workflow%3A%22Ansible+Molecule%22)
[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D5-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)
[![Ansible Galaxy](https://img.shields.io/badge/ansible-galaxy-black.svg?style=flat-square&logo=ansible)](https://galaxy.ansible.com/claranet/nodejs)


> :star: Star us on GitHub — it motivates us a lot!

Install and configure NodeJS

## :warning: Requirements

Ansible >= 5

## :zap: Installation

```bash
ansible-galaxy install claranet.nodejs
```

## :gear: Role variables

Variable       | Default value | Description
---------------|---------------|------------
nodejs_version | **null**      | version of nodejs to install. It can be short : "16" ou long : "16.11"

## :arrows_counterclockwise: Dependencies

N/A

## :pencil2: Example Playbook

```yaml
---
- name: Install NodeJS
  hosts: all
  vars:
    nodejs_version: "16"
    nodejs_npm:
      coffeescript: {}
      chance:
        version: "1.1.3"
      enzyme:
        state: absent
    proxy_settings_https_proxy: "https://proxy:3128"
    proxy_settings_http_proxy: "https://proxy:3128"
  roles:
    - claranet.nodejs
```

## :closed_lock_with_key: [Hardening](HARDENING.md)

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
