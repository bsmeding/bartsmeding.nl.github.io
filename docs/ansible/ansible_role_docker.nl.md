# Ansible-role: Docker (`bsmeding.docker`)

Deze Ansible-role installeert Docker op Linux en sluit aan bij andere container-roles. Gebaseerd op [geerlingguy/ansible-role-docker](https://github.com/geerlingguy/ansible-role-docker) met uitbreidingen voor betere integratie en automatisering.

- **GitHub:** [bsmeding/ansible_role_docker](https://github.com/bsmeding/ansible_role_docker)
- **Ansible Galaxy:** [bsmeding.docker](https://galaxy.ansible.com/bsmeding/docker)

---

## Kenmerken
- Installeert Docker CE (Community Edition) of EE (Enterprise Edition)
- Optioneel Docker Compose (plugin of standalone)
- Voegt gebruikers toe aan de groep `docker`
- Zet `docker_uid` en `docker_gid` voor gebruik in andere roles
- Verwijdert Podman op RedHat-gebaseerde systemen
- Ondersteunt Ubuntu, Debian, Rocky Linux, Pop!_OS en Linux Mint
- Configureerbare proxy, repository en daemon-opties

---

## Vereisten
- Linux (Ubuntu, Debian, Rocky Linux, enz.)
- Python en Ansible geïnstalleerd

---

## Role-variabelen (veelgebruikt)
Hieronder een selectie. Zie het [role-README](https://github.com/bsmeding/ansible_role_docker#role-variables) voor de volledige lijst.

```yaml
# Docker edition ('ce' for Community Edition, 'ee' for Enterprise Edition)
docker_edition: 'ce'

# List of users to add to the docker group
docker_users: []

# Install Docker Compose plugin?
docker_install_compose_plugin: true

# Install Docker Compose standalone binary?
docker_install_compose: false

# Proxy settings (if needed)
http_proxy: ''
https_proxy: ''
no_proxy: ''

# Manage Docker service
docker_service_manage: true
docker_service_state: started
docker_service_enabled: true
```

---

## Voorbeeld-playbook
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.docker
      vars:
        docker_users:
          - youruser
        docker_install_compose_plugin: true
```

---

## Tips
- Neem `bsmeding.docker` op vóór je container-roles.
- De role zet facts `docker_uid` en `docker_gid` voor downstream roles.
- Geavanceerde configuratie via playbook of inventory.

---

## Meer informatie
- [GitHub-repository](https://github.com/bsmeding/ansible_role_docker)
- [Ansible Galaxy-documentatie](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/docker/documentation/)
- [geerlingguy/ansible-role-docker](https://github.com/geerlingguy/ansible-role-docker) (upstream)

---

*MIT-licentie. Oorspronkelijk van Jeff Geerling, uitgebreid door Bart Smeding.*
