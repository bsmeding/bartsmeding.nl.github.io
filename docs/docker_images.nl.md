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

**b@rtsmeding IT** bouwt en onderhoudt deze **Docker-images** zodat teams **consistente Ansible CI/CD** kunnen draaien (Molecule, linting, device-bibliotheken) en **doordachte applicatie-images** (bijv. Nautobot met bruikbare defaults) zonder elke keer basislagen opnieuw uit te vinden.

We gebruiken ze intern en bij **automation delivery**; voor **images afgestemd op uw registry, securitybeleid of pipeline** kunt u bij ons **advies** terecht — zie [Over](about.md).

---

## Docker CI/CD-images


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
| [ansible_cicd_debian12](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_debian12/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_debian12) |
| [ansible_cicd_debian13](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_debian13/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_debian13) |
| [ansible_cicd_debian](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_debian/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_debian) |
| [ansible_cicd_rockylinux8](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_rockylinux8/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_rockylinux8) |
| [ansible_cicd_rockylinux9](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_rockylinux9/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_rockylinux9) |
| [ansible_cicd_rockylinux](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_rockylinux/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_rockylinux) |
| [ansible_cicd_ubuntu2404](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_ubuntu2404/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_ubuntu2404) |
| [ansible_cicd_ubuntu2604](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_ubuntu2604/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_ubuntu2604) |
| [ansible_cicd_ubuntu](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_ubuntu/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_ubuntu) |
| [ansible_cicd_alpine3.22](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_alpine3.22/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_alpine3.22) |
| [ansible_cicd_alpine3.23](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_alpine3.23/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_alpine3.23) |
| [ansible_cicd_alpine3](https://hub.docker.com/repository/docker/bsmeding/ansible_cicd_alpine3/general) | [![Build and Push Ansible Images](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_ansible_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/ansible_cicd_alpine3) |

### NetDevOps CI/CD-images

Deze images zijn bedoeld voor Python-gebaseerde NetDevOps-pipelines waarvoor Ansible niet nodig is. Ze bevatten Netmiko, Scrapli, Nornir, NAPALM, ncclient, Paramiko, Nautobot- en NetBox-API-clients (`pynautobot`, `pynetbox`), pytest, pytest-cov, pytest-xdist, ruff, mypy en yamllint.

Voor API- en configuratievalidatie bevatten ze JSON Schema, Pydantic, PyYAML, Jinja2, JMESPath, TextFSM, ntc-templates, TTP, requests, HTTPX, Rich, Typer en pybatfish. Typische toepassingen zijn het valideren van gegenereerde netwerkconfiguraties, testen van Jinja2-templates, controleren van YAML-/JSON-inventorydata, testen van Nautobot- of NetBox-synchronisaties, valideren van REST API-responses, parsen van CLI-output en uitvoeren van network intent tests in CI/CD.

Ze gebruiken dezelfde distro-tags als de Ansible-images. De default aliases wijzen naar `ubuntu2604`, `debian13`, `rockylinux9` en `alpine3.23`; oudere image-tags blijven beschikbaar maar worden niet meer bijgewerkt.

| Container | CI-status | Downloads |
| --------- | --------- | --------- |
| [netdevops_cicd_ubuntu](https://hub.docker.com/repository/docker/bsmeding/netdevops_cicd_ubuntu/general) | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_ubuntu) |
| [netdevops_cicd_debian](https://hub.docker.com/repository/docker/bsmeding/netdevops_cicd_debian/general) | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_debian) |
| [netdevops_cicd_rockylinux](https://hub.docker.com/repository/docker/bsmeding/netdevops_cicd_rockylinux/general) | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_rockylinux) |
| [netdevops_cicd_alpine3](https://hub.docker.com/repository/docker/bsmeding/netdevops_cicd_alpine3/general) | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_alpine3) |

### AIOps CI/CD-images

Deze images zijn bedoeld om AI-ondersteunde operationele pipelines te testen. Ze bevatten LLM-clients en routers zoals OpenAI, Anthropic en LiteLLM; evaluatieframeworks zoals DeepEval en Ragas; en agent workflow tools zoals LangChain, LangSmith en LangGraph op Python 3.10+-images.

Voor AIOps CI/CD-tests bevatten ze pytest, pytest-asyncio, pytest-cov, ruff, mypy, Pydantic, JSON Schema, PyYAML, Jinja2, python-dotenv, structlog, requests, HTTPX, responses, respx, vcrpy, freezegun, faker, pandas, NumPy, DuckDB, OpenTelemetry SDK, Prometheus API client, pynautobot en pynetbox. Typische toepassingen zijn prompt-regressietests, agent tool-call tests, gestructureerde JSON-outputvalidatie, incident replay, log-/eventclassificatietests, RAG-evaluatie, gemockte Nautobot/NetBox API-tests en CI-controles voor AI-gegenereerde operationele aanbevelingen.

Ze gebruiken dezelfde distro-tags als de Ansible-images. De default aliases wijzen naar `ubuntu2604`, `debian13`, `rockylinux9` en `alpine3.23`; oudere image-tags blijven beschikbaar maar worden niet meer bijgewerkt.

| Container | CI-status | Downloads |
| --------- | --------- | --------- |
| [aiops_cicd_ubuntu](https://hub.docker.com/repository/docker/bsmeding/aiops_cicd_ubuntu/general) | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_ubuntu) |
| [aiops_cicd_debian](https://hub.docker.com/repository/docker/bsmeding/aiops_cicd_debian/general) | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_debian) |
| [aiops_cicd_rockylinux](https://hub.docker.com/repository/docker/bsmeding/aiops_cicd_rockylinux/general) | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_rockylinux) |
| [aiops_cicd_alpine3](https://hub.docker.com/repository/docker/bsmeding/aiops_cicd_alpine3/general) | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_alpine3) |

---

## Docker-applicaties

Deze images draaien specifieke applicaties met extra’s voor netwerkautomatisering en infrastructuurlabs.

| Container | Omschrijving | CI-status | Downloads |
| --------- | ----------- | --------- | --------- |
| [nautobot](docker/docker_conatiner_nautobot.md) | Nautobot inclusief plugins en apps | ![Build](https://github.com/bsmeding/docker_container_nautobot/actions/workflows/build.yml/badge.svg) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/nautobot) |
| [gitea-act-runner-ansible](docker/docker_conatiner_gitea_runner.md) | Gitea Act Runner met Ansible en Python-automatiseringsdependencies | ![Build](https://github.com/bsmeding/docker_container_gitea_runner_ansible/actions/workflows/build.yml/badge.svg) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/gitea-act-runner-ansible) |
| [rat-of-fortune](docker/docker_conatiner_rat_of_fortune.md) | Browsergebaseerd grafisch rad om willekeurig een naam uit een lijst te kiezen | ![Build](https://github.com/bsmeding/docker_container_rat-of-fortune/actions/workflows/docker-publish.yml/badge.svg) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/rat-of-fortune) |

