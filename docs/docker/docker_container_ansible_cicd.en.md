# Ansible CI/CD Docker Images

The `ansible_cicd` images are built for Ansible playbook, role, Molecule, linting, and network automation testing in CI/CD pipelines.

## Image

- Docker Hub: [bsmeding/ansible_cicd_ubuntu](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_ubuntu/general)
- Source: [docker_containers_ansible_cicd](https://github.com/bsmeding/docker_containers_ansible_cicd)
- Build status: [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml)

## Maintained distro tags

| Family | Active tags | Default alias |
| ------ | ----------- | ------------- |
| Ubuntu | `ubuntu2404`, `ubuntu2604` | `ubuntu` -> Ubuntu 26.04 |
| Debian | `debian12`, `debian13` | `debian` -> Debian 13 / Trixie |
| Rocky Linux | `rockylinux8`, `rockylinux9` | `rockylinux` -> Rocky Linux 9 |
| Alpine | `alpine3.22`, `alpine3.23` | `alpine3` -> Alpine 3.23 |

Older tags remain available on Docker Hub but are no longer updated.

## Included tooling

- Ansible, ansible-lint, Molecule, molecule-plugins, pytest, pytest-ansible
- Network automation libraries: Netmiko, ncclient, Scrapli, NAPALM, Paramiko, TextFSM, ntc-templates
- CMDB and source-of-truth clients: pynautobot, pynetbox
- Data and automation libraries: cryptography, yamllint, JMESPath, netaddr, pywinrm, requests, boto3, openstacksdk, kubernetes, Jinja2, passlib
- Systemd support for Molecule on Debian, Ubuntu, and Rocky Linux images

pyATS is not available in Alpine and Rocky Linux variants.

## Usage

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

Use a version-specific image such as `bsmeding/ansible_cicd_debian12:latest` when a pipeline must match a specific OS version.
