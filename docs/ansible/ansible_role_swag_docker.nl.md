# Ansible-role: swag_docker (`bsmeding.swag_docker`)

Secure Web Application Gateway (SWAG) running in docker container

- **GitHub:** [ansible_role_swag_docker](https://github.com/bsmeding/ansible_role_swag_docker)
- **Ansible Galaxy:** [bsmeding.swag_docker](https://galaxy.ansible.com/bsmeding/swag_docker)
- **Laatste tag:** `1.4.0`

---

## Korte details
- **Role-map:** `ansible_role_swag_docker`
- **Minimale Ansible-versie:** `2.10`
- **Ondersteunde platformen:** Fedora, Debian, Ubuntu, Alpine, ArchLinux
- **Galaxy-tags:** web, system, nginx, letsencrypt, swag, docker

---

## Voorbeeldgebruik
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.swag_docker
```

---

## Opmerking
Deze pagina is opgebouwd op basis van role-metadata (`meta/main.yml`) en gelijkgetrokken met de repository-structuur.
