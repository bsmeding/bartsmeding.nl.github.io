# Ansible Role: awx_docker (`bsmeding.awx_docker`)

Role to Install Ansible AWX (opensource Tower) in Docker container

- **GitHub:** [ansible_role_awx_docker](https://github.com/bsmeding/ansible_role_awx_docker)
- **Ansible Galaxy:** [bsmeding.awx_docker](https://galaxy.ansible.com/bsmeding/awx_docker)
- **Latest tag:** `1.2.0`

---

## Quick details
- **Role directory:** `ansible_role_awx_docker`
- **Minimum Ansible version:** `2.10`
- **Supported platforms:** Fedora, Debian, Ubuntu, Alpine, ArchLinux
- **Galaxy tags:** awx, tower, ansible, docker, awx_version_17

---

## Example usage
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.awx_docker
```

---

## Notes
This page is generated from role metadata (`meta/main.yml`) and kept in sync with the repository layout.
