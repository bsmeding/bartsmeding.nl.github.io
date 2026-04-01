# Ansible Role: nautobot_docker (`bsmeding.nautobot_docker`)

Role to install Nautobot CMDB in Docker container

- **GitHub:** [ansible_role_nautobot_docker](https://github.com/bsmeding/ansible_role_nautobot_docker)
- **Ansible Galaxy:** [bsmeding.nautobot_docker](https://galaxy.ansible.com/bsmeding/nautobot_docker)
- **Latest tag:** `1.4.0`

---

## Quick details
- **Role directory:** `ansible_role_nautobot_docker`
- **Minimum Ansible version:** `2.10`
- **Supported platforms:** Fedora, Debian, Ubuntu, Alpine, ArchLinux
- **Galaxy tags:** nautobot, docker, ssot, ipam, dcim, netdevops

---

## Example usage
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.nautobot_docker
```

---

## Notes
This page is generated from role metadata (`meta/main.yml`) and kept in sync with the repository layout.
