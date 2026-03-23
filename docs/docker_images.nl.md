---
title: Docker-images
tags:
  - docker
  - ansible
  - cicd
  - automation
  - infrastructure
---

# Docker-images

**bartsmeding IT** onderhoudt meerdere Docker-images, vooral voor Ansible CI/CD-pipelines en netwerk-/infrastructuurapplicaties, met extra’s die passen bij dagelijks gebruik.

---

## Docker CI/CD-images

Deze images zijn bedoeld om Ansible-playbooks, roles en meer te testen. Ze zijn gebaseerd op diverse Linux-distributies met Ansible en andere pakketten vooraf geïnstalleerd, vooral voor **network automation** (NetDevOps). Per distro is er een image zonder versienummer dat altijd de nieuwste release bevat (bijv. `ansible_cicd_debian` is gelijk aan `ansible_cicd_debian13`).

**Momenteel geïnstalleerde Python-pakketten voor netwerk- en CMDB-tests:**

- ansible (versie verschilt per distributie)
- cryptography
- yamllint
- pynautobot
- pynetbox
- jmespath
- netaddr
- pywinrm

**Netwerkautomatisering:**
- netmiko
- ncclient
- scrapli
- napalm
- paramiko
- textfsm
- ntc-templates
- pyats *(pyats niet beschikbaar in alpine- en rocky-images)*

**CI/CD-testen:**
- ansible-lint
- molecule
- molecule-plugins
- pytest
- pytest-ansible

**Cloud/API-automatisering:**
- requests
- boto3
- openstacksdk
- kubernetes

**Hulpmiddelen:**
- jinja2
- passlib

| Container | CI-status | Downloads |
| --------- | ----------- | --------- |
| [ansible_cicd_debian11](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_debian11/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_debian11) |
| [ansible_cicd_debian12](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_debian12/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_debian12) |
| [ansible_cicd_debian13](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_debian13/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_debian13) |
| [ansible_cicd_debian](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_debian/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_debian) |
| [ansible_cicd_rockylinux8](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_rockylinux8/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_rockylinux8) |
| [ansible_cicd_rockylinux9](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_rockylinux9/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_rockylinux9) |
| [ansible_cicd_rockylinux](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_rockylinux/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_rockylinux) |
| [ansible_cicd_ubuntu2004](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_ubuntu2004/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_ubuntu2004) |
| [ansible_cicd_ubuntu2204](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_ubuntu2204/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_ubuntu2204) |
| [ansible_cicd_ubuntu2404](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_ubuntu2404/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_ubuntu2404) |
| [ansible_cicd_ubuntu](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_ubuntu/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_ubuntu) |
| [ansible_cicd_alpine3.20](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_alpine3.20/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_alpine3.20) |
| [ansible_cicd_alpine3.21](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_alpine3.21/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_alpine3.21) |
| [ansible_cicd_alpine3](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_alpine3/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_alpine3) |

---

## Docker-applicaties

Deze images draaien specifieke applicaties met extra’s voor netwerkautomatisering en infrastructuurlabs.

| Container | Omschrijving | CI-status | Downloads |
| --------- | ----------- | --------- | --------- |
| [nautobot](https://hub.docker.com/repository/docker/bsmeding/nautobot/general) | Nautobot inclusief plugins en apps | ![Build](https://github.com/bsmeding/docker_container_nautobot/actions/workflows/build.yml/badge.svg) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/nautobot) |

