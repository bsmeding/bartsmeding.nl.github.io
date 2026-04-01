# Ansible-role: nginx_docker (`bsmeding.nginx_docker`)

NGINX webserver running in docker container

- **GitHub:** [ansible_role_nginx_docker](https://github.com/bsmeding/ansible_role_nginx_docker)
- **Ansible Galaxy:** [bsmeding.nginx_docker](https://galaxy.ansible.com/bsmeding/nginx_docker)
- **Laatste tag:** `1.1.0`

---

## Korte details
- **Role-map:** `ansible_role_nginx_docker`
- **Minimale Ansible-versie:** `2.10`
- **Ondersteunde platformen:** Fedora, Debian, Ubuntu, Alpine, ArchLinux
- **Galaxy-tags:** web, system, nginx

---

## Voorbeeldgebruik
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.nginx_docker
```

---

## Opmerking
Deze pagina is opgebouwd op basis van role-metadata (`meta/main.yml`) en gelijkgetrokken met de repository-structuur.
