# Ansible-role: AWX Docker (`bsmeding.awx_docker`)

Deze Ansible-role deployt AWX (open-source Ansible Tower) in Docker-containers. Bedoeld voor eenvoudige, geautomatiseerde AWX-implementaties in lab, demo of productie.

- **GitHub:** [bsmeding/ansible_role_awx_docker](https://github.com/bsmeding/ansible_role_awx_docker)
- **Ansible Galaxy:** [bsmeding.awx_docker](https://galaxy.ansible.com/bsmeding/awx_docker)

---

## Kenmerken
- Deployt AWX, Postgres en Redis in Docker
- Admin-credentials en poorten instelbaar
- Volumes voor persistente data
- Ondersteuning voor organisaties, teams en LDAP
- Combineert met andere roles (bijv. Docker, Nginx, Nautobot)

---

## Vereisten
- Linux met Docker (gebruik role `bsmeding.docker`)
- Python en Ansible

---

## Veelgebruikte variabelen
Zie het [role-README](https://github.com/bsmeding/ansible_role_awx_docker#role-variables) voor alle opties.

```yaml
# Admin credentials
awx__admin_user: admin
awx__admin_password: password

# Web ports
awx__port_web_http: 9080
awx__port_web_https: 9443

# Postgres credentials
awx__postgres_username: awxpguser
awx__postgres_password: awxpgpass
awx__postgres_db: awx

# Host root directory
awx__host_root: /opt/awx

# Volumes to mount
awx__project_data_dir: "{{ awx__host_root }}/projects"
awx__docker_compose_dir: "{{ awx__host_root }}/docker_compose"

# AWX version
awx__version: 17.1.0
```

---

## Voorbeeld-playbook
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.docker
    - role: bsmeding.awx_docker
      vars:
        awx__admin_user: admin
        awx__admin_password: password
```

---

## Tips
- Combineer met `bsmeding.docker` zodat Docker aanwezig is.
- Zie [role-README](https://github.com/bsmeding/ansible_role_awx_docker#role-variables) voor geavanceerde opties.

---

## Meer informatie
- [GitHub-repository](https://github.com/bsmeding/ansible_role_awx_docker)
- [Ansible Galaxy](https://galaxy.ansible.com/bsmeding/awx_docker)

---

*MIT-licentie. Bart Smeding.*
