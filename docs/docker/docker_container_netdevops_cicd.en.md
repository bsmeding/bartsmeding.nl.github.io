# NetDevOps CI/CD Docker Images

The `netdevops_cicd` images are Python-based CI/CD images for network automation pipelines where Ansible is not required.

## Image

- Docker Hub: [bsmeding/netdevops_cicd_ubuntu](https://hub.docker.com/repository/docker/bsmeding/netdevops_cicd_ubuntu/general)
- Source: [docker_containers_netdevops_cicd](https://github.com/bsmeding/docker_containers_netdevops_cicd)
- Build status: [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml)

## Maintained distro tags

| Family | Active tags | Default alias |
| ------ | ----------- | ------------- |
| Ubuntu | `ubuntu2404`, `ubuntu2604` | `ubuntu` -> Ubuntu 26.04 |
| Debian | `debian12`, `debian13` | `debian` -> Debian 13 / Trixie |
| Rocky Linux | `rockylinux8`, `rockylinux9` | `rockylinux` -> Rocky Linux 9 |
| Alpine | `alpine3.22`, `alpine3.23` | `alpine3` -> Alpine 3.23 |

Older tags remain available on Docker Hub but are no longer updated.

## Included tooling

- Network automation: Netmiko, Scrapli, Nornir, NAPALM, ncclient, Paramiko
- Source-of-truth and CMDB APIs: pynautobot, pynetbox
- API and configuration validation: JSON Schema, Pydantic, PyYAML, Jinja2, JMESPath, TextFSM, ntc-templates, TTP, pybatfish
- CI and code quality: pytest, pytest-cov, pytest-xdist, ruff, mypy, yamllint
- API and CLI helpers: requests, HTTPX, Rich, Typer

## Use cases

- Validate generated network configurations
- Test Jinja2 templates and YAML/JSON inventory data
- Run Nornir, Scrapli, Netmiko, or NAPALM workflows in CI
- Test Nautobot and NetBox synchronization jobs
- Parse CLI output with TextFSM, ntc-templates, or TTP
- Run network intent tests and API response validation

## Usage

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    container:
      image: bsmeding/netdevops_cicd_ubuntu:latest
    steps:
      - uses: actions/checkout@v5
      - run: pytest
      - run: ruff check .
```
