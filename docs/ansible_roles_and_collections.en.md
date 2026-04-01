---
title: Ansible Roles and Collections
tags:
  - ansible
  - roles
  - collections
  - automation
  - infrastructure
---

# Ansible Roles and Collections

**bartsmeding IT** maintains several Ansible roles and collections, primarily for network, cloud, and infrastructure automation. Many are used in demos, labs, or student environments.

---

## Active Ansible roles maintained by Bart Smeding

Below is an updated list of active roles (roles with a real `tasks/main.yml`), with links to [Ansible Galaxy](https://galaxy.ansible.com/ui/standalone/namespaces/1041/), CI status, and download badges.

| Role | Description | Role page | CI Status | Downloads |
| ---- | ----------- | --------- | --------- | --------- |
| [bsmeding.awx_docker](https://galaxy.ansible.com/bsmeding/awx_docker) | Role to Install Ansible AWX (opensource Tower) in Docker container | [ansible_role_awx_docker](ansible/ansible_role_awx_docker.md) | ![CI Status](https://github.com/bsmeding/ansible_role_awx_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/awx_docker) |
| [bsmeding.container_lab_docker](https://galaxy.ansible.com/bsmeding/container_lab_docker) | Role to install container_lab in Docker container | [ansible_role_container_lab_docker](ansible/ansible_role_container_lab_docker.md) | ![CI Status](https://github.com/bsmeding/ansible_role_container_lab_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/container_lab_docker) |
| [bsmeding.docker](https://galaxy.ansible.com/bsmeding/docker) | Docker for Linux, Forked from geerlingguy.docker. | [ansible_role_docker](ansible/ansible_role_docker.md) | ![CI Status](https://github.com/bsmeding/ansible_role_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/docker) |
| [bsmeding.gitea_runner](https://galaxy.ansible.com/bsmeding/gitea_runner) | Gitea ACT Runner running in docker container | [ansible_role_gitea_runner](ansible/ansible_role_gitea_runner.md) | ![CI Status](https://github.com/bsmeding/ansible_role_gitea_runner/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/gitea_runner) |
| [bsmeding.gitlab_docker](https://galaxy.ansible.com/bsmeding/gitlab_docker) | Manage and run the gitlab ce docker container with Postgres container as backend. | [ansible_role_gitlab_ce_docker](ansible/ansible_role_gitlab_ce_docker.md) | ![CI Status](https://github.com/bsmeding/ansible_role_gitlab_ce_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/gitlab_docker) |
| [bsmeding.install_development_workstation](https://galaxy.ansible.com/bsmeding/install_development_workstation) | Set up a development workstation on macOS and Ubuntu with comprehensive development tools | [ansible_role_install_development_workstation](ansible/ansible_role_install_development_workstation.md) | ![CI Status](https://github.com/bsmeding/ansible_role_install_development_workstation/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/install_development_workstation) |
| [bsmeding.iptv_analyzer](https://galaxy.ansible.com/bsmeding/iptv_analyzer) | Ansible role to install IPTV Analyzer (https://github.com/bsmeding/IPTV-Analyzer) with Ansible. Original made by netoptimizer / Jesper Dangaard Brouer | [ansible_role_iptv_analyzer](ansible/ansible_role_iptv_analyzer.md) | ![CI Status](https://github.com/bsmeding/ansible_role_iptv_analyzer/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/iptv_analyzer) |
| [bsmeding.librechat_docker](https://galaxy.ansible.com/bsmeding/librechat_docker) | Deploy LibreChat (ChatGPT-style UI with multi-provider AI) via Docker Compose | [ansible_role_librechat_docker](ansible/ansible_role_librechat_docker.md) | ![CI Status](https://github.com/bsmeding/ansible_role_librechat_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/librechat_docker) |
| [bsmeding.nautobot_docker](https://galaxy.ansible.com/bsmeding/nautobot_docker) | Role to install Nautobot CMDB in Docker container | [ansible_role_nautobot_docker](ansible/ansible_role_nautobot_docker.md) | ![CI Status](https://github.com/bsmeding/ansible_role_nautobot_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/nautobot_docker) |
| [bsmeding.nginx_docker](https://galaxy.ansible.com/bsmeding/nginx_docker) | NGINX webserver running in docker container | [ansible_role_nginx_docker](ansible/ansible_role_nginx_docker.md) | ![CI Status](https://github.com/bsmeding/ansible_role_nginx_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/nginx_docker) |
| [bsmeding.ollama](https://galaxy.ansible.com/bsmeding/ollama) | Deploy Ollama on Linux (local LLM inference server) | [ansible_role_ollama](ansible/ansible_role_ollama.md) | ![CI Status](https://github.com/bsmeding/ansible_role_ollama/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/ollama) |
| [bsmeding.openwebui_docker](https://galaxy.ansible.com/bsmeding/openwebui_docker) | Deploy Open WebUI (web interface for Ollama) via Docker container | [ansible_role_openwebui_docker](ansible/ansible_role_openwebui_docker.md) | ![CI Status](https://github.com/bsmeding/ansible_role_openwebui_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/openwebui_docker) |
| [bsmeding.swag_docker](https://galaxy.ansible.com/bsmeding/swag_docker) | Secure Web Application Gateway (SWAG) running in docker container | [ansible_role_swag_docker](ansible/ansible_role_swag_docker.md) | ![CI Status](https://github.com/bsmeding/ansible_role_swag_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/swag_docker) |
| [bsmeding.tickg_stack_docker](https://galaxy.ansible.com/bsmeding/tickg_stack_docker) | Ansible Role to install Telegraf, InfluxDB, Chronograf, Kapacitor and Grafana (TICK+G) as docker containers | [ansible_role_tickg_stack_containers](ansible/ansible_role_tickg_stack_containers.md) | ![CI Status](https://github.com/bsmeding/ansible_role_tickg_stack_containers/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/tickg_stack_docker) |
| [bsmeding.tig_stack_docker](https://galaxy.ansible.com/bsmeding/tig_stack_docker) | Ansible Role to install Telegraf, InfluxDB and Grafana (TIG) as docker containers | [ansible_role_tig_stack_containers](ansible/ansible_role_tig_stack_containers.md) | ![CI Status](https://github.com/bsmeding/ansible_role_tig_stack_containers/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/tig_stack_docker) |
| [bsmeding.webmin](https://galaxy.ansible.com/bsmeding/webmin) | Ansible role to install and configure Webmin. | [ansible-role-webmin](ansible/ansible-role-webmin.md) | ![CI Status](https://github.com/bsmeding/ansible-role-webmin/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/webmin) |

---

## Ansible collections maintained by Bart Smeding

I am also working on Ansible collections to group related roles, modules, and plugins for easier reuse and distribution.

*More information and links to collections will be added here soon!*
