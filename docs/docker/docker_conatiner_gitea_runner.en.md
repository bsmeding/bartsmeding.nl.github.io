# Gitea Act Runner with Ansible

# docker_container_gitea_runner_ansible

This Docker image extends the official `gitea/act_runner` image with Ansible, Molecule, Docker support, and Python automation dependencies.

It is intended for self-hosted Gitea Actions runners that need to run Ansible playbooks, roles, linting, and Molecule tests from CI/CD jobs.

## Image

- Docker Hub: [bsmeding/gitea-act-runner-ansible](https://hub.docker.com/repository/docker/bsmeding/gitea-act-runner-ansible/general)
- Source: [docker_container_gitea_runner_ansible](https://github.com/bsmeding/docker_container_gitea_runner_ansible)
- Base image: `gitea/act_runner`

## Included tooling

- Ansible Core
- Molecule with Docker driver
- ansible-lint
- yamllint
- pytest
- Docker CLI
- SSH client tooling
- Python libraries for NetDevOps and CMDB automation

## Python packages

- ansible-core
- molecule
- molecule-plugins[docker]
- ansible-lint
- yamllint
- jinja2
- pyyaml
- packaging
- rich
- paramiko
- cryptography
- pytest
- netaddr
- pynautobot
- pynetbox
- jmespath

## Required environment variables

| Variable | Description | Example |
| -------- | ----------- | ------- |
| `GITEA_INSTANCE_URL` | URL of your Gitea server | `https://gitea.example.com` |
| `GITEA_RUNNER_TOKEN` | Registration token from Gitea | `your_token_here` |
| `GITEA_RUNNER_NAME` | Name for this runner | `my-ansible-runner` |
| `GITEA_RUNNER_LABELS` | Labels this runner supports | `ubuntu-latest:docker` |

## Docker run

```bash
docker run -d \
  --name gitea-ansible-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v gitea_runner_data:/data \
  -e GITEA_INSTANCE_URL=https://gitea.example.com \
  -e GITEA_RUNNER_TOKEN=your_token_here \
  -e GITEA_RUNNER_NAME=my-ansible-runner \
  -e GITEA_RUNNER_LABELS=ubuntu-latest:docker \
  bsmeding/gitea-act-runner-ansible:latest
```

## Docker Compose

Create a `.env` file:

```dotenv
GITEA_INSTANCE_URL=https://gitea.example.com
GITEA_RUNNER_TOKEN=your_token_here
GITEA_RUNNER_NAME=my-ansible-runner
GITEA_RUNNER_LABELS=ubuntu-latest:docker
```

Use it from `docker-compose.yml`:

```yaml
version: "3"

services:
  gitea-ansible-runner:
    image: bsmeding/gitea-act-runner-ansible:latest
    container_name: gitea-ansible-runner
    restart: unless-stopped
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - gitea_runner_data:/data
    env_file:
      - .env

volumes:
  gitea_runner_data:
```

Start the runner:

```bash
docker compose up -d
```

## Notes

- The runner registers automatically on first run.
- If `/data/config.yaml` already exists, registration is skipped.
- Python packages are installed from the image repository `requirements.txt`.
