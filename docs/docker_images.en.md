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

| Container | Description | CI Status | Downloads |
| --------- | ----------- | --------- | --------- |
| [ansible_cicd](docker/docker_container_ansible_cicd.md) | Ansible, Molecule, ansible-lint, network automation, and CMDB testing images | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_ubuntu) |
| [netdevops_cicd](docker/docker_container_netdevops_cicd.md) | Python NetDevOps images with Netmiko, Scrapli, Nornir, NAPALM, API and config validation tools | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_ubuntu) |
| [aiops_cicd](docker/docker_container_aiops_cicd.md) | AIOps evaluation images for LLM clients, prompt tests, agent tests, RAG evaluation, and operational replay | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_ubuntu) |

The maintained CI/CD images support the latest two distro versions per family: Ubuntu 24.04/26.04, Debian 12/13, Rocky Linux 8/9, and Alpine 3.22/3.23. Older Docker Hub image tags remain available but are no longer updated.

---

## Docker Applications

| Container | Description | CI Status | Downloads |
| --------- | ----------- | --------- | --------- |
| [nautobot](docker/docker_conatiner_nautobot.md) | Nautobot including plugins and apps | ![Build](https://github.com/bsmeding/docker_container_nautobot/actions/workflows/build.yml/badge.svg) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/nautobot) |
| [gitea-act-runner-ansible](docker/docker_conatiner_gitea_runner.md) | Gitea Act Runner with Ansible and Python automation dependencies | ![Build](https://github.com/bsmeding/docker_container_gitea_runner_ansible/actions/workflows/build.yml/badge.svg) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/gitea-act-runner-ansible) |
| [rat-of-fortune](docker/docker_conatiner_rat_of_fortune.md) | Browser-based graphical wheel for randomly selecting a name from a list | ![Build](https://github.com/bsmeding/docker_container_rat-of-fortune/actions/workflows/docker-publish.yml/badge.svg) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/rat-of-fortune) |
