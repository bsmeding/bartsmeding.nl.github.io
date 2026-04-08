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

**b@rtsmeding IT** maintains these **Ansible roles** in the open: they power **labs and demos**, back **training** material, and are reused in **customer engagements** where a maintained, CI-checked baseline beats a one-off script.

If you need **roles extended**, **integrated into your pipeline**, or **matched to your standards**, that is part of our **consultancy** — [get in touch via About](about.md).

---

## Active Ansible roles maintained by Bart Smeding

Below is an updated list of active roles (roles with a real `tasks/main.yml`), with links to [Ansible Galaxy](https://galaxy.ansible.com/ui/standalone/namespaces/1041/), CI status, and download badges.

| Role | Description | CI Status | Downloads |
| ---- | ----------- | --------- | --------- |
| [bsmeding.awx_docker](ansible/ansible_role_awx_docker.md) | Role to Install Ansible AWX (opensource Tower) in Docker container | ![CI Status](https://github.com/bsmeding/ansible_role_awx_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/awx_docker) |
| [bsmeding.container_lab_docker](ansible/ansible_role_container_lab_docker.md) | Role to install container_lab in Docker container | ![CI Status](https://github.com/bsmeding/ansible_role_container_lab_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/container_lab_docker) |
| [bsmeding.docker](ansible/ansible_role_docker.md) | Docker for Linux, Forked from geerlingguy.docker. | ![CI Status](https://github.com/bsmeding/ansible_role_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/docker) |
| [bsmeding.gitea_runner](ansible/ansible_role_gitea_runner.md) | Gitea ACT Runner running in docker container | ![CI Status](https://github.com/bsmeding/ansible_role_gitea_runner/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/gitea_runner) |
| [bsmeding.gitlab_docker](ansible/ansible_role_gitlab_ce_docker.md) | Manage and run the gitlab ce docker container with Postgres container as backend. | ![CI Status](https://github.com/bsmeding/ansible_role_gitlab_ce_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/gitlab_docker) |
| [bsmeding.install_development_workstation](ansible/ansible_role_install_development_workstation.md) | Set up a development workstation on macOS and Ubuntu with comprehensive development tools | ![CI Status](https://github.com/bsmeding/ansible_role_install_development_workstation/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/install_development_workstation) |
| [bsmeding.iptv_analyzer](ansible/ansible_role_iptv_analyzer.md) | Ansible role to install IPTV Analyzer (https://github.com/bsmeding/IPTV-Analyzer) with Ansible. Original made by netoptimizer / Jesper Dangaard Brouer | ![CI Status](https://github.com/bsmeding/ansible_role_iptv_analyzer/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/iptv_analyzer) |
| [bsmeding.librechat_docker](ansible/ansible_role_librechat_docker.md) | Deploy LibreChat (ChatGPT-style UI with multi-provider AI) via Docker Compose | ![CI Status](https://github.com/bsmeding/ansible_role_librechat_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/librechat_docker) |
| [bsmeding.nautobot_docker](ansible/ansible_role_nautobot_docker.md) | Role to install Nautobot CMDB in Docker container | ![CI Status](https://github.com/bsmeding/ansible_role_nautobot_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/nautobot_docker) |
| [bsmeding.nginx_docker](ansible/ansible_role_nginx_docker.md) | NGINX webserver running in docker container | ![CI Status](https://github.com/bsmeding/ansible_role_nginx_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/nginx_docker) |
| [bsmeding.ollama](ansible/ansible_role_ollama.md) | Deploy Ollama on Linux (local LLM inference server) | ![CI Status](https://github.com/bsmeding/ansible_role_ollama/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/ollama) |
| [bsmeding.openwebui_docker](ansible/ansible_role_openwebui_docker.md) | Deploy Open WebUI (web interface for Ollama) via Docker container | ![CI Status](https://github.com/bsmeding/ansible_role_openwebui_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/openwebui_docker) |
| [bsmeding.swag_docker](ansible/ansible_role_swag_docker.md) | Secure Web Application Gateway (SWAG) running in docker container | ![CI Status](https://github.com/bsmeding/ansible_role_swag_docker/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/swag_docker) |
| [bsmeding.tig_stack_docker](ansible/ansible_role_tig_stack_containers.md) | Ansible Role to install Telegraf, InfluxDB and Grafana (TIG) as docker containers | ![CI Status](https://github.com/bsmeding/ansible_role_tig_stack_containers/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/tig_stack_docker) |
| [bsmeding.webmin](ansible/ansible-role-webmin.md) | Ansible role to install and configure Webmin. | ![CI Status](https://github.com/bsmeding/ansible-role-webmin/actions/workflows/ci.yml/badge.svg) | ![Ansible Role](https://img.shields.io/ansible/role/d/bsmeding/webmin) |

---

## Ansible collections maintained by Bart Smeding

I am also working on Ansible collections to group related roles, modules, and plugins for easier reuse and distribution.

*More information and links to collections will be added here soon!*
