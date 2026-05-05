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

**b@rtsmeding IT** bouwt en onderhoudt Docker-images voor reproduceerbare CI/CD, NetDevOps, AIOps, netwerkautomatisering en infrastructuurlabs.

Deze pagina is het compacte statusoverzicht. Gedetailleerde pakketlijsten, ondersteunde distro-tags en gebruiksvoorbeelden staan op de gelinkte image-pagina's.

---

## CI/CD-imagefamilies

| Container | Omschrijving | CI-status | Downloads |
| --------- | ------------ | --------- | --------- |
| [ansible_cicd](docker/docker_container_ansible_cicd.md) | Images met Ansible, Molecule, ansible-lint, netwerkautomatisering en CMDB-tests | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_ubuntu) |
| [netdevops_cicd](docker/docker_container_netdevops_cicd.md) | Python NetDevOps-images met Netmiko, Scrapli, Nornir, NAPALM, API- en configuratievalidatie | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_ubuntu) |
| [aiops_cicd](docker/docker_container_aiops_cicd.md) | AIOps-evaluatie-images voor LLM-clients, prompttests, agenttests, RAG-evaluatie en operationele replay | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_ubuntu) |

De onderhouden CI/CD-images ondersteunen de nieuwste twee distroversies per familie: Ubuntu 24.04/26.04, Debian 12/13, Rocky Linux 8/9 en Alpine 3.22/3.23. Oudere Docker Hub image-tags blijven beschikbaar maar worden niet meer bijgewerkt.

---

## Docker-applicaties

| Container | Omschrijving | CI-status | Downloads |
| --------- | ------------ | --------- | --------- |
| [nautobot](docker/docker_conatiner_nautobot.md) | Nautobot inclusief plugins en apps | ![Build](https://github.com/bsmeding/docker_container_nautobot/actions/workflows/build.yml/badge.svg) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/nautobot) |
| [gitea-act-runner-ansible](docker/docker_conatiner_gitea_runner.md) | Gitea Act Runner met Ansible en Python-automatiseringsdependencies | ![Build](https://github.com/bsmeding/docker_container_gitea_runner_ansible/actions/workflows/build.yml/badge.svg) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/gitea-act-runner-ansible) |
| [rat-of-fortune](docker/docker_conatiner_rat_of_fortune.md) | Browsergebaseerd grafisch rad om willekeurig een naam uit een lijst te kiezen | ![Build](https://github.com/bsmeding/docker_container_rat-of-fortune/actions/workflows/docker-publish.yml/badge.svg) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/rat-of-fortune) |
