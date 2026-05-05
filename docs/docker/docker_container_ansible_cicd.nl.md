# Ansible CI/CD Docker-images

De `ansible_cicd` images zijn bedoeld voor Ansible-playbooks, roles, Molecule, linting en netwerkautomatiseringstests in CI/CD-pipelines.

## Image

- Docker Hub: [bsmeding/ansible_cicd_ubuntu](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_ubuntu/general)
- Source: [docker_containers_ansible_cicd](https://github.com/bsmeding/docker_containers_ansible_cicd)
- Buildstatus: [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml)

## Onderhouden distro-tags

| Familie | Actieve tags | Default alias |
| ------- | ------------ | ------------- |
| Ubuntu | `ubuntu2404`, `ubuntu2604` | `ubuntu` -> Ubuntu 26.04 |
| Debian | `debian12`, `debian13` | `debian` -> Debian 13 / Trixie |
| Rocky Linux | `rockylinux8`, `rockylinux9` | `rockylinux` -> Rocky Linux 9 |
| Alpine | `alpine3.22`, `alpine3.23` | `alpine3` -> Alpine 3.23 |

Oudere tags blijven beschikbaar op Docker Hub maar worden niet meer bijgewerkt.

## Meegeleverde tooling

- Ansible, ansible-lint, Molecule, molecule-plugins, pytest, pytest-ansible
- Netwerkautomatisering: Netmiko, ncclient, Scrapli, NAPALM, Paramiko, TextFSM, ntc-templates
- CMDB- en source-of-truth-clients: pynautobot, pynetbox
- Data- en automatiseringslibraries: cryptography, yamllint, JMESPath, netaddr, pywinrm, requests, boto3, openstacksdk, kubernetes, Jinja2, passlib
- Systemd-support voor Molecule op Debian-, Ubuntu- en Rocky Linux-images

pyATS is niet beschikbaar in Alpine- en Rocky Linux-varianten.

## Gebruik

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    container:
      image: bsmeding/ansible_cicd_ubuntu:latest
    steps:
      - uses: actions/checkout@v5
      - run: ansible-lint
      - run: molecule test
```

Gebruik een versie-specifiek image zoals `bsmeding/ansible_cicd_debian12:latest` wanneer een pipeline een specifieke OS-versie moet volgen.
