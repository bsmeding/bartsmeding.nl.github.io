# Gitea Act Runner met Ansible

# docker_container_gitea_runner_ansible

Deze Docker-image breidt de officiele `gitea/act_runner` image uit met Ansible, Molecule, Docker-ondersteuning en Python-dependencies voor automatisering.

De image is bedoeld voor self-hosted Gitea Actions runners die Ansible-playbooks, roles, linting en Molecule-tests vanuit CI/CD-jobs moeten draaien.

## Image

- Docker Hub: [bsmeding/gitea-act-runner-ansible](https://hub.docker.com/repository/docker/bsmeding/gitea-act-runner-ansible/general)
- Broncode: [docker_container_gitea_runner_ansible](https://github.com/bsmeding/docker_container_gitea_runner_ansible)
- Base image: `gitea/act_runner`

## Meegeleverde tooling

- Ansible Core
- Molecule met Docker-driver
- ansible-lint
- yamllint
- pytest
- Docker CLI
- SSH-clienttooling
- Python-libraries voor NetDevOps- en CMDB-automatisering

## Python-pakketten

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

## Vereiste omgevingsvariabelen

| Variabele | Omschrijving | Voorbeeld |
| --------- | ------------ | --------- |
| `GITEA_INSTANCE_URL` | URL van de Gitea-server | `https://gitea.example.com` |
| `GITEA_RUNNER_TOKEN` | Registratietoken vanuit Gitea | `your_token_here` |
| `GITEA_RUNNER_NAME` | Naam voor deze runner | `my-ansible-runner` |
| `GITEA_RUNNER_LABELS` | Labels die deze runner ondersteunt | `ubuntu-latest:docker` |

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

Maak een `.env`-bestand:

```dotenv
GITEA_INSTANCE_URL=https://gitea.example.com
GITEA_RUNNER_TOKEN=your_token_here
GITEA_RUNNER_NAME=my-ansible-runner
GITEA_RUNNER_LABELS=ubuntu-latest:docker
```

Gebruik dit vanuit `docker-compose.yml`:

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

Start de runner:

```bash
docker compose up -d
```

## Opmerkingen

- De runner registreert zichzelf automatisch bij de eerste start.
- Als `/data/config.yaml` al bestaat, wordt registratie overgeslagen.
- Python-pakketten worden geinstalleerd vanuit `requirements.txt` in de image-repository.
