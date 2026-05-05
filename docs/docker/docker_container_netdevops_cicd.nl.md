# NetDevOps CI/CD Docker-images

De `netdevops_cicd` images zijn Python-gebaseerde CI/CD-images voor netwerkautomatiseringspipelines waarvoor Ansible niet nodig is.

## Image

- Docker Hub: [bsmeding/netdevops_cicd_ubuntu](https://hub.docker.com/repository/docker/bsmeding/netdevops_cicd_ubuntu/general)
- Source: [docker_containers_netdevops_cicd](https://github.com/bsmeding/docker_containers_netdevops_cicd)
- Buildstatus: [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml)

## Onderhouden distro-tags

| Familie | Actieve tags | Default alias |
| ------- | ------------ | ------------- |
| Ubuntu | `ubuntu2404`, `ubuntu2604` | `ubuntu` -> Ubuntu 26.04 |
| Debian | `debian12`, `debian13` | `debian` -> Debian 13 / Trixie |
| Rocky Linux | `rockylinux8`, `rockylinux9` | `rockylinux` -> Rocky Linux 9 |
| Alpine | `alpine3.22`, `alpine3.23` | `alpine3` -> Alpine 3.23 |

Oudere tags blijven beschikbaar op Docker Hub maar worden niet meer bijgewerkt.

## Meegeleverde tooling

- Netwerkautomatisering: Netmiko, Scrapli, Nornir, NAPALM, ncclient, Paramiko
- Source-of-truth- en CMDB-API's: pynautobot, pynetbox
- API- en configuratievalidatie: JSON Schema, Pydantic, PyYAML, Jinja2, JMESPath, TextFSM, ntc-templates, TTP, pybatfish
- Cisco API-hulpmiddelen: dnacentersdk en wingpy op Python 3.10+-images
- CI en codekwaliteit: pytest, pytest-cov, pytest-xdist, ruff, mypy, yamllint
- API- en CLI-hulpmiddelen: requests, HTTPX, Rich, Typer

## Toepassingen

- Gegenereerde netwerkconfiguraties valideren
- Jinja2-templates en YAML-/JSON-inventorydata testen
- Nornir-, Scrapli-, Netmiko- of NAPALM-workflows in CI draaien
- Nautobot- en NetBox-synchronisaties testen
- CLI-output parsen met TextFSM, ntc-templates of TTP
- Network intent tests en API-responsevalidatie uitvoeren

## Gebruik

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
