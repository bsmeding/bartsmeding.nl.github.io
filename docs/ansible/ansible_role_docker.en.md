# Ansible Role: docker (`bsmeding.docker`)

Docker for Linux, Forked from geerlingguy.docker.

- **GitHub:** [ansible_role_docker](https://github.com/bsmeding/ansible_role_docker)
- **Ansible Galaxy:** [bsmeding.docker](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/docker/)

---

## Quick details
- **Role directory:** `ansible_role_docker`
- **Minimum Ansible version:** `2.10`
- **Supported platforms:** Fedora, Debian, Ubuntu, Alpine, ArchLinux
- **Galaxy tags:** web, system, containers, docker, orchestration, compose, server

---

## Example usage
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.docker
```

---

## Notes
This page is generated from role metadata (`meta/main.yml`) and kept in sync with the repository layout.
