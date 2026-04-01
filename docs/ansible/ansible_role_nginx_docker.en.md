# Ansible Role: nginx_docker (`bsmeding.nginx_docker`)

NGINX webserver running in docker container

- **GitHub:** [ansible_role_nginx_docker](https://github.com/bsmeding/ansible_role_nginx_docker)
- **Ansible Galaxy:** [bsmeding.nginx_docker](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/nginx_docker/)

---

## Quick details
- **Role directory:** `ansible_role_nginx_docker`
- **Minimum Ansible version:** `2.10`
- **Supported platforms:** Fedora, Debian, Ubuntu, Alpine, ArchLinux
- **Galaxy tags:** web, system, nginx

---

## Example usage
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.nginx_docker
```

---

## Notes
This page is generated from role metadata (`meta/main.yml`) and kept in sync with the repository layout.
