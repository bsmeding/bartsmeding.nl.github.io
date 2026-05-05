---
title: Docker Images
tags:
  - docker
  - ansible
  - cicd
  - automation
  - infrastructure
---

# Docker Images

**b@rtsmeding IT** builds and maintains Docker images for reproducible CI/CD, NetDevOps, AIOps, network automation, and infrastructure lab workflows.

This page is the compact status overview. Detailed package lists, supported distro tags, and usage examples are on the linked image pages.

---

## CI/CD Image Families

### ansible_cicd

[ansible_cicd](docker/docker_container_ansible_cicd.md) images provide Ansible, Molecule, ansible-lint, network automation tools, and CMDB testing dependencies for role and playbook CI/CD.

| Image | Base | CI Status | Downloads |
| ----- | ---- | --------- | --------- |
| `ansible_cicd_ubuntu2004` | Ubuntu 20.04 (legacy) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_ubuntu2004) |
| `ansible_cicd_ubuntu2204` | Ubuntu 22.04 (legacy) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_ubuntu2204) |
| `ansible_cicd_ubuntu2404` | Ubuntu 24.04 | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_ubuntu2404) |
| `ansible_cicd_ubuntu2604` | Ubuntu 26.04 | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_ubuntu2604) |
| `ansible_cicd_ubuntu` | Ubuntu alias | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_ubuntu) |
| `ansible_cicd_debian11` | Debian 11 (legacy) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_debian11) |
| `ansible_cicd_debian12` | Debian 12 | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_debian12) |
| `ansible_cicd_debian13` | Debian 13 | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_debian13) |
| `ansible_cicd_debian` | Debian alias | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_debian) |
| `ansible_cicd_rockylinux8` | Rocky Linux 8 | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_rockylinux8) |
| `ansible_cicd_rockylinux9` | Rocky Linux 9 | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_rockylinux9) |
| `ansible_cicd_rockylinux` | Rocky Linux alias | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_rockylinux) |
| `ansible_cicd_alpine3.20` | Alpine 3.20 (legacy) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_alpine3.20) |
| `ansible_cicd_alpine3.21` | Alpine 3.21 (legacy) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_alpine3.21) |
| `ansible_cicd_alpine3.22` | Alpine 3.22 | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_alpine3.22) |
| `ansible_cicd_alpine3.23` | Alpine 3.23 | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_alpine3.23) |
| `ansible_cicd_alpine3` | Alpine 3 alias | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_alpine3) |

### netdevops_cicd

[netdevops_cicd](docker/docker_container_netdevops_cicd.md) images provide Python NetDevOps tooling such as Netmiko, Scrapli, Nornir, NAPALM, API clients, and configuration validation helpers.

| Image | Base | CI Status | Downloads |
| ----- | ---- | --------- | --------- |
| `netdevops_cicd_ubuntu2404` | Ubuntu 24.04 | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_ubuntu2404) |
| `netdevops_cicd_ubuntu2604` | Ubuntu 26.04 | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_ubuntu2604) |
| `netdevops_cicd_ubuntu` | Ubuntu alias | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_ubuntu) |
| `netdevops_cicd_debian12` | Debian 12 | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_debian12) |
| `netdevops_cicd_debian13` | Debian 13 | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_debian13) |
| `netdevops_cicd_debian` | Debian alias | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_debian) |
| `netdevops_cicd_rockylinux8` | Rocky Linux 8 | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_rockylinux8) |
| `netdevops_cicd_rockylinux9` | Rocky Linux 9 | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_rockylinux9) |
| `netdevops_cicd_rockylinux` | Rocky Linux alias | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_rockylinux) |
| `netdevops_cicd_alpine3.22` | Alpine 3.22 | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_alpine3.22) |
| `netdevops_cicd_alpine3.23` | Alpine 3.23 | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_alpine3.23) |
| `netdevops_cicd_alpine3` | Alpine 3 alias | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_alpine3) |

### aiops_cicd

[aiops_cicd](docker/docker_container_aiops_cicd.md) images provide LLM clients, prompt and agent testing tools, structured output validation, RAG evaluation, and operational replay dependencies.

| Image | Base | CI Status | Downloads |
| ----- | ---- | --------- | --------- |
| `aiops_cicd_ubuntu2404` | Ubuntu 24.04 | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_ubuntu2404) |
| `aiops_cicd_ubuntu2604` | Ubuntu 26.04 | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_ubuntu2604) |
| `aiops_cicd_ubuntu` | Ubuntu alias | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_ubuntu) |
| `aiops_cicd_debian12` | Debian 12 | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_debian12) |
| `aiops_cicd_debian13` | Debian 13 | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_debian13) |
| `aiops_cicd_debian` | Debian alias | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_debian) |
| `aiops_cicd_rockylinux8` | Rocky Linux 8 | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_rockylinux8) |
| `aiops_cicd_rockylinux9` | Rocky Linux 9 | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_rockylinux9) |
| `aiops_cicd_rockylinux` | Rocky Linux alias | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_rockylinux) |
| `aiops_cicd_alpine3.22` | Alpine 3.22 | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_alpine3.22) |
| `aiops_cicd_alpine3.23` | Alpine 3.23 | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_alpine3.23) |
| `aiops_cicd_alpine3` | Alpine 3 alias | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_alpine3) |

The maintained CI/CD images support the latest two distro versions per family: Ubuntu 24.04/26.04, Debian 12/13, Rocky Linux 8/9, and Alpine 3.22/3.23. Older Docker Hub image tags remain available but are no longer updated.

---

## Docker Applications

| Container | Description | CI Status | Downloads |
| --------- | ----------- | --------- | --------- |
| [nautobot](docker/docker_conatiner_nautobot.md) | Nautobot including plugins and apps | ![Build](https://github.com/bsmeding/docker_container_nautobot/actions/workflows/build.yml/badge.svg) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/nautobot) |
| [gitea-act-runner-ansible](docker/docker_conatiner_gitea_runner.md) | Gitea Act Runner with Ansible and Python automation dependencies | ![Build](https://github.com/bsmeding/docker_container_gitea_runner_ansible/actions/workflows/build.yml/badge.svg) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/gitea-act-runner-ansible) |
| [rat-of-fortune](docker/docker_conatiner_rat_of_fortune.md) | Browser-based graphical wheel for randomly selecting a name from a list | ![Build](https://github.com/bsmeding/docker_container_rat-of-fortune/actions/workflows/docker-publish.yml/badge.svg) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/rat-of-fortune) |
