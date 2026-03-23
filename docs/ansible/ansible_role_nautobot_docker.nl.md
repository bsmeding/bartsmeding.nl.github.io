# Ansible-role: Nautobot Docker (`bsmeding.nautobot_docker`)

Deze Ansible-role deployt Nautobot (Network Source of Truth) in een Docker-container. Geschikt voor labs, demo’s of productie.

- **GitHub:** [bsmeding/ansible_role_nautobot_docker](https://github.com/bsmeding/ansible_role_nautobot_docker)
- **Ansible Galaxy:** [bsmeding.nautobot_docker](https://galaxy.ansible.com/bsmeding/nautobot_docker)

---

## Kenmerken
- Nautobot met afhankelijkheden (Postgres, Redis) in Docker
- Plugins, LDAP, eigen configuratie
- Admin-credentials en API-token instelbaar
- Persistentie via volumes
- Combineert met Docker, Nginx, AWX, enz.

---

## Vereisten
- Linux met Docker (role `bsmeding.docker`)
- Python en Ansible

---

## Veelgebruikte variabelen
Zie [role-README](https://github.com/bsmeding/ansible_role_nautobot_docker#role-variables).

```yaml
# Name of the container
nautobot__name: nautobot

# Docker image to use
nautobot__image: nautobot:2.3

# HTTP/HTTPS ports
nautobot__port_http: 8080
nautobot__port_https: 8444

# Admin credentials
nautobot__superuser_name: admin
nautobot__superuser_password: admin
nautobot__superuser_api_token: "1234567890abcdefghijklmnopqrstuvwxyz"

# Enable/disable internal Postgres/Redis
nautobot__install_own_postgres_db: true

# Volumes to mount
nautobot__directory_volumes:
  - "{{ nautobot__home }}/logs:/var/log/nautobot"
  - "{{ nautobot__home }}/media:/opt/nautobot/media"
  - "{{ nautobot__home }}/jobs:/opt/nautobot/jobs"
  - "{{ nautobot__home }}/static:/opt/nautobot/static"

# Plugins
nautobot__plugins: []
```

---

## Voorbeeld-playbook
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.docker
    - role: bsmeding.nautobot_docker
      vars:
        nautobot__superuser_name: admin
        nautobot__superuser_password: admin
        nautobot__superuser_api_token: "myapitoken"
```

---

## Tips
- Gebruik `bsmeding.docker` eerst.
- Zet `nautobot__install_own_postgres_db: false` voor externe Postgres.
- Zie [role-README](https://github.com/bsmeding/ansible_role_nautobot_docker#role-variables).

---

## Meer informatie
- [GitHub-repository](https://github.com/bsmeding/ansible_role_nautobot_docker)
- [Ansible Galaxy](https://galaxy.ansible.com/bsmeding/nautobot_docker)

---

*MIT-licentie. Bart Smeding.*
