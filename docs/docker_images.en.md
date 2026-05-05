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

**b@rtsmeding IT** builds and maintains these **Docker images** so teams can run **consistent Ansible CI/CD** (Molecule, linting, device libraries) and **opinionated app images** (e.g. Nautobot with useful defaults) without reinventing base layers.

They are what we use internally and in **automation delivery**; if you want **images aligned to your registry, security policy, or pipeline**, we can help through **consultancy** — see [About](about.md).

---

## Docker CI/CD Images


**Currently installed Python packages for network and CMDB testing:**

- ansible (version varies by distribution)
- cryptography
- yamllint
- pynautobot
- pynetbox
- jmespath
- netaddr
- pywinrm

**Network automation:**
- netmiko
- ncclient
- scrapli
- napalm
- paramiko
- textfsm
- ntc-templates
- pyats *(pyats not available in alpine and rocky distros)*

**CI/CD testing:**
- ansible-lint
- molecule
- molecule-plugins
- pytest
- pytest-ansible

**Cloud/API automation:**
- requests
- boto3
- openstacksdk
- kubernetes

**Utilities:**
- jinja2
- passlib

| Container | CI Status   | Downloads |
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

### NetDevOps CI/CD Images

These images are for Python-based NetDevOps pipelines where Ansible is not required. They include Netmiko, Scrapli, Nornir, NAPALM, ncclient, Paramiko, Nautobot and NetBox API clients (`pynautobot`, `pynetbox`), pytest, pytest-cov, pytest-xdist, ruff, mypy, and yamllint.

For API and configuration validation they include JSON Schema, Pydantic, PyYAML, Jinja2, JMESPath, TextFSM, ntc-templates, TTP, requests, HTTPX, Rich, Typer, and pybatfish. Typical use cases are validating generated network configs, testing Jinja2 templates, checking YAML/JSON inventory data, testing Nautobot or NetBox synchronization jobs, validating REST API responses, parsing CLI output, and running network intent tests in CI/CD.

They use the same distro tags as the Ansible images. The default aliases point to `ubuntu2604`, `debian13`, `rockylinux9`, and `alpine3.23`; older image tags remain available but are no longer updated.

| Container | CI Status | Downloads |
| --------- | --------- | --------- |
| [netdevops_cicd_ubuntu](https://hub.docker.com/repository/docker/bsmeding/netdevops_cicd_ubuntu/general) | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_ubuntu) |
| [netdevops_cicd_debian](https://hub.docker.com/repository/docker/bsmeding/netdevops_cicd_debian/general) | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_debian) |
| [netdevops_cicd_rockylinux](https://hub.docker.com/repository/docker/bsmeding/netdevops_cicd_rockylinux/general) | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_rockylinux) |
| [netdevops_cicd_alpine3](https://hub.docker.com/repository/docker/bsmeding/netdevops_cicd_alpine3/general) | [![Build and Push NetDevOps Images](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_netdevops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/netdevops_cicd_alpine3) |

### AIOps CI/CD Images

These images are for testing AI-assisted operational pipelines. They include LLM clients and routers such as OpenAI, Anthropic, and LiteLLM; evaluation frameworks such as DeepEval and Ragas; and agent workflow tools such as LangChain, LangSmith, and LangGraph on Python 3.10+ images.

For AIOps CI/CD testing they include pytest, pytest-asyncio, pytest-cov, ruff, mypy, Pydantic, JSON Schema, PyYAML, Jinja2, python-dotenv, structlog, requests, HTTPX, responses, respx, vcrpy, freezegun, faker, pandas, NumPy, DuckDB, OpenTelemetry SDK, Prometheus API client, pynautobot, and pynetbox. Typical use cases are prompt regression tests, agent tool-call tests, structured JSON output validation, incident replay, log/event classification tests, RAG evaluation, mocked Nautobot/NetBox API tests, and CI checks for AI-generated operational recommendations.

They use the same distro tags as the Ansible images. The default aliases point to `ubuntu2604`, `debian13`, `rockylinux9`, and `alpine3.23`; older image tags remain available but are no longer updated.

| Container | CI Status | Downloads |
| --------- | --------- | --------- |
| [aiops_cicd_ubuntu](https://hub.docker.com/repository/docker/bsmeding/aiops_cicd_ubuntu/general) | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_ubuntu) |
| [aiops_cicd_debian](https://hub.docker.com/repository/docker/bsmeding/aiops_cicd_debian/general) | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_debian) |
| [aiops_cicd_rockylinux](https://hub.docker.com/repository/docker/bsmeding/aiops_cicd_rockylinux/general) | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_rockylinux) |
| [aiops_cicd_alpine3](https://hub.docker.com/repository/docker/bsmeding/aiops_cicd_alpine3/general) | [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/aiops_cicd_alpine3) |

---

## Docker Applications

These images are for running specific applications with enhancements for network automation and infrastructure labs.

| Container | Description | CI Status | Downloads |
| --------- | ----------- | --------- | --------- |
| [nautobot](docker/docker_conatiner_nautobot.md) | Nautobot including plugins and apps | ![Build](https://github.com/bsmeding/docker_container_nautobot/actions/workflows/build.yml/badge.svg) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/nautobot) |
| [gitea-act-runner-ansible](docker/docker_conatiner_gitea_runner.md) | Gitea Act Runner with Ansible and Python automation dependencies | ![Build](https://github.com/bsmeding/docker_container_gitea_runner_ansible/actions/workflows/build.yml/badge.svg) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/gitea-act-runner-ansible) |
| [rat-of-fortune](docker/docker_conatiner_rat_of_fortune.md) | Browser-based graphical wheel for randomly selecting a name from a list | ![Build](https://github.com/bsmeding/docker_container_rat-of-fortune/actions/workflows/docker-publish.yml/badge.svg) | ![Docker Pulls](https://img.shields.io/docker/pulls/bsmeding/rat-of-fortune) |


