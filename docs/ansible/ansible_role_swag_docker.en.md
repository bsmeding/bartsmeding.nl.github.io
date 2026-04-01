# Ansible Role: swag_docker (`bsmeding.swag_docker`)

Secure Web Application Gateway (SWAG) running in docker container

- **GitHub:** [ansible_role_swag_docker](https://github.com/bsmeding/ansible_role_swag_docker)
- **Ansible Galaxy:** [bsmeding.swag_docker](https://galaxy.ansible.com/bsmeding/swag_docker)
- **Latest tag:** `1.4.0`

---

## Quick details
- **Role directory:** `ansible_role_swag_docker`
- **Minimum Ansible version:** `2.10`
- **Supported platforms:** Fedora, Debian, Ubuntu, Alpine, ArchLinux
- **Galaxy tags:** web, system, nginx, letsencrypt, swag, docker

---

## Example usage
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.swag_docker
```

---

## Notes
This page is generated from role metadata (`meta/main.yml`) and kept in sync with the repository layout.
